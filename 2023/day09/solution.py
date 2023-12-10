import operator

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(list(map(int, line.split())))

    return lines


def build_stacks(history):
    stacks = [history]
    while not all(map(lambda x: x == 0, stacks[-1])):
        stacks.append([x - y for x, y in zip(stacks[-1][1:], stacks[-1][:-1])])
    return stacks


def predict(history, op = operator.add, ind = -1):
    stacks = build_stacks(history)
    next = 0
    for stack in reversed(stacks):
        next = op(stack[ind], next)
    return next


def part1(filename):
    input = parse_file(filename)
    ans = sum(map(predict, input))
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = sum(map(lambda h: predict(h, operator.sub, 0), input))
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

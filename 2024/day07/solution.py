import operator

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            res, ops = line.split(':')
            ops = list(map(int, ops.split()))
            lines.append((int(res), ops))

    return lines


def concat(a, b):
    return int(str(a) + str(b))

def computes(test, args, fns):
    partials = set([args[0]])
    args = args[1:]
    while len(args) > 0:
        n = args[0]
        args = args[1:]
        next_partials = set()
        for p in partials:
            for fn in fns:
                res = fn(p, n)
                if res <= test:
                    next_partials.add(res)
        partials = next_partials
    
    return test in partials


def solve(filename, fns):
    input = parse_file(filename)
    ans = 0

    for res, args in input:
        if computes(res, args, fns):
            ans += res
    return ans


def part1(filename):
    ans = solve(filename, [operator.add, operator.mul])
    print(f'P1 {filename}: {ans}')


def part2(filename):
    ans = solve(filename, [operator.add, operator.mul, concat])
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

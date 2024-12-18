from helpers import *


def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            x,y = line.split(',')
            lines.append((int(x), int(y)))

    return lines


def est_fn(_, start, end):
    return mhn_dist(start, end)


def generate_fn(context, cost, loc):
    blocked, size = context
    for dir in cardinals:
        n = vadd(loc, dir)
        if all(map(lambda x: x >= 0 and x <= size, n)) and n not in blocked:
            yield (cost + 1, n)



def part1(filename, size, bytes):
    input = parse_file(filename)
    context = (set(input[:bytes]), size)
    ans,_ = a_star(context, (0,0), (size, size), generate_fn, est_fn)
    print(f'P1 {filename}: {ans}')


def part2(filename, size):
    input = parse_file(filename)
    ans = None
    bottom = 0
    i = len(input) // 2
    top = len(input)
    while True:
        context = (set(input[:i]), size)
        cost,_ = a_star(context, (0,0), (size, size), generate_fn, est_fn)
        if cost == None:
            top = i
        else:
            bottom = i
        i = (top - bottom) // 2 + bottom
        if top - bottom == 1:
            ans = input[bottom]
            break

    print(f'P2 {filename}: {ans[0]},{ans[1]}')


part1('example.txt', 6, 12)
part1('input.txt', 70, 1024)

part2('example.txt', 6)
part2('input.txt', 70)

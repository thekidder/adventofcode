from collections import defaultdict

def parse_file(filename):
    devices = defaultdict(set)
    with open(filename, 'r') as f:
        for line in f:
            device, outputs = line.split(':')
            devices[device] = set(outputs.split())

    return devices


def part1(filename):
    input = parse_file(filename)
    ans = 0

    paths = [['you']]
    changed = True
    while changed:
        changed = False
        next = []
        for path in paths:
            if path[-1] == 'out':
                ans += 1
                continue
            for output in input[path[-1]]:
                if output not in path:
                    next.append(path[:] + [output])
                    changed = True
        paths = next

    print(f'P1 {filename}: {ans}')


def npaths(input, begin, end):
    paths = defaultdict(int)
    paths[begin] += 1
    npaths = 0
    changed = True
    while changed:
        next = defaultdict(int)
        changed = False
        for p, cnt in paths.items():
            if p == end:
                npaths += cnt
                continue
            for out in input[p]:
                next[out] += cnt
                changed = True
        paths = next
    return npaths


def part2(filename):
    input = parse_file(filename)

    a = npaths(input, 'svr', 'fft') * npaths(input, 'fft', 'dac') * npaths(input, 'dac', 'out')
    b = npaths(input, 'svr', 'dac') * npaths(input, 'dac', 'fft') * npaths(input, 'dac', 'out')
    ans = a + b

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example2.txt')
part2('input.txt')

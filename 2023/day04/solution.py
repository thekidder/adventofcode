from collections import defaultdict

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        for l in f:
            _, nums = l.split(':')
            winning, mine = nums.split('|')
            winning = set(map(int, winning.split()))
            mine = set(map(int, mine.split()))
            r.append((winning, mine))

        return r


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for g in input:
        pts = len(g[0] & g[1])
        if pts > 0:
            ans += 2 ** (pts-1)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    copies_per_index = defaultdict(int)
    for i, g in enumerate(input):
        copies_per_index[i] += 1
        ncopies = len(g[0] & g[1])
        for j in range(ncopies):
            copies_per_index[i+j+1] += copies_per_index[i]

    ans = sum(copies_per_index.values())

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

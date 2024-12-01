from collections import defaultdict

def parse_file(filename):
    a = []
    b = []
    with open(filename, 'r') as f:
        for line in f:
            a1,b1 = line.split()
            a.append(int(a1))
            b.append(int(b1))
    return a,b


def part1(filename):
    a,b = parse_file(filename)
    a.sort()
    b.sort()
    ans = 0
    for x,y in zip(a,b):
        ans += abs(x-y)

    print(f'P1 {filename}: {ans}')


def part2(filename):
    a,b = parse_file(filename)
    cnt_b = defaultdict(int)
    for val in b:
        cnt_b[val] += 1
    ans = 0
    for val in a:
        ans += val * cnt_b[val]
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

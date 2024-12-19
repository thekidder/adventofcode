import bisect
import functools

def parse_file(filename):
   with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        towels = sections[0].split(',')
        towels = list(map(lambda x: x.strip(), towels))
        towels.sort()

        designs = sections[1].split()

        return towels, designs

towels = []

@functools.cache
def can_make(design, partial = ''):
    r = 0
    if design == '':
        return 1
    pos = bisect.bisect_left(towels, design[:1])
    for i in range(pos, len(towels)):
        t = towels[i]
        if t > design:
            break
        if design[:len(t)] == t:
             r += can_make(design[len(t):], partial + t)
    return r


def part1(filename):
    global towels
    towels, designs = parse_file(filename)
    ans = 0

    for d in designs:
        if can_make(d, ''):
            ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    global towels
    towels, designs = parse_file(filename)
    ans = 0

    for d in designs:
        r = can_make(d, '')
        ans += r

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

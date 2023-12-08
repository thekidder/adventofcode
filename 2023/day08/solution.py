from collections import defaultdict
import re
import math
# BBB = (DDD, EEE)
pattern = re.compile('(\w+) = \((\w+), (\w+)\)')

def to_ind(c):
    if c == 'L':
        return 0
    return 1

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        instructions = sections[0].strip()

        nodes = sections[1].split('\n')
        for l in nodes:
            m = pattern.match(l)
            r.append((m[1], (m[2], m[3])))

        instructions = list(map(to_ind, instructions))
        return instructions, dict(r)


def part1(filename):
    ins, nodes = parse_file(filename)
    ans = 0
    node = 'AAA'
    while node != 'ZZZ':
        idx = ins[ans % len(ins)]
        node = nodes[node][idx]
        ans += 1
    print(f'P1 {filename}: {ans}')


def part2(filename):
    ins, nodes = parse_file(filename)
    cycle_lens = []
    for n in nodes.keys():
        if n[2] == 'A':
            i = 0
            while n[2] != 'Z':
                idx = ins[i % len(ins)]
                n = nodes[n][idx]
                i += 1
            cycle_lens.append(i)

    print(f'P2 {filename}: {math.lcm(*cycle_lens)}')


part1('example.txt')
part1('input.txt')

part2('example2.txt')
part2('input.txt')

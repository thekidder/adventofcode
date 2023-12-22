from copy import deepcopy
from helpers import *

def coord(str):
    c = str.split(',')
    return tuple(map(int,c))


def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for i,line in enumerate(f):
            a,b = line.split('~')
            a = coord(a)
            b = coord(b)
            if a[2] > b[2]:
                c = a
                a = b
                b = c

            lines.append((a,b, False, i))

    return lines


def sortz(brick):
    return brick[0][2]


def intersect(a,b):
    for xa in range(a[0][0], a[1][0]+1):
        for ya in range(a[0][1], a[1][1]+1):
            for xb in range(b[0][0], b[1][0]+1):
                for yb in range(b[0][1], b[1][1]+1):
                    if xa == xb and ya == yb:
                        return True
    return False


def resting(b, input):
    s = set()
    if b[0][2] == 1:
        return True, s
    for a in input:
        if a == b:
            continue
        if a[1][2] != b[0][2] - 1:
            continue
        if not a[2]:
            continue
        if intersect(a,b):
            s.add((a[0], a[1]))
    return len(s) > 0, s


def sim(input):
    falls = set()
    while not all(map(lambda b: b[2], input)):
        for i,b in enumerate(input):
            if b[2]:
                continue
            r, s = resting(b, input)
            if r:
                input[i] = (b[0], b[1], True, b[3], s)
                continue
            input[i] = (vadd(b[0], (0,0,-1)), vadd(b[1], (0,0,-1)), False, b[3])
            falls.add(b[3])
        input.sort(key=sortz)
    return len(falls)


def part1(filename):
    input = sorted(parse_file(filename), key=sortz)
    # print(input)
    ans = 0

    sim(input)

    all_supports = set()
    dupe_supports = set()
    for b in input:
        all_supports.update(b[4])
        if len(b[4]) > 1:
            dupe_supports.update(b[4])

    for b in input:
        if len(b[4]) == 1 and list(b[4])[0] in dupe_supports:
            dupe_supports.remove(list(b[4])[0])

    ans = len(dupe_supports)

    for b in input:
        if (b[0], b[1]) not in all_supports:
            ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = sorted(parse_file(filename), key=sortz)
    sim(input)
    # print(input)
    ans = 0

    for b in input:
        c = deepcopy(input)
        c.remove(b)
        for i,a in enumerate(c):
            c[i] = (a[0], a[1], False, a[3])

        nfalls = sim(c)
        ans += nfalls
        # print(f'{b}: {nfalls}')

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')

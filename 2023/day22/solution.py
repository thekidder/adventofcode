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
            lines.append([a, b, False, i, None])

    return lines


def sortz(brick):
    return brick[0][2]


def intersect(a,b):
    ax = (a[0][0],a[1][0])
    bx = (b[0][0],b[1][0])
    if bx[0] < ax[0]:
        ax,bx = bx,ax

    ay = (a[0][1],a[1][1])
    by = (b[0][1],b[1][1])
    if by[0] < ay[0]:
        ay,by = by,ay
 
    return ax[1] >= bx[0] and ay[1] >= by[0]

    # for xa in range(a[0][0], a[1][0]+1):
    #     for ya in range(a[0][1], a[1][1]+1):
    #         for xb in range(b[0][0], b[1][0]+1):
    #             for yb in range(b[0][1], b[1][1]+1):
    #                 if xa == xb and ya == yb:
    #                     return True
    # return False


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
        for b in input:
            if b[2]:
                continue
            r, s = resting(b, input)
            if r:
                b[2] = True
                b[4] = s
                continue
            b[0] = vadd(b[0], (0,0,-1))
            b[1] = vadd(b[1], (0,0,-1))
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
    single_supports = set()
    for b in input:
        all_supports.update(b[4])
        if len(b[4]) == 1:
            single_supports.update(b[4])
        elif len(b[4]) > 1:
            dupe_supports.update(b[4])

    ans = len(dupe_supports - single_supports)

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

from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    r = defaultdict(bool)
    with open(filename, 'r') as f:
        lines = f.readlines()
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    r[(x,y)] = True
        return r


dirs = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

def adjacent(r, pos):
    for x in range(-1, 2):
        for y in range(-1,2):
            if x == 0 and y == 0: continue
            npos = vadd(pos, (x,y))
            if npos in r and r[npos]: return True
    return False


def can_move(r, pos, dir):
    if dir[1] != 0:
        return not any([vadd(pos, (x, dir[1])) in r and r[vadd(pos, (x, dir[1]))] for x in range(-1, 2)])
    return not any([vadd(pos, (dir[0], y)) in r and r[vadd(pos, (dir[0], y))] for y in range(-1, 2)])


def printmap(m):
    print('STATE:')
    minb = [sys.maxsize, sys.maxsize]
    maxb = [0, 0]
    for space,elf in m.items():
        if not elf: continue
        minb[0] = min(minb[0], space[0])
        minb[1] = min(minb[1], space[1])

        maxb[0] = max(maxb[0], space[0])
        maxb[1] = max(maxb[1], space[1])
    
    for y in range(minb[1], maxb[1]+1):
        for x in range(minb[0], maxb[0]+1):
            if (x,y) in m and m[(x,y)]:
                print('#',end='')
            else:
                print('.',end='')
        print()
 

def part1(filename):
    m = parse_file(filename)
    for round in range(10000):
        proposals = defaultdict(int)
        actions = {}
        # printmap(m)
        for space,elf in m.items():
            if not elf: continue
            if not adjacent(m, space):
                actions[space] = space
            else:
                for d in dirs:
                    if can_move(m, space, d):
                        next = vadd(space, d)
                        # print(f'{space} MOVES {d} TO {next}')
                        actions[space] = next
                        proposals[next] += 1
                        break
                else:
                    actions[space] = space
                    # print(f'{space} CANT MOVE {d}')

        n = defaultdict(bool)
        has_moves = False
        for prev,next in actions.items():
            if prev == next or proposals[next] > 1:
                n[prev] = True
            else:
                has_moves = True
                n[next] = True

        if not has_moves:
            print(f'ENDED AT ROUND {round+1}')
            sys.exit(1)
        m = n

        d = dirs.pop(0)
        dirs.append(d)

    elves = 0
    minb = [sys.maxsize, sys.maxsize]
    maxb = [0, 0]
    for space,elf in m.items():
        if not elf: continue
        elves += 1
        minb[0] = min(minb[0], space[0])
        minb[1] = min(minb[1], space[1])

        maxb[0] = max(maxb[0], space[0])
        maxb[1] = max(maxb[1], space[1])

    ans = (maxb[0] - minb[0]+1) * (maxb[1] - minb[1]+1) - elves

    print(f'P1 {filename}: {maxb} {minb} {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')

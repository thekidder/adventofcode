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
    m = defaultdict(list)
    with open(filename, 'r') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    # pass
                    m[(x,y)] = None
                elif c == '.':
                    pass
                    m[(x,y)] = []
                else:
                    m[(x,y)] = [dirs[c]]

        bounds = list(functools.reduce(lambda a,b: map(max, a, b), m.keys()))

        start = None
        end = None
        for x in range(bounds[0]+1):
            if m[(x, 0)] == []:
                start = (x,0)
            if m[(x, bounds[1])] == []:
                end = (x, bounds[1])


        return m, bounds, start, end


def next_blizzard(m, bounds, pos, dir):
    if dir == (-1,0) and pos[0] == 1:
        return (bounds[0]-1, pos[1])
    if dir == (1,0) and pos[0] == bounds[0]-1:
        return (1, pos[1])
    if dir == (0,-1) and pos[1] == 1:
        return (pos[0], bounds[1] - 1)
    if dir == (0,1) and pos[1] == bounds[1]-1:
        return (pos[0], 1)
    
    return vadd(dir, pos)


def sim(m, bounds):
    n = defaultdict(list)
    for coord, blizzards in m.items():
        if blizzards == None:
            n[coord] = None
        else:
            for b in blizzards:
                n[next_blizzard(m, bounds, coord, b)].append(b)
    return n
        

def moves(m, pos):
    r = []
    if m[pos] is not None and len(m[pos]) == 0:
        r.append(pos)
    for d in dirs.values():
        n = vadd(d, pos)
        if n[1] < 0: continue
        if m[n] is not None and len(m[n]) == 0:
            r.append(n)
    return r


def printmap(m, bounds):
    for y in range(bounds[1]+1):
        for x in range(bounds[0]+1):
            c = ''
            if m[(x,y)] == None:
                c = '#'
            elif len(m[(x,y)]) == 0:
                c = '.'
            elif len(m[(x,y)]) == 1:
                c = to_dirs[m[(x,y)][0]]
            else:
                c = str(len(m[(x,y)]))
            print(c, end='')
        print()

def part1(filename):
    m, bounds, start, end = parse_file(filename)
    states = set([start])
    time = 0
    goals = [end, start, end]
    while len(goals):
        # printmap(m,bounds)
        # print(f'{len(states)} states at time {time}: {states}')
        m = sim(m, bounds)
        t = set()
        for s in states:
            t.update(moves(m, s))
        states = t
        time += 1
        # if time == 20:
        #     sys.exit(1)
        if goals[0] in states:
            print(f'{goals[0]} at {time}')
            g = goals.pop(0)
            states = set([g])
            

    print(f'P1 {filename}: {time}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')

# part1('simple.txt')

# part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')

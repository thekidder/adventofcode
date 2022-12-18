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
    r = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            r.append(tuple(map(int, l.split(','))))
            
        return r


def part1(filename):
    input = parse_file(filename)
    edges = defaultdict(int)
    for coord in input:
        edges[(coord[0], coord[1], coord[2], 'X')] += 1
        edges[(coord[0], coord[1], coord[2], 'Y')] += 1
        edges[(coord[0], coord[1], coord[2], 'Z')] += 1

        edges[(coord[0]-1, coord[1], coord[2], 'X')] += 1
        edges[(coord[0], coord[1]-1, coord[2], 'Y')] += 1
        edges[(coord[0], coord[1], coord[2]-1, 'Z')] += 1
    ans = 0
    for edge in edges.values():
        if edge == 1:
            ans += 1
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    edges = defaultdict(int)

    filled = {x: True for x in input}

    xs = (sys.maxsize, 0)
    ys = (sys.maxsize, 0)
    zs = (sys.maxsize, 0)

    for coord in input:
        xs = (min(xs[0], coord[0]), max(xs[1], coord[0]))
        ys = (min(ys[0], coord[1]), max(ys[1], coord[1]))
        zs = (min(zs[0], coord[2]), max(zs[1], coord[2]))
        edges[(coord[0], coord[1], coord[2], 'X')] += 1
        edges[(coord[0], coord[1], coord[2], 'Y')] += 1
        edges[(coord[0], coord[1], coord[2], 'Z')] += 1

        edges[(coord[0]-1, coord[1], coord[2], 'X')] += 1
        edges[(coord[0], coord[1]-1, coord[2], 'Y')] += 1
        edges[(coord[0], coord[1], coord[2]-1, 'Z')] += 1

    ans = 0

    memo = {}
    def is_inside(c):
        q = [c]
        all = set()
        while len(q) > 0:
            c = q.pop()
            # print(c)
            # print(f'check {c}')
            if c not in filled:
                if c in memo:
                    if memo[c]:
                        break
                    else:
                        # for c in all:
                        #     memo[c] = False
                        return False
                all.add(c)
                if c[0] <= xs[0] or c[0] >= xs[1] or \
                    c[1] <= ys[0] or c[1] >= ys[1] or \
                    c[2] <= zs[0] or c[2] >= zs[1]:
                    # for c in all:
                    #     memo[c] = False
                    return False
                for n in [
                    (c[0]-1, c[1], c[2]),
                    (c[0], c[1]-1, c[2]),
                    (c[0], c[1], c[2]-1),
                    (c[0]+1, c[1], c[2]),
                    (c[0], c[1]+1, c[2]),
                    (c[0], c[1], c[2]+1),
                ]:
                    if n not in all and n not in filled:
                        q.append(n)
        for c in all:
            memo[c] = True
        return True

    print(xs,ys,zs)
    for x in range(xs[0], xs[1]+1):
        for y in range(ys[0], ys[1]+1):
            for z in range(zs[0], zs[1]+1):
                coord = (x,y,z)
                if coord in filled:
                    continue
                # print(x,y,z)
                if is_inside(coord):
                    edges[(coord[0], coord[1], coord[2], 'X')] += 10
                    edges[(coord[0], coord[1], coord[2], 'Y')] += 10
                    edges[(coord[0], coord[1], coord[2], 'Z')] += 10

                    edges[(coord[0]-1, coord[1], coord[2], 'X')] += 10
                    edges[(coord[0], coord[1]-1, coord[2], 'Y')] += 10
                    edges[(coord[0], coord[1], coord[2]-1, 'Z')] += 10

    print(len(memo))
    print(len(filled))

    for edge in edges.values():
        if edge == 1:
            ans += 1

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

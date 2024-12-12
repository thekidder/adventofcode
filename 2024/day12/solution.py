from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *


def flood_fill(m, pos):
    t = m[pos]
    area = set([pos])

    open = [pos]
    while len(open):
        p = open.pop()
        for n in neighbors(p):
            if n in m and m[n] == t and n not in area:
                area.add(n)
                open.append(n)

    return area


def perimeter(m, plot):
    t = m[next(iter(plot))]
    perimeter = set()
    for p in plot:
        for dir in cardinals:
            n = vadd(dir, p)
            if n not in m or m[n] != t:
                perimeter.add((n, dir))

    return perimeter


def part1(filename):
    input,_,_ = parse_grid(filename)
    ans = 0

    plots = []

    for pos in input.keys():
        if any(filter(lambda x: pos in x, plots)):
            continue
        plots.append(flood_fill(input, pos))

    for p in plots:
        t = input[next(iter(p))]
        # print(f'{t}: area {len(p)}, perimeter {perimeter(input, p)}')
        ans += len(p) * len(perimeter(input, p))

    print(f'P1 {filename}: {ans}')


def adjacent(a, o):
    for b in o:
        if mhn_dist(a[0], b[0]) == 1 and a[1] == b[1]:
            return True
    return False

def sides(m, plot):
    t = m[next(iter(plot))]
    perim = sorted(perimeter(m, plot))

    sides = []

    for a in perim:
        if any(filter(lambda x: a in x, sides)):
            continue
        side = set([a])
        for b in perim:
            if a == b or any(filter(lambda x: b in x, sides)):
                continue
            if adjacent(b, side):
                side.add(b)
        sides.append(side)

    # print(sides)
    return len(sides)


def part2(filename):
    input,_,_ = parse_grid(filename)
    ans = 0

    plots = []

    for pos in input.keys():
        if any(filter(lambda x: pos in x, plots)):
            continue
        plots.append(flood_fill(input, pos))

    for p in plots:
        t = input[next(iter(p))]
        # print(f'{t}: area {len(p)}, sides {sides(input, p)}')
        ans += len(p) * sides(input, p)
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

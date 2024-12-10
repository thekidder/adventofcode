from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *


def score(m, pos):
    open = set([pos])
    closed = set()
    ends = set()
    while len(open):
        p = open.pop()
        val = m[p]
        if m[p] == 9:
            ends.add(p)
        closed.add(p)
        for dir in cardinals:
            n = vadd(p, dir)
            if n in m and n not in closed and m[n] == val + 1:
                open.add(n)
    return len(ends)


def score2(m, pos):
    trails = [[pos]]
    completed = 0
    while len(trails):
        trail = trails.pop()
        p = trail[-1]
        if m[p] == 9:
            completed += 1
            continue
        val = m[p]
        for dir in cardinals:
            n = vadd(p, dir)
            if n in m and m[n] == val + 1:
                trails.append(trail + [n])
    return completed



def part1(filename):
    input,_,_ = parse_grid(filename)
    print(input)

    ans = 0
    for pos,v in input.items():
        if v == 0:
            s = score(input, pos)
            print(f'{pos}: {s}')
            ans += s

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input,_,_ = parse_grid(filename)
    print(input)

    ans = 0
    for pos,v in input.items():
        if v == 0:
            s = score2(input, pos)
            print(f'{pos}: {s}')
            ans += s

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

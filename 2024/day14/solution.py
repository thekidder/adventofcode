from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
pattern = re.compile('p=(\d+),(\d+) v=(-?[\d]+),(-?[\d]+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group
# p=0,4 v=3,-3

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            m = pattern.match(line)
            lines.append(((int(m.group(1)), int(m.group(2))), ((int(m.group(3)), int(m.group(4))))))

    return lines


def sim(robot, w, h):
    p, v = robot

    p = vadd(p, v)
    p = (p[0] % w, p[1] % h)

    return (p, v)


def print_robots(input, w, h):
    grid = defaultdict(int)
    for r in input:
        p, _ = r
        grid[p] += 1
    print_grid(grid, w-1, h-1)
    print('')


def area(input):
    x = y = 0
    w = h = 200
    for r in input:
        p, _ = r
        x = max(x, p[0])
        y = max(y, p[1])
        w = max(w, p[0])
        h = max(h, p[1])
    return (w - x) * (h - y)


def nrobots(input, x, y, w, h):
    n = 0
    for r in input:
        p, _ = r
        if p[0] >= x and p[0] <= w and p[1] >= y and p[1] <= h:
            n += 1
    return n


def max_overlap(input):
    n = 0
    positions = defaultdict(int)
    for r in input:
        p, _ = r
        positions[p] += 1
    return max(positions.values())


def part1(filename, w, h):
    input = parse_file(filename)
    # print_robots(input, w, h)
    
    for iter in range(8000):
        for i in range(len(input)):
            input[i] = sim(input[i], w, h)
        # if (iter - 37) % 101 == 0:
        # if iter > 6000:
        # print(iter+1)
        # print_robots(input, w, h)
            # print(nrobots(input, w / 4, h / 4, 3 * w / 4, 3 * h / 4))
        n = nrobots(input, w / 4, h / 4, 3 * w / 4, 3 * h / 4)
            # m = max_overlap(input)
        if n > 300:
        # if area(input) < 9800:
            print('DENSITY', iter+1, n)
            print_robots(input, w, h)
            # if m > 4:
            #     print('OVERLAP', iter, m)
            #     print_robots(input, w, h)



    # print_robots(input, w, h)
    a = b = c = d = 0
    for r in input:
        p, _ = r
        # print(p)
        if p[0]+1 < (w+1) / 2 and p[1]+1 < (h+1) / 2:
            print(p)
            a += 1
        elif p[0]+1 > (w+1) / 2 and p[1]+1 < (h+1) / 2:
            b += 1
        elif p[0]+1 < (w+1) / 2 and p[1]+1 > (h+1) / 2:
            c += 1
        elif p[0]+1 > (w+1) / 2 and p[1]+1 > (h+1) / 2:
            d += 1
    print(a, b, c, d)
    ans = a * b * c * d


    print(f'P1 {filename}: {ans}')


part1('example.txt', 11, 7)
part1('input.txt', 101, 103)

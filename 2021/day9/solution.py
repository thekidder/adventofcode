from collections import defaultdict, Counter

import functools
import math
import re
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append([h for h in map(int, line.strip())])

    return lines


def neighbors(lines, x, y):
    if x > 0:
        yield lines[y][x-1]
    if x < len(lines[0]) - 1:
        yield lines[y][x+1]
    if y > 0:
        yield lines[y-1][x]
    if y < len(lines) - 1:
        yield lines[y+1][x]


def neighbors_pos(lines, x, y):
    if x > 0:
        yield (x-1,y)
    if x < len(lines[0]) - 1:
        yield (x+1,y)
    if y > 0:
        yield (x,y-1)
    if y < len(lines) - 1:
        yield (x,y+1)


def flood(lines, x, y):
    open = set()
    open.add((x,y))
    closed = set()

    s = 0

    while len(open) > 0:
        p = open.pop()
        # print(f'GOT {p}')
        closed.add(p)

        last = lines[p[1]][p[0]]


        for n in neighbors_pos(lines, p[0], p[1]):
            val = lines[n[1]][n[0]]
            # print(f'investigate {n}')
            if val == 9 or val <= last:
                continue
            if n not in closed:
                open.add(n)

    return len(closed)


def part1(filename):
    ans = 0
    lines = parse_file(filename)
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            low = True
            for n in neighbors(lines, x, y):
                if n <= h:
                    low = False
            if low:
                ans += h + 1 
    print(f'ANSWER: {ans}')


def part2(filename):
    lines = parse_file(filename)
    low_points = []
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            low = True
            for n in neighbors(lines, x, y):
                if n <= h:
                    low = False
            if low:
                low_points.append((x,y))

    sizes = []
    for p in low_points:
        b = flood(lines, p[0],p[1])
        print(f'basin size: {b}')
        sizes.append(b)

    sizes.sort()

    ans = 1
    for i in sizes[-3:]:
        ans *= i

    
    print(f'ANSWER: {ans}')


part2('input.txt')

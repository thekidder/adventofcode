from collections import defaultdict, Counter

import functools
import math
import re
import sys


# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group


def visible_h(trees, coord):
    x, y = coord
    row = trees[y]
    h = row[x]
    if x == 0 or x == len(row) - 1:
        return True
    for i in range(x-1, -1, -1):
        if row[i] >= h:
            break
        if i == 0:
            return True
    for i in range(x+1, len(row), 1):
        if row[i] >= h:
            break
        if i == len(row) - 1:
            return True
    return False


def visible_v(trees, coord):
    x, y = coord
    row = trees[y]
    h = trees[y][x]
    if y == 0 or y == len(trees) - 1:
        return True
    for i in range(y-1, -1, -1):
        if trees[i][x] >= h:
            break
        if i == 0:
            return True
    for i in range(y+1, len(trees), 1):
        if trees[i][x] >= h:
            break
        if i == len(trees) - 1:
            return True
    return False


def scenic_h(trees, coord):
    x, y = coord
    row = trees[y]
    h = row[x]
    p = 0
    n = 0
    if x == 0 or x == len(row) - 1:
        return 0
    for i in range(x-1, -1, -1):
        p += 1
        if row[i] >= h:
            break
    for i in range(x+1, len(row), 1):
        n += 1
        if row[i] >= h:
            break
    return n*p


def scenic_v(trees, coord):
    x, y = coord
    h = trees[y][x]
    if y == 0 or y == len(trees) - 1:
        return 0
    p = 0
    n = 0
    for i in range(y-1, -1, -1):
        p += 1
        if trees[i][x] >= h:
            break
    for i in range(y+1, len(trees), 1):
        n += 1
        if trees[i][x] >= h:
            break
    return n * p

def parse_file(filename):
    trees = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for t in line.strip():
                row.append(int(t))
            trees.append(row)
            
        return trees


def part1(filename):
    ans = 0
    input = parse_file(filename)
    for x in range(len(input[0])):
        for y in range(len(input)):
            if visible_h(input, (x,y)) or visible_v(input, (x,y)):
                ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    for x in range(len(input[0])):
        for y in range(len(input)):
            c = scenic_h(input, (x,y)) * scenic_v(input, (x,y))
            if c > 0:
                print(f'{x},{y}: {c}')
            if c > ans:
                ans = c
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

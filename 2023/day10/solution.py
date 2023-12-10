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
    m = {}
    mx = 0
    my = 0
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            my = max(my, y+1)
            for x, c in enumerate(line.strip()):
                mx = max(mx, x+1)
                m[(x,y)] = c

    return m,mx,my


def connected_cells(m, coord):
    if coord not in m:
        return []
    if m[coord] == '.':
        return []
    if m[coord] == '-':
        return [vadd(dirs['W'], coord), vadd(dirs['E'], coord)]
    if m[coord] == '|':
        return [vadd(dirs['N'], coord), vadd(dirs['S'], coord)]
    if m[coord] == 'F':
        return [vadd(dirs['E'], coord), vadd(dirs['S'], coord)]
    if m[coord] == '7':
        return [vadd(dirs['W'], coord), vadd(dirs['S'], coord)]
    if m[coord] == 'L':
        return [vadd(dirs['E'], coord), vadd(dirs['N'], coord)]
    if m[coord] == 'J':
        return [vadd(dirs['W'], coord), vadd(dirs['N'], coord)]
    if m[coord] == 'S':
        return [vadd(dirs['W'], coord), vadd(dirs['N'], coord), vadd(dirs['E'], coord), vadd(dirs['S'], coord)]


def set_dist(m, src, dist, r):
    neighbors = connected_cells(m, src)
    for coord in neighbors:
        if src not in connected_cells(m, coord):
            continue
        # print(coord, dist, r[coord])
        if dist + 1 < r[coord]:
            r[coord] = dist + 1
            # print(src, coord, m[coord], dist, r[coord])
            # print(f'{m[src]} -> {m[coord]} at {dist} ({src},{coord})')
            set_dist(m, coord, dist+1, r)


sys.setrecursionlimit(100000)
def part1(filename):
    input,mx,my = parse_file(filename)
    for coord, v in input.items():
        if v != 'S':
            continue
        max_from_coord = defaultdict(lambda: float('inf'))
        max_from_coord[coord] = 0
        set_dist(input, coord, 0, max_from_coord)
    print(f'P1 {filename}: {max(max_from_coord.values())}')


def flood_fill(coord, m, dst, skip, c):
    visited = set()
    next = set([coord])
    while len(next) > 0:
        coord = next.pop()
        dst[coord] = c
        visited.add(coord)
        neighbors = map(lambda x: vadd(x, coord), dirs.values())
        for n in neighbors:
            if n in skip or n in visited or n not in m:
                continue
            
            next.add(n)


def printm(m, mx, my):
    for y in range(my):
        for x in range(mx):
            print(m[(x,y)], end = '')
        print()


turn_right = {
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0)
}

turn_left = {
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0)
}

def traverse(c, m):
    inside = (0, -1)
    coord = c
    prev = None
    started = True
    while coord != c or started:
        neighbors = connected_cells(m, coord)
        for nbc in neighbors:
            if m[nbc] == '0':
                continue
            if coord not in connected_cells(m, nbc):
                continue
            if nbc == prev:
                continue
            started = False
            prev = coord

            if m[vadd(inside, nbc)] == '.' or m[vadd(inside, nbc)] == '0':
                m[vadd(inside, nbc)] = '*'

            dir = vsub(nbc, coord)
            # print(coord, inside, vadd(inside, coord), dir, m[nbc])
            # print(dir)

            if dir == (1, 0) and m[nbc] == '7':
                inside = turn_right[inside]
            if dir == (0, -1) and m[nbc] == '7':
                inside = turn_left[inside]

            if dir == (-1, 0) and m[nbc] == 'L':
                inside = turn_right[inside]
            if dir == (0, 1) and m[nbc] == 'L':
                inside = turn_left[inside]

            if dir == (0, -1) and m[nbc] == 'F':
                inside = turn_right[inside]
            if dir == (-1, 0) and m[nbc] == 'F':
                inside = turn_left[inside]

            if dir == (0, 1) and m[nbc] == 'J':
                inside = turn_right[inside]
            if dir == (1, 0) and m[nbc] == 'J':
                inside = turn_left[inside]

            if m[vadd(inside, nbc)] == '.' or m[vadd(inside, nbc)] == '0':
                m[vadd(inside, nbc)] = '*'

            coord = nbc
            break

def part2(filename):
    input,mx,my = parse_file(filename)
    pipes = defaultdict(lambda: float('inf'))
    snake = None
    for coord, v in input.items():
        if v != 'S':
            continue
        snake = coord
        pipes[coord] = 0
        set_dist(input, coord, 0, pipes)

    # visited = set()
    for coord,v in input.items():
        if coord not in pipes:
            input[coord] = '.'
    flood_fill((0,0), input, input, pipes, '0')

    printm(input,mx,my)
    print()

    traverse(snake, input)

    # inside = set()
    for coord,v in input.items():
        if v == '*':
            flood_fill(coord, input, input, pipes, '*')
    
    printm(input,mx,my)

    ans = len(list(filter(lambda x: x[1] == '*', input.items())))
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example2.txt')
# not 548
# not 84
# 244: too low
part2('input.txt')

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
    with open(filename, 'r') as f:
        bounds = [0,0]
        final_map = {}
        file = f.read()
        map,path = file.split('\n\n')
        lines = map.split('\n')
        start = None
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == ' ':
                    continue
                if start is None and lines[y][x] == '.':
                    start = (x,y)
                bounds[0] = max(bounds[0], x)
                bounds[1] = max(bounds[1], y)
                final_map[(x,y)] = True if lines[y][x] =='#' else False
        
        token = ''
        final_path = []
        for c in path:
            if c >= '0' and c <= '9':
                token += c
            else:
                final_path.append(int(token))
                token = ''
                final_path.append(c)
        if len(token) > 0:
            final_path.append(int(token))

        return start, final_map, final_path, bounds
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines

dirs = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

edges = [
    (0, 0),
    (3, 0),
    (3, 3),
    (0, 3)
]

def rotate(cur, dir):
    # print(f'ROTATE {cur} {dir}')
    dir = 1 if dir == 'R' else -1
    return (cur + dir) % 4


def next(map, loc, dir):
    n = vadd(loc, dirs[dir])
    if n in map:
        return n

    print('BACKTRACK')

    opp = (2 + dir) % 4
    prev = loc
    while loc in map:
        prev = loc
        loc = vadd(loc, dirs[opp])
        print(f'backtrack {loc} {prev}')
    return prev

def part1(filename):
    dir = 0
    loc, map, path, bounds = parse_file(filename)

    for p in path:
        if type(p) == int:
            for i in range(p):
                prev = loc
                loc = next(map, loc, dir)
                print(f'??? wat {loc}')
                if map[loc]:
                    print(f'WALL AT {loc}')
                    loc = prev
                    break
        else:
            dir = rotate(dir, p)
        print(f'NEXT {loc} {dir}')
    print(f'FINAL {loc} {dir}')



    ans = 1000 * (loc[1] + 1) + 4 * (loc[0] + 1) + dir
    print(f'P1 {filename}: {ans} {loc} {dir}')


def in_line(x, a, b):
    if a[0] == b[0]:
        if x[0] != a[0]: return False
        return x[1] >= a[1] and x[1] <= b[1]

    if a[1] != b[1]: return False

    if x[1] != a[1]: return False
    return x[0] >= a[0] and x[0] <= b[0]


def nextp2(m, loc, dir, neighbors):
    n = vadd(loc, dirs[dir])
    if n in m:
        return n, dir

    print('FACE OFF')
    for src_edge, dst_edge in neighbors.items():
        src_start = src_edge[:2]
        src_end = vadd(src_edge[:2], src_edge[2:4])
        l = sorted([src_start, src_end])

        # print(src_edge[:2], loc, src_start, src_end)

        if in_line(loc, l[0], l[1]) and dir == src_edge[4]:
            print(f'EDGE FROM {src_edge} to {dst_edge}')
            dst = mhn_dist(src_start, loc)
            # print(src_start, loc)

            dst_start = dst_edge[:2]
            dst_dir = dst_edge[4] + 2
            dir = tuple(map(sign, dst_edge[2:4]))
            print(dir)
            final = vadd((dir[0] * dst, dir[1] * dst), dst_start)

            # print(f'TO FINAL {final} {dst_dir % 4}')
            return final, dst_dir % 4
        print(f'NO EDGE AT {loc} {dir}')


def part2(filename, neighbors):
    keys = list(neighbors.keys())
    for k in keys:
        v = neighbors[k]
        neighbors[v] = k

    dir = 0
    loc, map, path, bounds = parse_file(filename)

    for p in path:
        if type(p) == int:
            for i in range(p):
                prev = loc
                prev_dir = dir
                loc, dir = nextp2(map, loc, dir, neighbors)
                # print(f'??? wat {loc} {dir}')
                if map[loc]:
                    # print(f'WALL AT {loc}')
                    loc = prev
                    dir = prev_dir
                    break
        else:
            dir = rotate(dir, p)
        # print(f'NEXT {loc} {dir}')
    print(f'FINAL {loc} {dir}')



    ans = 1000 * (loc[1] + 1) + 4 * (loc[0] + 1) + dir
    print(f'P2 {filename}: {ans} {loc} {dir}')

# part1('example.txt')
# part1('input.txt')

neighbors_example = {
    # in order of edge directions:
    # edge start coord, edge span, rotation -> edge start coord, edge dir, relative rotation
    (8, 11, 3, 0, 1):  (3, 7,   -3, 0,   1),
    (11, 4, 0, 3, 0): (15, 8,   -3, 0,   3),
    (4, 4, 3, 0, 3): (8, 0,   0, 3,   2),
}

neighbors_input = {
    # in order of edge directions:
    # edge start coord, edge span, rotation -> edge start coord, edge span, rotation
    (50,   0,  49, 0,   3):  (0,  150,  0, 49,   2), # A -> J
    (100,  0,  49, 0,   3):  (0,  199,  49, 0,   1), # B -> I
    (149,  0,  0, 49,   0):  (99, 149,  0, -49,  0), # C -> F
    (100, 49,  49, 0,   1):  (99,  50,  0, 49,   0), # D -> E
    (50, 149,  49, 0,   1):  (49, 150,  0, 49,   0), # G -> H
    (0,  100,  0, 49,   2):  (50,  49,  0, -49,  2), # K -> N
    (50,  99,  0, -49,  2):  (49, 100,  -49, 0,  3), # M -> L
}

# part2('example.txt', neighbors_example)
part2('input.txt', neighbors_input)

# 34391 too low
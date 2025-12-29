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


def find_portal(map, a, portal_positions):
    b = None
    e = None
    for n in cardinal_neighbors(a):
        if n not in map:
            continue
        if map[n] >= 'A' and map[n] <= 'Z':
            b = n
        if map[n] == '.':
            e = n
    portal_positions.add(b)
    if e is None:
        for n in cardinal_neighbors(b):
            if map[n] == '.':
                e = n
    return e, ''.join(sorted([map[a],map[b]]))


def parse(data):
    grid,sx,sy = parse_grid(data)
    portal_positions = set()
    portal_entries = defaultdict(list)
    portals = {}
    entry = None
    exit = None
    for c,v in grid.items():
        if v >= 'A' and v <= 'Z' and c not in portal_positions:
            portal_positions.add(c)
            entry, code = find_portal(grid, c, portal_positions)
            portal_entries[code].append(entry)
    for code, exits in portal_entries.items():
        if code == 'AA':
            entry = exits[0]
        elif code == 'ZZ':
            exit = exits[0]
        else:
            portals[exits[0]] = exits[1]
            portals[exits[1]] = exits[0]
    return grid, entry, exit, portals


def parse2(data):
    grid,sx,sy = parse_grid(data)
    portal_positions = set()
    portal_entries = defaultdict(list)
    portals = {}
    entry = None
    exit = None
    for c,v in grid.items():
        if v >= 'A' and v <= 'Z' and c not in portal_positions:
            portal_positions.add(c)
            entry, code = find_portal(grid, c, portal_positions)
            portal_entries[code].append(entry)
    for code, exits in portal_entries.items():
        if code == 'AA':
            entry = exits[0]
        elif code == 'ZZ':
            exit = exits[0]
        else:
            offset = 0
            if exits[0][1] == 2 or exits[0][1] == sy - 2 or exits[0][0] == 2 or exits[0][0] == sx - 2:
                offset = -1
            else:
                offset = 1
            
            portals[exits[0]] = (exits[1], offset)
            portals[exits[1]] = (exits[0], -offset)
    return grid, entry, exit, portals


def map_neighbors(grid, portals, c):
    for n in cardinal_neighbors(c):
        if n in grid and grid[n] == '.':
            yield n
    if c in portals:
        yield portals[c]


def part1(data):
    grid, entry, exit, portals = parse(data)
    visited = defaultdict(lambda: 9999999)

    open = [(entry, 0)]

    while len(open):
        c, dist = open.pop()
        for n in map_neighbors(grid, portals, c):
            if dist + 1 < visited[n]:
                visited[n] = dist + 1
                open.append((n, dist+1))
    
    return visited[exit]


def map_neighbors2(grid, portals, lvl, c):
    for n in cardinal_neighbors(c):
        if n in grid and grid[n] == '.':
            yield lvl, n
    if c in portals:
        next_coord, offset = portals[c]
        if offset + lvl >= 0 and offset + lvl <= 25:
            yield offset + lvl, next_coord


def part2(data):
    grid, entry, exit, portals = parse2(data)
    visited = defaultdict(lambda: 9999999)

    open = [(0, entry, 0)]

    while len(open):
        lvl, coord, dist = open.pop()
        for next_lvl, next_coord in map_neighbors2(grid, portals, lvl, coord):
            k = (next_lvl, next_coord)
            if dist + 1 < visited[k]:
                visited[k] = dist + 1
                open.append((next_lvl, next_coord, dist+1))
    
    return visited[(0, exit)]


check(part1, 'example1.txt', 23)
check(part1, 'example2.txt', 58)
exec(part1, 'input.txt')

check(part2, 'example1.txt', 26)
check(part2, 'example3.txt', 396)
exec(part2, 'input.txt')

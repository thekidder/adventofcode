from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        grid, movements = lines.split('\n\n')
        grid,w,h = parse_grid(grid)
        movements = movements.replace('\n', '')

        return grid, w, h, movements


def parse_file2(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        grid, movements = lines.split('\n\n')
        grid,w,h = parse_grid2(grid)
        movements = movements.replace('\n', '')

        return grid, w, h, movements



def can_move(grid, pos, dir):
    while True:
        v = grid[pos]
        if v == '.':
            return True
        if v == 'O':
            return can_move(grid, vadd(pos, dir), dir)
        if v == '#':
            return False
        pos = vadd(pos, dir)


def move_dep(grid, pos, dir):
    open = [pos]
    closed = set()
    while len(open):
        pos = open.pop()
        if pos in closed:
            continue
        v = grid[pos]
        if v == '.':
            # return True, boxes
            pass
        if v == '[':
            closed.add(pos)
            closed.add((pos[0]+1, pos[1]))
            open.append(vadd(pos, dir))
            open.append(vadd((pos[0]+1, pos[1]), dir))
        if v == ']':
            closed.add(pos)
            closed.add((pos[0]-1, pos[1]))
            open.append(vadd(pos, dir))
            open.append(vadd((pos[0]-1, pos[1]), dir))
        if v == '#':
            return False, []
    return True, list(closed)


def move(grid, char, dest):
    o = grid[dest]
    grid[dest] = char
    return o


def sim(grid, pos, dir):
    dir = dirs[dir]
    last = '.'
    holding = '@'
    if can_move(grid, vadd(pos, dir), dir):
        n = pos
        while True:
            old = n
            n = vadd(n, dir)
            grid[old] = last
            last = holding
            holding = move(grid, holding, n)
            if holding == '.':
                break
        return vadd(pos, dir)
    else:
        return pos


def part1(filename):
    grid, w, h, movements = parse_file(filename)
    print_grid(grid, w, h)
    p = None
    for k, v in grid.items():
        if v == '@':
            p = k
            break

    for i in range(len(movements)):
        # print(f'Move {movements[i]}')
        p = sim(grid, p, movements[i])
        # print_grid(grid, w, h)


    ans = 0
    for p, v in grid.items():
        if v == 'O':
            ans += 100 * p[1] + p[0]
    print(f'P1 {filename}: {ans}')


def sim2(grid, pos, dir):
    dir = dirs[dir]
    last = '.'
    holding = '@'
    n = vadd(pos, dir)
    can_move, deps = move_dep(grid, n, dir)
    # print(can_move, deps)

    if can_move:
        if dir == (-1, 0):
            deps.sort()
        elif dir == (1, 0):
            deps = reversed(sorted(deps))
        elif dir == (0, -1):
            deps.sort(key=lambda p: p[1])
        elif dir == (0, 1):
            deps.sort(key=lambda p: p[1])
            deps.reverse()
        for p in deps:
            grid[vadd(p, dir)] = grid[p]
            grid[p] = '.'

        grid[pos] = '.'
        move(grid, holding, n)
        return vadd(pos, dir)
    else:
        return pos


def part2(filename):
    grid, w, h, movements = parse_file2(filename)
    print_grid(grid, w, h)

    p = None
    for k, v in grid.items():
        if v == '@':
            p = k
            break

    for i in range(len(movements)):
        print(f'Move {movements[i]}')
        p = sim2(grid, p, movements[i])
        # print_grid(grid, w, h)

    ans = 0
    for p, v in grid.items():
        if v == '[':
            ans += 100 * p[1] + p[0]
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

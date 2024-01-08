from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *
from intcode import *

def get_path_len(grid, start, end):
    cache = defaultdict(lambda: float('inf'))
    queue = [(start, 0)]
    while len(queue) > 0:
        pos, dist = queue.pop(0)
        for dir in dirs.values():
            npos = vadd(pos, dir)
            ndist = dist + 1
            if npos in grid and grid[npos] == '.' and ndist < cache[npos]:
                queue.append((npos, ndist))
    return cache[end]


def neighbors_fn(grid, coord, end):
    for dir in dirs.values():
        next_node = vadd(coord, dir)
        if next_node == end or (next_node in grid and grid[next_node] == '.'):
            yield next_node

def path_to(grid, a, b):
    def cost_fn(a,b):
        return 1
    
    def est_fn(x, y):
        return mhn_dist(x, y)

    cost, path = a_star(cost_fn, est_fn, lambda c: neighbors_fn(grid, c, b), a, b)
    return path


def dir_from(a, b):
    d = vsub(b, a)
    for ind, dir in dirs.items():
        if dir == d:
            return ind
    return None


def solve(filename):
    code = parse(file(filename))

    grid = {}
    start = (0,0)
    pos = start
    goal = None
    grid[pos] = '.'

    q = set([(1,0),(-1,0),(0,-1),(0,1)])
    path = path_to(grid, pos, next(iter(q)))

    i = 0
    last_move = None

    def get_input():
        nonlocal i, last_move
        m =  dir_from(pos, path[0])
        last_move = m
        return m

    prog = run(code, get_input, False)    
    for output in prog:
        if output == 0:
            wall_pos = vadd(dirs[last_move], pos)
            grid[wall_pos] = '#'
            if wall_pos in q:
                q.remove(wall_pos)
                if len(q) == 0:
                    break
                path = path_to(grid, pos, next(iter(q)))
            # print(f'MOVED {last_move}; WALL AT {wall_pos}')
            # print_grid(grid)
        else:
            pos = vadd(dirs[last_move], pos)
            grid[pos] = '.'
            # print(f'MOVED {last_move} to {pos}')
            # print_grid(grid)
            for dir in dirs.values():
                ne = vadd(pos, dir)
                if ne not in grid:
                    q.add(ne)

            if pos in q:
                q.remove(pos)
                path = path_to(grid, pos, next(iter(q)))
            elif len(path) > 1:
                path = path[1:]
            else:
                path = path_to(grid, pos, next(iter(q)))

            if output == 2:
                print(f'FOUND OXYGEN AT {pos}')
                goal = pos

    grid[goal] = 'O'
    print_grid(grid)
    p = path_to(grid, start, goal)
                        
    print(f'P1 {filename}: {len(p)}')

    mins = 0
    while True:
        # if mins % 10 == 0:
        #     print(f'MIN {mins}')
        #     print_grid(grid)
        next_grid = dict(grid.items())
        updates = False
        for coord, val in grid.items():
            if val == 'O':
                for dir in dirs.values():
                    ne = vadd(dir, coord)
                    if ne in grid and grid[ne] == '.':
                        next_grid[ne] = 'O'
                        updates = True
        if not updates:
            break
        mins += 1
        grid = next_grid


    print_grid(grid)

    print(f'P2 {filename}: {mins}')


solve('input.txt')

from collections import defaultdict

import math
import heapq

from helpers import *

def find(grid, w, h, start, end, dir):
    open = []
    heapq.heappush(open, (0, start, dir, 0))

    scores = defaultdict(lambda: math.inf)
    came_from = defaultdict(list)

    i = 0

    best_cost = math.inf
    last_dir = None

    while len(open):
        i += 1
        _, pos, dir, cost = heapq.heappop(open)
        # if i % 1000 == 0:
        #     print(f'iter {i} loc {pos} end {end}')
        if pos == end and cost < best_cost:
            best_cost = cost
            last_dir = dir
        forward = vadd(pos, dirs[dir])
        if forward in grid and grid[forward] == '.':
            new_cost = cost +1
            if new_cost <= scores[(forward, dir)]:
                scores[(forward, dir)] = new_cost
                heapq.heappush(open, (mhn_dist(forward, end)+new_cost, forward, dir, new_cost))
                came_from[(forward, dir)].append((pos, dir))
        turns = [turn_left(dir), turn_right(dir)]
        for t in turns:
            forward = vadd(pos, dirs[t])
            if forward in grid and grid[forward] == '.':
                new_cost = cost + 1000
                if new_cost <= scores[(pos, t)]:
                    scores[(pos, t)] = new_cost
                    heapq.heappush(open, (mhn_dist(pos, end)+new_cost, pos, t, new_cost))
                    came_from[(pos, t)].append((pos, dir))

    open = [(end, last_dir)]
    visited = set()
    best_tiles = set()
    while len(open):
        p = open.pop()
        if p in visited:
            continue
        visited.add(p)
        best_tiles.add(p[0])
        grid[p[0]] = 'O'

        for n in came_from[p]:
            open.append(n)

    print_grid(grid, w, h)
    return best_cost, len(best_tiles)


def solve(filename):
    input,w,h = parse_grid(filename)
    start = [k for k,v in input.items() if v == 'S'][0]
    end = [k for k,v in input.items() if v == 'E'][0]

    input[start] = '.'
    input[end] = '.'

    dir = 'E'
    ans = find(input, w, h, start, end, dir)
    print(f'Solution for {filename}: {ans}')


solve('example.txt')
solve('input.txt')

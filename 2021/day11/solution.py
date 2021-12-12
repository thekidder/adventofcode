from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append([int(c) for c in line.strip()])
    return lines


dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

def neighbors(grid, pos):
    x,y = pos
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
            yield (nx,ny)


def flash(grid, pos):
    flashes = 1
    for nx,ny in neighbors(grid, pos):
        grid[ny][nx] += 1
        if grid[ny][nx] == 10:
            flashes += flash(grid, (nx,ny))
    return flashes


def step(grid):
    flashes = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
            if grid[y][x] == 10:
                flashes += flash(grid, (x,y))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] >= 10:
                grid[y][x] = 0

    return flashes


def pg(grid):
    print('GRID')
    for line in grid:
        print(''.join(map(str, line)))


def sync(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 0:
                return False
    return True


def part1(filename):
    grid = parse_file(filename)
    ans = 0
    for i in range(100):
        ans += step(grid)
        
    # print(step(grid))
    # pg(grid)
    # print(step(grid))
    # print(step(grid))
    pg(grid)
    print(f'ANSWER: {ans}')


def part2(filename):
    grid = parse_file(filename)
    ans = 0
    for i in range(10000):
        ans += step(grid)
        if sync(grid):
            print(f'SYNC AT {i+1}')
            break
        


part2('input.txt')

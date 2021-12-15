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
    (-1, 0), 
    (0, -1), (0, 1),
    (1, 0),
]

def neighbors(grid, pos):
    x,y = pos
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
            yield (nx,ny)


def part1(filename):
    input = parse_file(filename)
    pos = (0,0)
    exit = (len(input[0]) - 1, len(input) - 1)
    ans = 0
    print(input)

    costs = {
        pos: 0
    }

    open = set([pos])

    while len(open) > 0:
        x,y = open.pop()
        cost = costs[(x,y)]
        for nx,ny in neighbors(input, (x,y)):
            ncost = cost + input[ny][nx]
            if (nx,ny) not in costs or ncost < costs[(nx,ny)]:
                costs[(nx,ny)] = ncost
                open.add((nx,ny))

    print(f'ANSWER: {costs[exit]}')


def add_cost(cost):
    return cost + 1 if cost < 9 else 1


def transform_line(input):
    return [l for l in map(add_cost, input)]


def build_map(input):
    input = input[:]
    output = []
    for y in range(5):
        for line in input:
            f = []
            l = line[:]
            for x in range(5):
                f.extend(l)
                l = transform_line(l)
            output.append(f)
        for i in range(len(input)):
            input[i] = transform_line(input[i])

    return output


def part2(filename):
    input = parse_file(filename)
    input = build_map(input)
    pos = (0,0)
    exit = (len(input[0]) - 1, len(input) - 1)
    print(exit)

    costs = {
        pos: 0
    }

    open = set([pos])

    while len(open) > 0:
        x,y = open.pop()
        cost = costs[(x,y)]
        for nx,ny in neighbors(input, (x,y)):
            ncost = cost + input[ny][nx]
            if (nx,ny) not in costs or ncost < costs[(nx,ny)]:
                costs[(nx,ny)] = ncost
                open.add((nx,ny))

    print(f'ANSWER: {costs[exit]}')


part2('input.txt')

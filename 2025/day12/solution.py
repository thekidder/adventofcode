from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
pattern = re.compile('(\d+)x(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')

        shapes = sections[:-1]
        regions = sections[-1]

        shapes = list(map(lambda x: parse_grid(x.split('\n')[1:]), shapes))

        regions = regions.split('\n')
        for region in regions:
            size, quantities = region.split(':')
            m = pattern.match(size)
            x = int(m.group(1))
            y = int(m.group(2))
            quantities = mapl(int, quantities.split())

            r.append((x, y, quantities))
            

        return shapes, r
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def rotate(shape):
    n = {}
    for (x,y), v in shape.items():
        n[(-y+2, x)] = v
    return n


def rotations(r):
    res = [r]
    for _ in range(3):
        r = rotate(r)
        res.append(r)
    return res


def place(grid, shape, coord):
    for p, v in shape.items():
        if v == '.':
            continue
        if grid[vadd(coord, p)] == '#':
            return False
        
    for p, v in shape.items():
        if v == '.':
            continue
        grid[vadd(coord, p)] = '#'

    return True

def gen_coords(sx, sy):
    i = 0
    x = [(1,0), (1,0)]

    # for dist in range()


def bin_pack(shapes, region):
    grid = defaultdict(lambda: '.')

    remaining_shapes = region[2]

    next_shape = None
    for i in range(len(remaining_shapes)):
        if remaining_shapes[i] > 0:
            next_shape = i
            break

    place(grid, shapes[next_shape][0], (0,0))
    print_grid(grid, region[0]-1, region[1]-1)

def can_fit(shapes, region):
    # r = shapes[0][0]
    # print_grid(r, 2, 2)
    # for _ in range(3):
    #     r = rotate(r)
    #     print_grid(r, 2, 2)

    shape_spots = [len(list(filter(lambda x: x == '#', x[0].values()))) for x in shapes]
    taken_spots = sum([shape_spots[i] * region[2][i] for i in range(len(shapes))])
    free_slots = region[0] * region[1] - taken_spots

    if free_slots < 0:
        return 0
    
    return 1 #bin_pack(shapes, region)


def part1(filename):
    shapes, regions = parse_file(filename)

    all_rotations = [rotations(x[0]) for x in shapes]

    # can_fit(all_rotations, regions[0])
    # ans = 0
    ans = sum(map(functools.partial(can_fit, shapes), regions))

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0



    print(f'P2 {filename}: {ans}')


# part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')

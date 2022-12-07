from collections import defaultdict, Counter

import functools
import math
import re
import sys


# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def dist(coord):
    return abs(coord[0]) + abs(coord[1])


def get_dir(d):
    if d == 'U':
        return (0,1)
    elif d == 'D':
        return (0,-1)
    elif d == 'R':
        return (1,0)
    else: 
        return (-1,0)

def find_locations(wire):
    directions = wire.split(',')
    coord = (0, 0)
    locs = set()
    for d in directions:
        num = int(d[1:])
        dir = get_dir(d[0])
        for x in range(num):
            coord = (coord[0] + dir[0], coord[1] + dir[1])
            locs.add(coord)

    return locs


def locs_with_steps(wire):
    directions = wire.split(',')
    coord = (0, 0)
    steps = 0
    locs = {}
    for d in directions:
        num = int(d[1:])
        dir = get_dir(d[0])
        for x in range(num):
            steps += 1
            coord = (coord[0] + dir[0], coord[1] + dir[1])
            if coord not in locs:
                locs[coord] = steps
        
    return locs


def part1(wires):
    first,second = wires.split('\n')
    fl = find_locations(first)
    sl = find_locations(second)
    intersections = fl & sl
    min = sys.maxsize
    for coord in intersections:
        d = dist(coord) 
        if d < min:
            min = d

    print(f'P1 {wires}: {min}')


def part2(wires):
    first,second = wires.split('\n')
    fl = locs_with_steps(first)
    sl = locs_with_steps(second)
    min = sys.maxsize
    for coord in fl:
        if coord in sl:
            d = fl[coord] + sl[coord]
            if d < min:
                min = d

    print(f'P2 {wires}: {min}')


# part1('R8,U5,L5,D3\nU7,R6,D4,L4')
# part1('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83')
# part1(parse_file('input.txt'))

part2('R8,U5,L5,D3\nU7,R6,D4,L4')
part2('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83')
part2(parse_file('input.txt'))

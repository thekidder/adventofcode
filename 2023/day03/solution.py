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
    r = {}
    with open(filename, 'r') as f:
        for (y, l) in enumerate(f):
            for (x, c) in enumerate(l.strip()):
                r[(x,y)] = c


        return r
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def neighbors(coord):
    for xd in range(-1, 2):
        for yd in range(-1, 2):
            if xd == 0 and yd == 0:
                continue
            yield (coord[0] + xd, coord[1] + yd)


def symbol(x):
    return not x.isdigit() and x != '.'

def part1(filename):
    input = parse_file(filename)
    nums = {}
    for coord, el in input.items():
        if el.isdigit():
            nums[coord] = coord
            prev = (coord[0]-1, coord[1])
            while prev in input and input[prev].isdigit():
                nums[coord] = prev
                prev = (prev[0]-1, coord[1])
    
    parts = set()
    for coord, el in input.items():
        for neighbor in neighbors(coord):
            if el.isdigit() and neighbor in input and symbol(input[neighbor]):
                parts.add(nums[coord])

    ans = 0
    parts = sorted(list(parts))
    for coord in parts:
        num = input[coord]
        next = (coord[0]+1, coord[1])
        while next in input and input[next].isdigit():
            num += input[next]
            next = (next[0]+1, coord[1])
        ans += int(num)
        # print(coord, num)


    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    nums = {}
    for coord, el in input.items():
        if el.isdigit():
            nums[coord] = coord
            prev = (coord[0]-1, coord[1])
            while prev in input and input[prev].isdigit():
                nums[coord] = prev
                prev = (prev[0]-1, coord[1])
    
    geartonum = defaultdict(set)
    for coord, el in input.items():
        for neighbor in neighbors(coord):
            if el.isdigit() and neighbor in input and input[neighbor] == '*':
                geartonum[neighbor].add(nums[coord])

    ans = 0
    for gear, coords in geartonum.items():
        if len(coords) != 2:
            continue
        n = 1
        for coord in coords:
            num = input[coord]
            next = (coord[0]+1, coord[1])
            while next in input and input[next].isdigit():
                num += input[next]
                next = (next[0]+1, coord[1])
            n *= int(num)
        ans += n

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

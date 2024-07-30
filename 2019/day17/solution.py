from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *
from intcode import *

example_grid = '''..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..
'''


def read_grid():
    code = parse(file('input.txt'))

    def get_input():
        return 0

    prog = run(code, get_input, False)    
    output = ''
    for code in prog:
        output += chr(code)
    return output


def parse_grid(grid):
    r = {}
    mx = 0
    my = 0
    for (y, l) in enumerate(grid.split()):
        my = y
        for (x, c) in enumerate(l.strip()):
            r[(x,y)] = c
            mx = x

    return r,mx,my


def count_neighbor_scaffolds(grid, loc):
    cnt = 0 
    for offset in dirs.values():
        neighbor_loc = vadd(offset, loc)
        if neighbor_loc in grid and grid[neighbor_loc] == '#':
            cnt += 1
    # print(cnt)
    return cnt


def part1(grid):
    print(grid)
    alignment = 0
    grid, _, _ = parse_grid(grid)
    for loc,val in grid.items():
        if val == '#':
            cnt = count_neighbor_scaffolds(grid, loc)
            if cnt == 4:
                alignment += loc[0] * loc[1]
    print(f'P1: {alignment}')


def part2():
    code = parse(file('input.txt'))
    code[0] = 2

    rules = '''A,B,A,C,B,C,A,C,B,C
L,8,R,10,L,10
R,10,L,8,L,8,L,10
L,4,L,6,L,8,L,8
n
'''

    ind = 0
    def get_input():
        nonlocal ind
        r = ord(rules[ind])
        ind += 1
        return r

    prog = run(code, get_input, False)
    output = ''
    ans = 0
    for code in prog:
        if code < 127:
            output += chr(code)
        else:
            ans = code
    print(output)
    print(f'P2: {ans}')


# part1(example_grid)
# part1(read_grid())

part2()

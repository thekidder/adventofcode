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
    r = []
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()))


def part1(filename):
    input = parse_file(filename)
    indices = list(range(len(input)))
    
    for x in range(len(input)):
        ind = indices.index(x)
        val = input.pop(ind)

        next_ind = (ind + val) % len(input)
        if val != 0 and next_ind == 0:
            next_ind = len(input)
        elif next_ind == len(input):
            next_ind = 0

        input.insert(next_ind, val)

        indices.pop(ind)
        indices.insert(next_ind, x)

        # print(f'{val} moves from {ind}, {ind + val} to {next_ind}: {input}')
    
    ind = input.index(0)
    ans = input[(ind + 1000) % len(input)] + input[(ind + 2000) % len(input)] + input[(ind + 3000) % len(input)]
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = list(map(lambda x: x * 811589153, parse_file(filename)))
    indices = list(range(len(input)))
    
    print(input)
    for i in range(10):
        orig = input[:]
        for x in range(len(input)):
            ind = indices.index(x)
            # ind = input.index(orig[x])
            val = input.pop(ind)

            next_ind = (ind + val) % len(input)
            if val != 0 and next_ind == 0:
                next_ind = len(input)
            elif next_ind == len(input):
                next_ind = 0

            input.insert(next_ind, val)

            indices.pop(ind)
            indices.insert(next_ind, x)

        # print(f'{val} moves from {ind}, {ind + val} to {next_ind}: {input}')
        print(input)
    
    ind = input.index(0)
    ans = input[(ind + 1000) % len(input)] + input[(ind + 2000) % len(input)] + input[(ind + 3000) % len(input)]
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
part2('input.txt')

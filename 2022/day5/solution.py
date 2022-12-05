from collections import defaultdict, Counter

import functools
import math
import re
import sys

from helpers import *

pattern = re.compile('move (\d+) from (\d+) to (\d+)')
# m = pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def chunks(l):
    for i in range(0, len(l), 4):
        yield l[i:i + 4].strip()


def parse_file(filename):
    stacks = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        while True:
            line = lines[0]
            lines = lines[1:]
            if '[' not in line:
                break
            for i, c in enumerate(chunks(line)):
                if i+1 > len(stacks):
                    stacks.append([])
                if len(c) > 0:
                    stacks[i].append(c)

        movements = []
        for line in lines:
            m = pattern.match(line)
            if m is not None:
                movements.append([int(m.group(1)), int(m.group(2))-1, int(m.group(3))-1])


    return stacks,movements

    # group by newlines
    # return grouped_input(filename, int)

def top(stack):
    if len(stack) > 0:
        return stack[0][1]
    return ''

def part1(filename):
    stacks,movements = parse_file(filename)
    for num_crates,from_stack,to_stack in movements:
        for i in range(num_crates):
            crate = stacks[from_stack].pop(0)
            stacks[to_stack].insert(0, crate)
    
    tops = ''.join(map(top, stacks))
    print(f'P1 {filename}: {tops}')


def part2(filename):
    stacks,movements = parse_file(filename)
    for num_crates,from_stack,to_stack in movements:
        crates = stacks[from_stack][0:num_crates]
        stacks[from_stack] = stacks[from_stack][num_crates:]
        stacks[to_stack] = crates + stacks[to_stack]
    
    tops = ''.join(map(top, stacks))
    print(f'P1 {filename}: {tops}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

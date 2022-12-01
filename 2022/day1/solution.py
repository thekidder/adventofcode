from collections import defaultdict, Counter

import re
import math
import sys
import functools

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    elves = []
    elf = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line))
    elves.append(elf)

    return elves


def part1(filename):
    elves = parse_file(filename)
    m = 0
    for elf in elves:
        total = functools.reduce(lambda a,b: a+b, elf)
        print(total)
        if total > m:
            m = total

    print(f'ANSWER: {m}')


def part2(filename):
    elves = parse_file(filename)
    totals = []
    for elf in elves:
        total = functools.reduce(lambda a,b: a+b, elf)
        totals.append(total)

    totals.sort()
    totals = totals[-3:]
    ans = functools.reduce(lambda a,b: a+b, totals)



    print(f'ANSWER: {ans}')


# part2('example.txt')
part2('input.txt')

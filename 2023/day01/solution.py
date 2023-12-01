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
        lines = f.read()
        sections = lines.split('\n\n')

        return r
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def part1(filename):
    ans = 0
    with open(filename, 'r') as f:
        for l in f:
            nums = [x for x in l if x >='0' and x <= '9']
            ans += int(nums[0] + nums[-1])
    print(f'P1 {filename}: {ans}')


def part2(filename):
    ans = 0
    with open(filename, 'r') as f:
        for l in f:
            l = l.replace('one', 'o1e')
            l = l.replace('two', 't2o')
            l = l.replace('three', 't3e')
            l = l.replace('four', 'f4r')
            l = l.replace('five', 'f5e')
            l = l.replace('six', 's6x')
            l = l.replace('seven', 's7n')
            l = l.replace('eight', 'e8t')
            l = l.replace('nine', 'n9e')
            nums = [x for x in l if x >= '0' and x <= '9']
            print(int(nums[0] + nums[-1]))
            ans += int(nums[0] + nums[-1])
    print(f'P1 {filename}: {ans}')


part2('example2.txt')
part2('input.txt')

# part2('example.txt')
# part2('input.txt')

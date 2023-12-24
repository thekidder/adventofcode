from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
pattern = re.compile('(-?\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            nums = pattern.findall(line)
            pos = tuple(map(int, nums[:3]))
            vel = tuple(map(int, nums[3:]))
            lines.append((pos,vel))

    return lines


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for i,j in itertools.combinations(input, 2):
        p1 = i[0][:2]
        p2 = vadd(p1, i[1][:2])

        p3 = j[0][:2]
        p4 = vadd(p3, j[1][:2])
        print(p1,p2,p3,p4)

        dem = (p1[0] - p2[0])*(p3[1]-p4[1])-(p1[1]-p2[1])*(p3[0]-p4[0])

        if dem == 0:
            continue
        num1 = (p1[0]*p2[1] - p1[1]*p2[0])*(p3[0]-p4[0])-(p1[0]-p2[0])*(p3[0]*p4[1]-p3[1]*p4[0])
        num2 = (p1[0]*p2[1] - p1[1]*p2[0])*(p3[1]-p4[1])-(p1[1]-p2[1])*(p3[0]*p4[1]-p3[1]*p4[0])

        xint = num1/dem
        yint = num2/dem

        intmin = 7
        intmax = 27
        intmin = 200000000000000
        intmax = 400000000000000

        slope1 = i[1][1] / i[1][0] 
        slope2 = j[1][1] / j[1][0]

        b1 = p1[1] - slope1*p1[0]
        b2 = p3[1] - slope2*p3[0]

        print(b1,b2,slope1,slope2)

        x1 = (yint - b1)/slope1 - p1[0]
        x2 = (yint - b2)/slope2 - p3[0]

        print(x1,x2)

        if i[1][0] < 0:
            x1 = -x1
        if j[1][0] < 0:
            x2 = -x2

        print(x1,x2)

        if x1 < 0 or x2 < 0:
            continue

        print(xint,yint)

        if xint >= intmin and yint >= intmin and xint <= intmax and yint <= intmax:
            ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0

    for i in itertools.permutations(input, len(input)):
        print(i)

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
part2('input.txt')

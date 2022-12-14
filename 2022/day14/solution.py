from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys


# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def sign(x):
    if x == 0: return 0
    return x // abs(x)

def parse_file(filename):
    r = {}
    max_y = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            coords = list([[int(x) for x in x.split(',')] for x in l.split('->')])
            for i in range(1, len(coords), 1):
                prev_x, prev_y = coords[i-1]
                x, y = coords[i]
                while prev_x != x or prev_y != y:
                    r[(prev_x, prev_y)] = True
                    prev_x += sign(x - prev_x)
                    prev_y += sign(y - prev_y)
                    max_y = max(prev_y, max_y)
                    r[(prev_x, prev_y)] = True


        return r, max_y
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def n(c):
    yield (c[0], c[1]+1)
    yield (c[0]-1, c[1]+1)
    yield (c[0]+1, c[1]+1)

def part1(filename):
    m,max_y = parse_file(filename)
    print(m)
    src = (500, 0)
    ans = 0
    while True:
        sand = src
        while True:
            moving = False
            for nsand in n(sand):
                if nsand not in m:
                    sand = nsand
                    moving = True
                    break
            # print(f'sim step {sand}')
            if not moving:
                if sand not in m:
                    print(f'resting at {sand}')
                    m[sand] = True
                    ans += 1
                    break
                # else:
                #     print(f'P1 {filename}: {ans}')
                #     sys.exit(0)

            if sand[1] > max_y:
                print(f'P1 {filename}: {ans}')
                sys.exit(0)
    


def part2(filename):
    m,max_y = parse_file(filename)
    floor = max_y + 2
    print(m)
    src = (500, 0)
    ans = 0
    while src not in m:
        sand = src
        while True:
            moving = False
            for nsand in n(sand):
                if nsand not in m and sand[1] != floor-1:
                    sand = nsand
                    moving = True
                    break
            # print(f'sim step {sand}')
            if not moving:
                if sand not in m:
                    print(f'resting at {sand}')
                    m[sand] = True
                    ans += 1
                    break
                # else:
                #     print(f'P1 {filename}: {ans}')
                #     sys.exit(0)

    print(f'P1 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
part2('input.txt')

from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group


def simulate(velocity, region):
    xmin,xmax,ymin,ymax = region
    xvel,yvel = velocity

    x = 0
    y = 0

    max_height = 0

    while True:
        x += xvel
        y += yvel
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1

        max_height = max(max_height, y)

        if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
            return True, max_height

        if abs(x) > max(abs(xmin),abs(xmax)) or y < min(ymin,ymax):
            return False, 0


def part1(region):
    max_height = 0
    num = 0
    for x in range(-300, 301):
        for y in range(-300, 301):
            if x == 0 and y == 0:
                continue
            success, h = simulate((x,y), region)
            if success:
                max_height = max(max_height, h)
                num += 1

    print(f'ANSWER: {max_height, num}')


def part2(filename):
    pass


# example
part1((20,30,-10,-5))
# input
part1((144,178,-100,-76))

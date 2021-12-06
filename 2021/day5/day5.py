from ast import parse
import collections
import math
import re
import sys

line_pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')

def sign(x):
    return int(bool(x)) * math.copysign(1, x)


def parse_lines(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            m = line_pattern.match(line)
            if m is None:
                print('ERROR')
                break
            x1 = int(m.group(1))
            y1 = int(m.group(2))

            x2 = int(m.group(3))
            y2 = int(m.group(4))

            lines.append((x1,y1,x2,y2))
    return lines

def part1(file):
    lines = parse_lines(file)
    print(lines)
    grid = collections.defaultdict(int)
    for line in lines:
        x1,y1,x2,y2 = line
        if x1 != x2 and y1 != y2:
            continue

        step_x = sign(x2-x1)
        step_y = sign(y2-y1)

        while x1 != x2 or y1 != y2:
            grid[(x1, y1)] += 1
            x1 += step_x
            y1 += step_y
        grid[(x1, y1)] += 1

    cnt = 0
    for val in grid.values():
        if val > 1:
            cnt += 1

    print(cnt)


def part2(file):
    lines = parse_lines(file)
    grid = collections.defaultdict(int)
    for line in lines:
        x1,y1,x2,y2 = line

        step_x = sign(x2-x1)
        step_y = sign(y2-y1)

        while x1 != x2 or y1 != y2:
            grid[(x1, y1)] += 1
            x1 += step_x
            y1 += step_y
        grid[(x1, y1)] += 1

    cnt = 0
    for pos, val in grid.items():
        if val > 1:
            cnt += 1

    print(cnt)


part2('input.txt')
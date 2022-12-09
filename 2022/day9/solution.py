from collections import defaultdict, Counter

import functools
import math
import re
import sys


# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            d,n = l.split(' ')
            lines.append((d, int(n)))

        return lines
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines

    # group by newlines
    # return grouped_input(filename, int)


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0


def next(head, tail):
    if head == tail:
        return tail
    dir = (tail[0] - head[0], tail[1] - head[1])
    if abs(dir[0]) > 1 or abs(dir[1]) > 1:
        return (tail[0] - sign(dir[0]), tail[1] - sign(dir[1]))
    return tail


dirs = {
    'U': (0,1),
    'D': (0,-1),
    'L': (-1,0),
    'R': (1,0),
}


def part1(filename):
    input = parse_file(filename)
    head = (0, 0)
    tail = (0, 0)
    visited = {(0,0): True}
    ans = 0

    for dir,steps in input:
        d = dirs[dir]
        for i in range(steps):
            head = (head[0] + d[0], head[1] + d[1])
            tail = next(head, tail)
            print(head, tail)
            visited[tail] = True

    print(f'P1 {filename}: {len(visited)}')


def part2(filename):
    input = parse_file(filename)
    knots = []
    for i in range(10):
        knots.append((0,0))
    visited = {(0,0): True}

    for dir,steps in input:
        d = dirs[dir]
        for i in range(steps):
            knots[0] = (knots[0][0] + d[0], knots[0][1] + d[1])
            for i in range(1, len(knots), 1):
                knots[i] = next(knots[i-1], knots[i])
                # print(head, tail)
            visited[knots[-1]] = True
    print(f'P2 {filename}: {len(visited)}')


# part1('example.txt')
# part1('input.txt')

part2('example2.txt')
part2('input.txt')

from collections import defaultdict, Counter

import copy
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
    with open(filename, 'r') as f:
        return f.read()


def jet(pattern):
    pos = 0
    def push():
        nonlocal pos
        r = pattern[pos]
        pos += 1
        pos %= len(pattern)
        return r
    return push


heights = [1, 3, 3, 4, 2]

def rock():
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)],
        [(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)],
        [(0, 3), (0, 2), (0, 1), (0, 0)],
        [(0, 1), (1, 1), (0, 0), (1, 0)],
    ]
    pos = 0
    def gen():
        nonlocal pos
        r = rocks[pos]
        pos += 1
        pos %= len(rocks)
        return r
    return gen


def collides(r, v, m):
    for coord in r:
        c = vadd(coord, v)
        if m[c] == True or c[0] < 0 or c[0] > 6 or c[1] == 0:
            return True
    return False


def move(r, v):
    s = []
    for coord in r:
        s.append(vadd(coord, v))
    return s

winds = {
    '<': (-1, 0),
    '>': (1, 0)
}
down = (0, -1)


def printm(m, max_y):
    for y in range(max_y, -1, -1):
        for x in range(0, 7):
            if m[(x,y)]:
                if y == 0:
                    print('@', end='')
                else:
                    print('#', end='')
            else:
                print('.', end='')
        print()


def part1(filename):
    input = parse_file(filename)
    wind = jet(input)
    get_rock = rock()
    m = defaultdict(lambda: False)
    for i in range(7):
        m[(i,0)] = True
    max_y = 0

    # print(len(input))

    buf = []
    # initial = []
    # initial_len = len(input) + 5
    # buf_len = len(input) - 5
    needed_tot = len(input) * 5
    buf_len = None
    i = 0
    tot = 0

    # for i in range(2022):
    while buf_len is None or i < buf_len * 3:
        i += 1
        resting = False
        r = get_rock()
        r = move(r, (2, max_y+4))
        falls = 0
        while not resting:
            prev_max_y = max_y
            w = winds[wind()]
            if not collides(r, w, m):
                r = move(r, w)
                # print(f'wind moving {w} {r}')

            if not collides(r, down, m):
                r = move(r, down)
                falls += 1
                # print(f'moving down {r}')
            else:
                resting = True
                for coord in r:
                    max_y = max(max_y, coord[1])
                    m[coord] = True

                    # full = True
                    # for x in range(7):
                    #     if not m[(x,coord[1])]:
                    #         full = False
                    # if full:
                    #     print(f'reset at rock {i} at y {coord[1]}')
        # print(falls)
        # print(max_y)
        # if i <= buf_len:
        if i > 2000:
            tot += falls + 1
        if buf_len is None and tot >= needed_tot:
            print(f'FOUND BUF LEN {tot} {needed_tot} {i - 2000}')
            buf_len = i - 2000
        buf.append(falls)
        # else:
        #     if buf[i%buf_len] != falls - 4:
        #         print(f'ERROR AT {i}')
    # iterations = 1000000000000

    # printm(m, max_y)

    # print(f'MAX OFFSET: {buf_len // 2}')

    for offset in range(buf_len // 2):
        valid = True
        for i in range(buf_len):
            if buf[offset + i] != buf[offset + i + buf_len]:
                valid = False
                break
        if valid:
            print(f'FOUND OFFSET: {offset}')
            break

    initial = buf[:offset]
    buf = buf[offset:buf_len+offset]

    # iterations = 2022
    iterations = 1000000000000
    y = 0
    # for i in range(iterations):
    #     if i % 1000000 == 0:
    #         print(i)
    #     if i < offset:
    #         y += max(0, (4 - initial[i]) + heights[i % 5]-1)
    #     else:
    #         y += max(0, (4 - buf[(i-offset) % buf_len]) + heights[i % 5]-1)

    for i in range(offset):
        y += max(0, (4 - initial[i]) + heights[i % 5]-1)

    iterations -= offset
    final_buf = []
    for i in range(buf_len * 5):
        final_buf.append(max(0, (4 - buf[i % buf_len]) + heights[i % 5]-1))

    y += sum(final_buf) * (iterations // len(final_buf))
    y += sum(final_buf[:iterations % len(final_buf)])

    print(f'FINAL HEIGHT: {y}')
    # too high: 1617506384211

    # print(f'P1 {filename}: {max_y}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
part1('input.txt')

# part2('example.txt')
# part2('input.txt')

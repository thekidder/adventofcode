from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

base = (0, 1, 0, -1)

def digits(n):
    n = str(n)
    for c in n:
        yield int(c)


def base_pattern(base, pos):
    for x in base:
        for _ in range(pos+1):
            yield x


@functools.cache
def pattern(base, pos, l):
    p = [x for x in base_pattern(base, pos)]
    p = p * math.ceil(l / (len(p) - 1))
    return p[1:l+1]


# @functools.cache
def fast_pattern(pos, l, min_i, max_i):
    # print('FAST PATTERN')
    skip = min_i - 1 # account for shift
    if max_i - min_i + 1 > pos:
        print('ERR')
    if pos < skip:
        print('SKIP ERR')
    l = max_i - min_i + 1
    if skip + pos < l:
        print('LEN ERR')
    # print(f'return {skip+1} - {skip+l}')
    # return [x for x in range(skip+1, skip+l+1)]
    for i in range(skip+1, max_i+1):
        yield i


def fft(x, base):
    print(''.join(map(str, x[:8])))
    y = [0] * len(x)
    for iter in range(100):
        for i in range(len(x)):
            r = 0
            for j in pattern(base, i, len(x)):
                r += x[j]
            # for a,b in zip(x, ):
            #     r += a * b
            y[i] = abs(r) % 10
        x = y
        print(''.join(map(str, x[:8])))
    return x


def fast_fft(x, base, min_i, max_i):
    y = [0] * len(x)
    for iter in range(100):
        print(f'iteration {iter}')
        for i in range(min_i, max_i+1):
            # print(f'iteration {iter} char {i}')
            r = 0
            for j in fast_pattern(i, len(x), min_i, max_i):
                r += x[j]
            # for a,b in zip(x, ):
            #     r += a * b
            y[i] = abs(r) % 10
        x = y
        print(''.join(map(str, x[min_i:min_i+80])))
    return x


def part1(filename):
    x = [x for x in digits(file(filename))]
    x = fft(x, base)

    ans = ''.join(map(str, x[:8]))
    print(f'P1 {filename}: {ans}')


def part2(filename):
    x = [x for x in digits(file(filename))] * 10000
    # print(len(x))
    skip = int(''.join(map(str, x[:7])))
    min_i = float('inf')
    max_i = 0
    for i in range(8):
        p = pattern(base, skip+i, len(x))
        n = 0
        for j, c in enumerate(p):
            if c != 0:
                n += 1
                min_i = min(min_i, j)
                max_i = max(max_i, j)
    print(skip, len(p), min_i, max_i, max_i - min_i)
    # print(skip)
    x = fft(x, base, min_i, max_i)

    ans = ''.join(map(str, x[skip:skip+8]))
    print(f'P2 {filename}: {ans}')


part1('example.txt')
# part1('input.txt')

# part2('example.txt')
# part2('input.txt')

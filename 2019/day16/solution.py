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
# def fast_pattern(pos, l, min_i, max_i):
#     # print('FAST PATTERN')
#     skip = min_i - 1 # account for shift
#     if max_i - min_i + 1 > pos:
#         print('ERR')
#     if pos < skip:
#         print('SKIP ERR')
#     l = max_i - min_i + 1
#     if skip + pos < l:
#         print('LEN ERR')
#     # print(f'return {skip+1} - {skip+l}')
#     # return [x for x in range(skip+1, skip+l+1)]
#     for i in range(skip+1, max_i+1):
#         yield i


def fft(x, base):
    print(''.join(map(str, x[:8])))
    y = [0] * len(x)
    for _ in range(100):
        for i in range(len(x)):
            r = 0
            for a,b in zip(x, pattern(base, i, len(x))):
                r += a * b
            y[i] = abs(r) % 10
        x = y
        print(''.join(map(str, x[:8])))
    return x


def part1(filename):
    x = [x for x in digits(file(filename))]
    x = fft(x, base)

    ans = ''.join(map(str, x[:8]))
    print(f'P1 {filename}: {ans}')


def fast_fft(x, base, min_i, max_i):
    y = [0] * len(x)
    for iter in range(100):
        print(f'iteration {iter}')
        for i in range(min_i, max_i+1):
            # print(f'iteration {iter} char {i}')
            r = 0
            for j in fast_pattern(i, len(x), min_i, max_i):
                r += x[j]
            y[i] = abs(r) % 10
        x = y
        print(''.join(map(str, x[min_i:min_i+80])))
    return x


# @functools.cache
def fast_pattern(base, pos, l):
    p = pattern(base, pos, l)
    r = []
    for i,v in enumerate(p):
        if v != 0:
            r.append((i,v))
    return r 


# notes:
# -- only 1s seem to be present in the pattern
def part2(filename):
    # x = [x for x in digits(file(filename))]
    # skip = 0
    x = [x for x in digits(file(filename))] * 10000
    skip = int(''.join(map(str, x[:7])))
    y = x[:]
    dependent_positions = set()
    for i in range(8):
        dependent_positions.add(skip+i)
        p = fast_pattern(base, skip+i, len(x))
        for (j,v) in p:
            dependent_positions.add(j)
    for iter in range(100):
        
        val = ''.join(map(str, x[skip:skip+8]))
        print(f'iteration {iter}: {val}')
        for num,i in enumerate(dependent_positions):
            # print(f'{num}/{len(dependent_positions)}')
            p = fast_pattern(base, i, len(x))
            r = 0
            for (j,v) in p:
                r += v * x[j]
            y[i] = abs(r) % 10
        x = y

    ans = ''.join(map(str, x[skip:skip+8]))
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
# part2('input.txt')

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


def from_digits(l):
    return int(''.join(map(str, l)))


def base_pattern(base, pos):
    for x in base:
        for _ in range(pos+1):
            yield x


@functools.cache
def pattern(base, pos, l):
    p = [x for x in base_pattern(base, pos)]
    p = p * math.ceil(l / (len(p) - 1))
    return p[1:l+1]


def input_digit(digits, pos):
    i = pos % len(digits)
    return digits[i]


def fft(x, base):
    y = [0] * len(x)
    for _ in range(100):
        for i in range(len(x)):
            r = 0
            for a,b in zip(x, pattern(base, i, len(x))):
                r += a * b
            y[i] = abs(r) % 10
        x = y
    return x


def part1(filename):
    x = [x for x in digits(file(filename))]
    x = fft(x, base)

    ans = ''.join(map(str, x[:8]))
    print(f'P1 {filename}: {ans}')


def fast_fft(input, repeat, offset, iterations):
    input_len = repeat * len(input)
    output_len = 8
    scratch = [0] * (input_len - offset)
    for i in range(0, input_len - offset):
        scratch[i] = input_digit(input, i + offset)

    for _ in range(iterations):
        accum = 0
        for p in range(len(scratch) - 1, -1, -1):
            accum += scratch[p]
            scratch[p] = accum % 10
    return from_digits(scratch[:output_len])


def part2(filename):
    input = list(digits(file(filename)))
    offset = from_digits(input[:7])
    print(f'P2 {filename}: {fast_fft(input, 10000, offset, 100)}')


part1('example.txt')
part1('input.txt')

part2('example1.txt')
part2('example2.txt')
part2('example3.txt')
part2('input.txt')

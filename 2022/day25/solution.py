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
    with open(filename, 'r') as f:
        return f.readlines()

def to_decimal_digit(d):
    if d == '2': return 2
    if d == '1': return 1
    if d == '0': return 0
    if d == '-': return -1
    return -2

def to_decimal(snafu):
    s = 0
    for i,digit in enumerate(reversed(snafu.strip())):
        s += pow(5, i) * to_decimal_digit(digit)
    return s


chars = ['=','-','0','1','2']

def dst(s,d): return abs(to_decimal(''.join(s))-d) 

def to_snafu(s):
    n = []
    while to_decimal(''.join(n)) < 2*s:
        n = ['2'] + n
    for i in range(len(n)):
        md = sys.maxsize
        mc = None
        for c in chars:
            n[i] = c
            val = to_decimal(''.join(n))
            print(f'try {c} at {i} for {dst(n, s)} {val}')
            if dst(n, s) < md:
                md = dst(n, s)
                mc = c
        n[i] = mc
        num = ''.join(n)
        print(f'{n} {to_decimal(num)}')
    while to_decimal(''.join(n)) < s:
        for i in range(len(n)-1,-1,-1):
            if n[i] != '2':
                n[i] = chars[chars.index(n[i])+1]
                break
        else:
            n = ['1'] + n
        print(f'fix digit at {i} to {n[i]}')
        for j in range(i+1, len(n)):
            md = sys.maxsize
            mc = None
            for c in chars:
                n[j] = c
                val = to_decimal(''.join(n))
                # print(f'try {c} at {j} for {dst(n, s)} {val}')
                if dst(n, s) < md:
                    md = dst(n, s)
                    mc = c
            n[j] = mc
            num = ''.join(n)
            print(f'{n} {to_decimal(num)}')
        
    return ''.join(n)
        

def part1(filename):
    input = parse_file(filename)
    ans = sum(map(to_decimal, input))
    print(f'P1 {filename}: {ans} {to_snafu(ans)}')



part1('example.txt') # 4890 2=-1=0
part1('input.txt')

# part2('example.txt')
# part2('input.txt')

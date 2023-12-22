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
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')

        return r
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def step(input, mx,my,locs):
    n = set()
    nm = set()
    for l in locs:
        for d in dirs.values():
            c = vadd(d, l)
            c_m = (c[0] % (mx+1), c[1] % (my+1))
            if input[c_m] == '.':
                n.add(c)
                nm.add(c_m)
    return n,nm


def nlines(m):
    miny = float('inf')
    maxy = 0
    for c in m:
        miny = min(miny, c[1])
        maxy = max(maxy, c[1])
    return maxy-miny+1


def grange(m):
    miny = float('inf')
    maxy = 0
    for c in m:
        miny = min(miny, c[1])
        maxy = max(maxy, c[1])
    return miny, maxy


def part1(filename):
    input,mx,my = parse_grid(filename)
    for c,v in input.items():
        if v == 'S':
            start = c
            break
    input[start] = '.'
    # print_grid(input,mx,my)
    # print(start)

    locs = set([start])
    last = 0
    dlast = 0
    lines = 0

    converged = False
    last_len = 0

    fngs = {}
    cycle_len = 0
    totals = []
    patterns = []
    fill_ratios = []
    

    for iter in range(20):
        locs, locs_m = step(input, mx,my,locs)
        curr = len(locs)
        dcurr = curr-last
        if len(locs_m) == last_len:
            converged = True
        last_len = len(locs_m)

        if converged:
            rows = []
            mi,ma = grange(locs)
            for _,y in enumerate(range(mi,ma+1)):
                cnt = len(list(filter(lambda c:c[1] == y, locs)))
                # print(f'{y},{iter}: {cnt}')
                rows.append(cnt)
            fng = tuple(rows[:6])
            # print(fng)

            if cycle_len == 0 and fng in fngs:
                cycle_len = iter-fngs[fng]
                print(f'{iter}: saw fingerprint at {fngs[fng]}; cycle {cycle_len}')
            fngs[fng] = iter

        if cycle_len != 0 and len(totals) < cycle_len*4:
            fill_ratios.append(((len(locs)/(iter*2+1)**2+1)/2, len(locs), ((iter*2+1)**2+1)//2))
            totals.append(tuple(rows))
            pattern = []
            for i in range(cycle_len*2):
                p = ''
                for j in range(cycle_len*2):
                    y = -cycle_len + i + my // 2
                    x = -cycle_len + j + mx // 2
                    if (x,y) in locs:
                        p +='#'
                    else:
                        p += '.'
                pattern.append(p)

            patterns.append(pattern)

        print_grid(locs, start)
        print()
        # if cycle_len != 0 and len(totals) == cycle_len*4:
        #     for f in fill_ratios:
        #         print(f)
            # for t in patterns:
            #     for p in t:
            #         print(p)
            #     print()
            # break

        # if True:#cycle_len != 0: #and iter% cycle_len == 0:
        #     print(iter+1)
        #     print_grid(locs)
            # print(len(rows))
            # j = (ma - mi+1)//2
            # y = mi + j
            # # for j,y in enumerate(range(mi,ma+1)):
            # cnt = len(list(filter(lambda c:c[1] == y, locs)))
            # print(f'{y},{j}: {cnt}')

        #     print(f'step {iter}: {curr} {len(locs_m)} {nlines(locs)} (+{dcurr}) (+{dcurr-dlast}) [{dcurr-nlines(locs)}]')
            # print(fng)
        last = curr
        dlast = dcurr

    ans = len(locs)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input,mx,my = parse_grid(filename)
    for c,v in input.items():
        if v == 'S':
            start = c
            break
    input[start] = '.'
    # print_grid(input,mx,my)
    # print(start)

    locs = set([start])
    
    for i in range(33):
        locs, locs_m = step(input, mx,my,locs)
        print_grid(locs)
        print()
    ans = 0
    print(f'P2 {filename}: {ans}')


part1('example.txt')
# part1('input.txt')

# part2('example.txt')
# part2('input.txt')

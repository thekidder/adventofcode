from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
pattern = re.compile('(\w) (\d+) \(\#([\w\d]+)\)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            m = pattern.match(line)
            lines.append((m.group(1), int(m.group(2)), m.group(3)))

    return lines


def flood_fill(pit, coord):
    closed = set()
    q = [coord]
    while len(q) > 0:
        coord = q.pop()
        for d in neighbors(coord):
            if d not in closed and (d not in pit or pit[d] != '#'):
                pit[d] = '#'
                closed.add(d)
                q.append(d)


def part1(filename):
    input = parse_file(filename)
    # print(input)
    pit = {}
    coord = (0,0)
    pit[coord] = '#'
    for i in input:
        for j in range(i[1]):
            coord = vadd(coord, dirs[i[0]])
            pit[coord] = '#'

    mx = 0
    my = 0
    minx = float('inf')
    miny = float('inf')
    for c in pit.keys():
        mx = max(mx, c[0])
        minx = min(minx, c[0])
        my = max(my, c[1])
        miny = min(miny, c[1])

    center = vsub((mx, my), (minx, miny))
    center = vmul(center, (0.5, 0.5))
    center = (math.floor(center[0]), math.floor(center[1]))
    flood_fill(pit, center)
    print_grid(pit, minx, miny, mx, my)

    ans = 0
    for c in pit.values():
        if c == '#':
            ans += 1

    print(f'P1 {filename}: {ans}')


dirl = ['R', 'D', 'L', 'U']

def is_inside(edges, p):
    cnt = 0
    for e in edges:
        if e[0] <= p[0] and e[1] >= p[0] and e[2] < p[1]:
            cnt += 1
    return cnt % 2 == 1

offsets = [
    (-.5, -.5),
    (.5, -.5),
    (.5, .5),
    (-.5, .5),
]


def part2(filename):
    input = parse_file(filename)

    coord = (0.0,0.0)
    coords = [coord]

    horz_edges = []
    for i in input:
        dist = int(i[2][:5], 16)
        dir = dirl[int(i[2][5])]
        ncoord = vadd(coord, vmul(dirs[dir], (dist, dist)))
        coords.append(ncoord)
        if coord[1] == ncoord[1]:
            e = sorted([coord[0],ncoord[0]])
            horz_edges.append((e[0],e[1],ncoord[1]))
        coord = ncoord

    expanded_coords = []
    for c in coords:
        inside = list(map(lambda o: is_inside(horz_edges, vadd(c, o)), offsets))
        # print(c,inside)
        if len(list(filter(None, inside))) == 3:
            expanded_coords.append(vadd(c, offsets[inside.index(False)]))
        else:
            for i in range(4):
                if not inside[i] and not inside[(i+1)%4] and not inside[(i-1)%4]:
                    expanded_coords.append(vadd(c, offsets[i]))
                    break
        # print(expanded_coords)

    # print(expanded_coords)

    horz_edges = []
    xs = set()
    ys = set()
    last_coord = expanded_coords[-1]

    for c in expanded_coords:
        if c[1] == last_coord[1]:
            e = sorted([last_coord[0],c[0]])
            horz_edges.append((e[0],e[1],c[1]))
        xs.add(c[0])
        ys.add(c[1])
        last_coord = c

    xs = sorted(xs)
    ys = sorted(ys)
    print(horz_edges)
    print(xs,ys)

    ans = 0
    for xmin,xmax in zip(xs[:-1], xs[1:]):
        for ymin,ymax in zip(ys[:-1], ys[1:]):
            inside = is_inside(horz_edges, (xmax-0.5, ymax-0.5))
            # print(f'({xmin},{ymin}) -> ({xmax},{ymax}) :: {inside}')
            if inside:
                ans += (xmax - xmin) * (ymax - ymin)

    print(f'P2 {filename}: {int(ans)}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

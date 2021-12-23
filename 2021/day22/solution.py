from collections import defaultdict, Counter

import re
import functools
import math
import sys

# regex example
pattern = re.compile('(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            m = pattern.match(line)
            state = 1 if m.group(1) == 'on' else 0
            lines.append((state, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)), int(m.group(7))))

    return lines


def part1(filename):
    cubes = defaultdict(int)
    input = parse_file(filename)
    for line in input:
        state, xmin,xmax,ymin,ymax,zmin,zmax = line
        xmin = max(-50, xmin)
        xmax = min(50, xmax)
        ymin = max(-50, ymin)
        ymax = min(50, ymax)
        zmin = max(-50, zmin)
        zmax = min(50, zmax)
        for x in range(xmin,xmax+1):
            for y in range(ymin,ymax+1):
                for z in range(zmin,zmax+1):
                    cubes[(x,y,z)] = state

    ans = functools.reduce(lambda x, y: x+y, cubes.values(), 0)
    print(f'ANSWER: {ans}')


def uniq(l, r2):
    r = [list(l)]
    # returns [ranges only in r1]

    out = []

    dimens = 3
    for dimen in range(dimens):
        next = []
        for i in range(len(r)):
            r1 = r[i]
            if r2[0+dimen*2] <= r1[0+dimen*2] and r2[1+dimen*2] >= r1[1+dimen*2]:
                next.append(r1[:])
            elif r2[0+dimen*2] > r1[0+dimen*2] and r2[1+dimen*2] < r1[1+dimen*2]:
                n = r1[:]
                n[0+dimen*2] = r2[1+dimen*2]+1
                out.append(n)

                n = r1[:]
                n[0+dimen*2] = r2[0+dimen*2]
                n[1+dimen*2] = r2[1+dimen*2]
                next.append(n)

                n = r1[:]
                n[1+dimen*2] = r2[0+dimen*2]-1
                out.append(n)

            elif r2[0+dimen*2] <= r1[0+dimen*2] and r2[1+dimen*2] >= r1[0+dimen*2]:
                n = r1[:]
                n[0+dimen*2] = r2[1+dimen*2]+1
                out.append(n)

                n = r1[:]
                n[1+dimen*2] = r2[1+dimen*2]
                next.append(n)
            elif r2[0+dimen*2] <= r1[1+dimen*2] and r2[1+dimen*2] >= r1[1+dimen*2]:
                n = r1[:]
                n[1+dimen*2] = r2[0+dimen*2]-1
                out.append(n)

                n = r1[:]
                n[0+dimen*2] = r2[0+dimen*2]
                next.append(n)
            else:
                # no overlap at all!
                out.append(list(r1))
        r = next 
    
    # out.extend(r)

    return map(tuple, out)
    

def part2(filename):
    cubes = set()
    input = parse_file(filename)
    for i,line in enumerate(input):
        state, xmin,xmax,ymin,ymax,zmin,zmax = line
        r2 = (xmin,xmax,ymin,ymax,zmin,zmax)
        next = set(cubes)
        for r1 in cubes:
            if state > 0:
                next.remove(r1)
                for x in uniq(r1, r2):
                    next.add(x)
            else:
                next.remove(r1)
                for x in uniq(r1, r2):
                    next.add(x)

        if state > 0:
            next.add(r2)

        cubes = next
        print(len(cubes))
        # print(f'{line} ::: {cubes}')

    ans = 0
    for r in cubes:
        x = r[1] - r[0] + 1
        y = r[3] - r[2] + 1
        z = r[5] - r[4] + 1
        ans += (x*y*z)

    print(ans)

# print([x for x in uniq((-5,5,-5,5),(3,6,3,6))])

part2('input.txt')

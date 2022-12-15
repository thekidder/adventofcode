from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

# regex example
pattern = re.compile('x=([0-9\-]+), y=([\-0-9]+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    sensors = []
    beacons = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            s, b = line.split(':')
            sm = pattern.search(s)
            bm = pattern.search(b)
            sensors.append((int(sm.group(1)),int(sm.group(2))))
            beacons.append((int(bm.group(1)),int(bm.group(2))))

        return sensors,beacons
    # lines = []
    # with open(filename, 'r') as f:
    #     for line in f:
    #         lines.append(int(line))

    # return lines


def dist(s, b):
    return sum(map(abs, vsub(s, b)))


def part1(filename, y):
    sensors,beacons = parse_file(filename)
    occ = {}
    closest = {}
    for sensor in sensors:
        for beacon in beacons:
            if sensor not in closest or dist(sensor, beacon) < dist(sensor, closest[sensor]):
                closest[sensor] = beacon

    for sensor in sensors:
        r = dist(sensor, closest[sensor])
        d = abs(sensor[1] - y)
        if d > r:
            continue
        r -= d
        for i in range(sensor[0] - r, sensor[0] + r):
            occ[i] = True

    print(f'P1 {filename}: {len(occ)}')


def candidates(sensor, closest):
    r = dist(sensor, closest[sensor])
    for i in range(sensor[1]-r-1, sensor[1]+r+2):
        if i == sensor[1]-r-1:
            yield (sensor[0], i)
        elif i == sensor[1]+r+1:
            yield (sensor[0], i)
        else:
            d = (r - abs(i - sensor[1]))+1
            yield (sensor[0]-d, i)
            yield (sensor[0]+d, i)


def find_clear_size(sensors, dists, size):

def part2(filename, size):
    sensors,beacons = parse_file(filename)
    closest = {}
    dists = {}
    for sensor in sensors:
        for beacon in beacons:
            if sensor not in closest or dist(sensor, beacon) < dist(sensor, closest[sensor]):
                closest[sensor] = beacon
                dists[sensor] = dist(sensor, beacon)

    for sensor in sensors:
        print(sensor)
        for c in candidates(sensor, closest):
            if c[0] < 0 or c[0] > size or c[1] < 0 or c[1] > size:
                continue
            v = True
            for o in sensors:
                if dist(c, o) <= dist(o, closest[o]):
                    v = False
                    break
            if v:
                print(c,c[0]*4000000+c[1])
    # occ = {}
    # for sensor in sensors:
    #     r = dist(sensor, closest[sensor])
    #     for i in range(sensor[0]-r, sensor[0]+r+1):
    #         for j in range(sensor[1]-r, sensor[1]+r+1):
    #             if dist((i,j), sensor) <= r:
    #                 occ[(i,j)] = True



    # for row in range(size+1):
    #     if row % 10000 == 0:
    #         print(row)
    #     occ = {}
    #     for sensor in sensors:
    #         r = dist(sensor, closest[sensor])
    #         d = abs(sensor[1] - row)
    #         if d > r:
    #             continue
    #         r -= d
    #         for i in range(sensor[0] - r, sensor[0] + r + 1):
    #             occ[i] = True
    #     for col in range(size+1):
    #         # print('#' if col in occ else '.', end='')
    #         if col not in occ:
    #             ans.append(col*4000000+row)
    #             # print(col, row, col*4000000+row)
    #     # print('')
    # print(ans)


# part1('example.txt', 10)
# part1('input.txt', 2000000)

# part2('example.txt', 20)
part2('input.txt', 4000000)

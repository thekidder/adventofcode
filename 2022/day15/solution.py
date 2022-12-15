import re

from helpers import *

pattern = re.compile('x=([0-9\-]+), y=([\-0-9]+)')

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


def dist(s, b):
    return sum(map(abs, vsub(s, b)))


def build_dists(sensors, beacons):
    dists = {}
    for sensor, beacon in zip(sensors, beacons):
        dists[sensor] = dist(sensor, beacon)
    return dists


def part1(filename, y):
    sensors,beacons = parse_file(filename)
    dists = build_dists(sensors, beacons)
    occ = {}
    for sensor in sensors:
        r = dists[sensor]
        d = abs(sensor[1] - y)
        if d > r:
            continue
        r = r - d
        for i in range(sensor[0] - r, sensor[0] + r + 1):
            if (i,y) not in beacons:
                occ[i] = True

    print(f'P1 {filename}: {len(occ)}')


def candidates(sensor, dists):
    r = dists[sensor]
    yield (sensor[0], sensor[1]-r-1)
    yield (sensor[0], sensor[1]+r+1)
    for i in range(sensor[1]-r, sensor[1]+r+1):
        d = r - abs(i - sensor[1]) + 1
        yield (sensor[0]-d, i)
        yield (sensor[0]+d, i)


def find_clear_space(sensors, dists, size):
    for sensor in sensors:
        for c in candidates(sensor, dists):
            if c[0] < 0 or c[0] > size or c[1] < 0 or c[1] > size:
                continue
            v = True
            for o in sensors:
                if dist(c, o) <= dists[o]:
                    v = False
                    break
            if v:
                return c


def part2(filename, size):
    sensors,beacons = parse_file(filename)
    dists = build_dists(sensors, beacons)
    ans = find_clear_space(sensors, dists, size)
    print(f'P2 {filename}: {ans[0]*4000000+ans[1]}')


# part1('example.txt', 10)
# part1('input.txt', 2000000)

part2('example.txt', 20)
part2('input.txt', 4000000)

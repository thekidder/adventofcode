from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

def parse(c):
    m = defaultdict(bool)
    for y, line in enumerate(c.split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                m[(x,y)] = True
    return m,x,y



def parse_file(filename):
    with open(filename, 'r') as f:
        return parse(f.read())


def calc_visibility(m, xo, yo, xs, ys):

    vis = 0

    for x in range(xs+1):
        for y in range(ys+1):
            if x == xo and yo == y:
                continue
            if not m[(x,y)]:
                continue
            slope = vsub((x,y), (xo,yo))
            if slope[0] == 0:
                slope = (0, sign(slope[1]))
            elif slope[1] == 0:
                slope = (sign(slope[0]), 0)
            else:
                g = math.gcd(*slope)
                slope = (slope[0] // g, slope[1] // g)
            cand = (x,y)
            found_interrupt = False
            while cand != (xo, yo) and not found_interrupt:
                cand = vsub(cand, slope)
                if cand != (xo,yo) and m[cand]:
                    found_interrupt = True
            if not found_interrupt:
                vis += 1
    return vis


def station_pos(input):
    max_visibility = 0
    max_visibility_at = (0,0)
    m, xs, ys = input
    for x in range(xs+1):
        for y in range(ys+1):
            if m[(x,y)]:
                v = calc_visibility(m, x, y, xs, ys)
                if v > max_visibility:
                    max_visibility = v
                    max_visibility_at = (x,y)
    return max_visibility, max_visibility_at


def part1(input):
    max_visibility, max_visibility_at = station_pos(input)
    print(f'P1 {max_visibility} at {max_visibility_at}')


def part2(input):
    _, max_visibility_at = station_pos(input)
    m, xs, ys = input

    asteroids = []
    # max_visibility_at = (8,3)
    print(f'station at: {max_visibility_at}')

    for x in range(xs+1):
        for y in range(ys+1):
            if m[(x,y)] and (x,y) != max_visibility_at:
                d = dist_sqr((x,y), max_visibility_at)
                s = vsub((x,y), max_visibility_at)
                angle = math.atan2(s[1], s[0]) + math.pi / 2
                if angle < 0:
                    angle = angle + 2*math.pi
                asteroids.append((angle, d, (x,y)))
    asteroids.sort()
    last_asteroid = None
    n = 0
    while len(asteroids) > 0:
        for i, a in enumerate(asteroids):
            if last_asteroid is None or a[0] > last_asteroid:
                a = asteroids.pop(i)
                n += 1
                if n == 200:
                    print(f'P2: {a[2][0]*100+a[2][1]} {a[2]} {len(asteroids)}')
                    return
                last_asteroid = a[0]
                break
        else:
            last_asteroid = None
        

# part1(parse('''.#..#
# .....
# #####
# ....#
# ...##'''))
# part2(parse('''.#....#####...#..
# ##...##.#####..##
# ##...#...#.#####.
# ..#.....X...###..
# ..#.#.....#....##
# '''))
part2(parse('''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''))
part2(parse('''#..#....#...#.#..#.......##.#.####
#......#..#.#..####.....#..#...##.
.##.......#..#.#....#.#..#.#....#.
###..#.....###.#....##.....#...#..
...#.##..#.###.......#....#....###
.####...##...........##..#..#.##..
..#...#.#.#.###....#.#...##.....#.
......#.....#..#...##.#..##.#..###
...###.#....#..##.#.#.#....#...###
..#.###.####..###.#.##..#.##.###..
...##...#.#..##.#............##.##
....#.##.##.##..#......##.........
.#..#.#..#.##......##...#.#.#...##
.##.....#.#.##...#.#.#...#..###...
#.#.#..##......#...#...#.......#..
#.......#..#####.###.#..#..#.#.#..
.#......##......##...#..#..#..###.
#.#...#..#....##.#....#.##.#....#.
....#..#....##..#...##..#..#.#.##.
#.#.#.#.##.#.#..###.......#....###
...#.#..##....###.####.#..#.#..#..
#....##..#...##.#.#.........##.#..
.#....#.#...#.#.........#..#......
...#..###...#...#.#.#...#.#..##.##
.####.##.#..#.#.#.#...#.##......#.
.##....##..#.#.#.......#.....####.
#.##.##....#...#..#.#..###..#.###.
...###.#..#.....#.#.#.#....#....#.
......#...#.........##....#....##.
.....#.....#..#.##.#.###.#..##....
.#.....#.#.....#####.....##..#....
.####.##...#.......####..#....##..
.#.#.......#......#.##..##.#.#..##
......##.....##...##.##...##......'''))

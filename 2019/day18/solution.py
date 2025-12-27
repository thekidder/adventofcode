from collections import defaultdict, Counter

import copy
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


def parse(input):
    return input.split('\n')


def get_keys(map, pos, existing_keys, steps):
    visited = set([pos])
    next = [(steps, pos)]

    keys = []

    while len(next):
        steps, coord = next.pop(0)
        for n in cardinal_neighbors(coord):
            if n not in map:
                continue
            if map[n] == '#':
                continue
            if map[n] >= 'a' and map[n] <= 'z' and map[n] not in existing_keys:
                visited.add(n)
                keys.append((steps+1, n))
                continue
            elif map[n] >= 'A' and map[n] <= 'Z' and map[n].lower() not in existing_keys:
                continue
            if n not in visited:
                visited.add(n)
                next.append((steps+1, n))
    next_states = {}
    for k in keys:
        new_key = map[k[1]]
        next_states[(k[1], tuple(existing_keys | set([new_key])))] = k[0]
    return next_states


def part1(data):
    input,sx,sy = parse_grid(data)
    start = None
    keys = set()
    num_keys = 0
    for coord, v in input.items():
        if v == '@':
            start = coord
        elif v >= 'a' and v <= 'z':
            num_keys += 1
    input[start] = '.'

    # (pos, keys) : steps
    states = { (start, tuple(keys)) : 0}
    best = 9999999

    i = 0
    while len(states):
        if i % 10 == 1:
            print(f'iteration {i}: {len(states)} states')
        next_states = {}
        for state, steps in states.items():
            n = get_keys(input, state[0], set(state[1]), steps)
            for k,v in n.items():
                if k not in next_states or next_states[k] > v:
                    next_states[k] = v
        states_at_goal = [v for k,v in next_states.items() if len(k[1]) == num_keys]
        if len(states_at_goal) > 0:
            best = min(best, min(states_at_goal))
        states = next_states
        i += 1

    return best


def update_robot(robots, i, new_robot):
    robots = list(robots)
    robots[i] = new_robot
    return tuple(robots)


def part2(data):
    input,sx,sy = parse_grid(data)
    robots = []
    keys = set()
    num_keys = 0
    for coord, v in input.items():
        if v == '@':
            robots.append(coord)
        elif v >= 'a' and v <= 'z':
            num_keys += 1
    for p in robots:
        input[p] = '.'

    # (robot_positions, keys) : steps
    states = { (tuple(robots), tuple(keys)) : 0}
    best = 9999999

    iterations = 0
    while len(states):
        if iterations % 10 == 0:
            example_key = next(iter(states))
            print(f'iteration {iterations}: {len(states)} states; {example_key}: {states[example_key]}')
        next_states = {}
        for state, steps in states.items():
            for i,robot in enumerate(state[0]):
                n = get_keys(input, robot, set(state[1]), steps)
                for k,v in n.items():
                    robots = update_robot(state[0], i, k[0])
                    next_key = (robots, k[1])
                    if next_key not in next_states or v < next_states[next_key]:
                        next_states[next_key] = v
        states_at_goal = [v for k,v in next_states.items() if len(k[1]) == num_keys]
        if len(states_at_goal) > 0:
            best = min(best, min(states_at_goal))
        states = next_states
        iterations += 1

    return best


map1 = '''
#########
#b.A.@.a#
#########'''


map2 = '''
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

map3 = '''
########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''

map4 = '''
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''

map5 = '''
########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################'''

map6 = '''
#######
#a.#Cd#
##@#@##
#######
##@#@##
#cB#Ab#
#######'''

map7 = '''
###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############'''

map8 = '''
#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############'''

check(part1, map1, 8)
check(part1, map2, 86)
check(part1, map3, 132)
check(part1, map5, 81)
check(part1, map4, 136)
exec(part1, 'input.txt')

check(part2, map6, 8)
check(part2, map7, 24)
check(part2, map8, 32)
exec(part2, 'input2.txt')

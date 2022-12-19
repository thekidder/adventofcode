from collections import defaultdict

import copy
import re

pattern = re.compile('Each (\w+) robot costs ([\d\w\s]+)\.')

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            blueprint = {}
            for m in re.finditer(pattern, line):
                resource = m.group(1)
                reqs = m.group(2).split('and')
                rr = []
                for req in reqs:
                    amt, t = req.strip().split(' ')
                    amt = int(amt)
                    t = t.strip()
                    rr.append((amt, t))
                blueprint[resource] = rr
            r.append(blueprint)

        return r


def can_build(blueprint, robot, resources):
    reqs = blueprint[robot]
    return all(map(lambda r: resources[r[1]] >= r[0], reqs))


def max_est(robot, resources, t, max_t):
    geodebots = robot['geode']
    geodes = resources['geode']
    for _ in range(t, max_t):
        geodes += geodebots
        geodebots += 1
    return geodes


all_resources = ['clay', 'ore', 'obsidian', 'geode']

def clone(blueprint, resources, robots, t):
    if can_build(blueprint, 'geode', resources):
        return [((resources, robots, t, 'geode'))]
    if can_build(blueprint, 'obsidian', resources):
        return [((resources, robots, t, 'obsidian'))]
    res = []
    for r in all_resources:
        if any(map(lambda x: robots[x[1]] < 1, blueprint[r])):
            continue
        nrobots = copy.deepcopy(robots)
        nresources = copy.deepcopy(resources)
        res.append((nresources, nrobots, t, r))
    return res


def most_geodes(blueprint, mins):
    resources = defaultdict(int)
    robots = defaultdict(int)
    robots['ore'] = 1

    worlds = clone(blueprint, resources, robots, 0)
    max_geodes = 0

    while len(worlds):
        resources, robots, t, next_robot = worlds.pop(-1)
        if t == mins:
            continue

        me = max_est(robots, resources, t, mins)
        if me < max_geodes:
            continue

        should_b = can_build(blueprint, next_robot, resources)

        for r,n in robots.items():
            resources[r] += n

        max_geodes = max(max_geodes, resources['geode'])
        nrobots = copy.deepcopy(robots)
        nresources = copy.deepcopy(resources)
        if should_b:
            for amt,robottype in blueprint[next_robot]:
                nresources[robottype] -= amt
            nrobots[next_robot] += 1
            worlds.extend(clone(blueprint, nresources, nrobots, t+1))
        else:
            worlds.append((nresources, nrobots, t+1, next_robot))

    return max_geodes


def solve(blueprints, time):
    quality = 0
    score = 1
    for i, bp in enumerate(blueprints):
        s = most_geodes(bp, time)
        quality += s * (i+1)
        score *= s
        print(f'calc {i+1} as {s} ({quality}, {score})...')
    print(f'solve: {quality}, {score}')

ex = parse_file('example.txt')
input = parse_file('input.txt')


# solve(ex, 24)
# solve(input, 24)

# solve(ex, 32)
solve(input[:3], 32)

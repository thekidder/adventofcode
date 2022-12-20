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


def can_build(blueprint, robot, state):
    reqs = blueprint[robot]
    return all(map(lambda r: state[indices[r[1]]] >= r[0], reqs))


def max_est(state, max_t):
    geodebots = state[indices['geode']+4]
    geodes = state[indices['geode']]
    t = state[8]
    for _ in range(t, max_t):
        geodes += geodebots
        geodebots += 1
    return geodes


def max_cost_of(blueprint, resource):
    m = 0
    for reqs in blueprint.values():
        for amt,req in reqs:
            if req == resource:
                m = max(amt, m)
    return m

all_resources = ['clay', 'ore', 'obsidian', 'geode']
indices = {x:i for i,x in enumerate(all_resources)}

def branch_states(blueprint, state):
    if can_build(blueprint, 'geode', state[:4]):
        return [state[:9] + ['geode',]]
    if can_build(blueprint, 'obsidian', state[:4]):
        return [state[:9] + ['obsidian',]]
    res = []

    robots = state[4:8]
    for r in all_resources:
        # don't try to build robots if have no robots building its dependencies
        if any(map(lambda x: robots[indices[x[1]]] < 1, blueprint[r])):
            continue
        # don't build robots if we're already producing enough
        if r != 'geode' and state[indices[r]+4] > max_cost_of(blueprint, r):
            continue
                
        next_state = state[:8]
        res.append(next_state + [state[8], r])
    return res


def most_geodes(blueprint, mins):
    # world state is represented as a single flat list with:
    # num resources, num robots, time, next robot index to build

    worlds = branch_states(blueprint, [0,0,0,0, 0,1,0,0, 0])
    max_geodes = 0

    while len(worlds):
        state = worlds.pop(-1)

        t = state[8]
        next_robot = state[9]

        if t == mins:
            continue

        me = max_est(state, mins)
        if me < max_geodes:
            continue

        should_build = can_build(blueprint, next_robot, state)

        for i in range(4):
            state[i] += state[i+4]

        max_geodes = max(max_geodes, state[indices['geode']])
        

        if should_build:
            for amt,robottype in blueprint[next_robot]:
                state[indices[robottype]] -= amt
            state[indices[next_robot]+4] += 1
            worlds.extend(branch_states(blueprint, state[:8] + [t+1,]))
        else:
            worlds.append(state[:8] + [t+1,next_robot])

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

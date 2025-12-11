from collections import defaultdict, Counter

import copy
import functools
import itertools
import math
import re
import sys
from multiprocessing import Pool
from functools import partial
from helpers import *

# regex example
pattern = re.compile('\[([\.\#]+)\] ([\d,\(\) ]+) \{([\d,]+)\}')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        for line in f:
            m = pattern.match(line)
            end_state = tuple(m.group(1))
            buttons = [mapl(int, x[1:-1].split(',')) for x in m.group(2).split(' ')]
            joltage = tuple(map(int, m.group(3).split(',')))
            r.append((end_state, buttons, joltage))

    return r


def est(_, start, end):
    return 100
    # cost = 0
    # for i, c in enumerate(start):
    #     if c != end[i]:
    #         cost += 1
    # return cost


def gen(buttons, cost, state, _):
    for button in buttons:
        n_state = list(state)
        for l in button:
            n_state[l] = '#' if n_state[l] == '.' else '.'
        # print(f'yield {n_state} from {state} with {button}')
        yield (cost+1, tuple(n_state))


def fewest_presses(machine):
    end_state, buttons, _ = machine
    state = tuple('.' * len(end_state))

    print(state, end_state)

    cost, _ = a_star(buttons, state, end_state, gen, est)
    return cost


def part1(filename):
    machines = parse_file(filename)
    ans = functools.reduce(operator.add, map(fewest_presses, machines))
    print(f'P1 {filename}: {ans}')


# @functools.cache
def reduce_equations(equations, constraints, button, val):
    equations = [[x[0], set(x[1])] for x in equations]
    constraints = list(constraints)
    reductions = {button: val}
    while len(reductions):
        # print(constraints, equations)
        button, val = reductions.popitem()
        if val < constraints[button][0] or val > constraints[button][1]:
            # print(f'reducing button {button} to {val} violated constraint {constraints[button]}')
            return False, None, None
        constraints[button] = (val,val)
        for i in range(len(equations)):
            if button in equations[i][1]:
                equations[i][0] -= val
                if equations[i][0] < 0:
                    return False, None, None
                equations[i][1].remove(button)
                if len(equations[i][1]) == 1:
                    b = next(iter(equations[i][1]))
                    reductions[b] = equations[i][0]
                    # equations[i][0] = 0
    if not all(map(lambda x: x[0]==0 or len(x[1]) > 0, equations)):
        return False, None, None
    return True, [(x[0], tuple(x[1])) for x in equations], constraints


# iterations = 0

# @functools.cache
def process(constraints, equations, button, i, best):
    # print(f'trying {button} -> {i}: current progress {len(equations)}: {equations}, {constraints}')
    # if iterations % 1000 == 0:
    #     print(f'{iterations} trying {button} -> {i}: current progress {len(equations)}: {equations}, {constraints}')

    # iterations += 1
    # print(f'set button {button} to {i}')
    # nconstraints = copy.deepcopy(constraints)
    # nequations = copy.deepcopy(equations)
    success, nequations, nconstraints = reduce_equations(equations, constraints, button, i)
    if not success:
        # print(f'contradiction {button} {i} {constraints}')
        return 999999
    # print(f'no contradiction {button} {i} {constraints}')
    # nequations = list(filter(lambda x: len(x[1])>0, nequations))
    return solve(nequations, nconstraints, best, None)


def solve(equations, constraints, best, pool=None, root=False):
    if all(map(lambda x: len(x[1])==0, equations)):
        if any(map(lambda x: x[0] > 0, equations)):
            # print(f'{indent}no resolve')
            return 999
        if any(map(lambda x: x[1] - x[0] > 0, constraints)):
            # print(f'{indent}not done')
            return 99999
        # print(f'END: {sum(map(lambda x: x[0], constraints))} {constraints}, {equations}')
        return sum(map(lambda x: x[0], constraints))

    min_presses = sum(map(lambda x: x[0], constraints))
    if min_presses > best:
        # print(f'{indent}too big {best}')
        return best

    equations.sort(key=lambda x: len(x[1]))
    # button = next(iter(equations[0][1]))
    # print(equations)

    for button in range(len(constraints)):
        if constraints[button][1] - constraints[button][0] == 0:
            continue
        for i in range(constraints[button][0], constraints[button][1]+1):
            best = min(process(tuple(constraints), tuple(equations), copy.copy(button), copy.copy(i), best), best)
            if root:
                print(f'best after {button},{i} is {best}')
    # if pool:
    #     pool.close()
    #     pool.join()
    # for a in answers:
    #     print(f'{indent}GOT {a()}')
    
    # print(f'{indent}found {best}')
    return best


def machine_cost_p2(machine):
    _, buttons, end_joltage = machine

    buttons_per_joltage = [set() for _ in end_joltage]
    for i, b in enumerate(buttons):
        for j in b:
            buttons_per_joltage[j].add(i)

    buttons_per_joltage = [tuple(x) for x in buttons_per_joltage]
    equations = [(end_joltage[i], buttons_per_joltage[i]) for i in range(len(end_joltage))]
    constraints = []
    for button in range(len(buttons)):
        constraints.append((0, min([x[0] for x in equations if button in x[1]])))
    
    pool = None
    # with Pool(8) as pool:
    sol = solve(equations, constraints, 99999, pool, True)
    print(f'SOLUTION {sol}')
    return sol


def part2(filename):
    machines = parse_file(filename)
    ans = functools.reduce(operator.add, map(machine_cost_p2, machines))
    print(f'P2 {filename}: {ans}')


if __name__ == '__main__':
    # part1('example.txt')
    # part1('input.txt')

    # part2('example.txt')
    part2('input.txt')
# 
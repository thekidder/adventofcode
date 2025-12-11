import functools
import operator
from z3 import *
import re

pattern = re.compile('\[([\.\#]+)\] ([\d,\(\) ]+) \{([\d,]+)\}')


def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        for line in f:
            m = pattern.match(line)
            end_state = tuple(m.group(1))
            buttons = [list(map(int, x[1:-1].split(','))) for x in m.group(2).split(' ')]
            joltage = tuple(map(int, m.group(3).split(',')))
            r.append((end_state, buttons, joltage))

    return r


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
    button_syms = [Int('B'+str(x)) for x in range(len(buttons))]
    s = Optimize()
    for i, x in enumerate(constraints):
        s.add(button_syms[i] <= x[1])
        s.add(button_syms[i] >= 0)

    for joltage, buttons in equations:
        s.add(Sum([button_syms[x] for x in buttons]) == joltage)

    s.minimize(Sum(button_syms))
    
    if s.check() == sat:
        m = s.model()
        return m.eval(Sum(button_syms)).as_long()


def solve(filename):
    machines = parse_file(filename)
    ans = functools.reduce(operator.add, map(machine_cost_p2, machines))
    print(f'P2 {filename}: {ans}')


solve('input.txt')
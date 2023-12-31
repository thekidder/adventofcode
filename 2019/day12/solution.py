import itertools
import math
import re

from copy import deepcopy
from helpers import *

pattern = re.compile('(-?\d+)')

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        for line in f:
            pos = list(map(int, pattern.findall(line)))
            r.append([pos, [0,0,0]])

        return r


def energy(moon):
    return math.prod(map(lambda c: sum(map(abs, c)), moon))


def total_energy(moons):
    return sum(map(energy, moons))


def step(moons):
    for a,b in itertools.combinations(moons, 2):
        gravity_a = tuple(map(lambda x: sign(x[1]-x[0]), zip(a[0], b[0])))
        gravity_b = tuple(map(lambda x: -x, gravity_a))
        a[1] = vadd(a[1], gravity_a)
        b[1] = vadd(b[1], gravity_b)

    for x in moons:
        x[0] = vadd(x[0], x[1])


def part1(filename, steps):
    input = parse_file(filename)
    ans = 0

    for _ in range(steps):
        step(input)

    ans = total_energy(input)

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)

    step_per_component = [0] * 3

    for i in range(3):
        turtle = deepcopy(input)
        rabbit = deepcopy(input)
        steps = 0

        while True:
            step(turtle)

            step(rabbit)
            step(rabbit)

            steps += 1

            def component_state(x):
                return [[c[i] for c in m] for m in x]

            turtle_state = component_state(turtle)
            rabbit_state = component_state(rabbit)

            if turtle_state == rabbit_state:
                break
        step_per_component[i] = steps

    ans = math.lcm(*step_per_component)

    print(step_per_component)

    print(f'P2 {filename}: {ans}')


# part1('example.txt', 10)
# part1('input.txt', 1000)

part2('input.txt')
# part2('input.txt')

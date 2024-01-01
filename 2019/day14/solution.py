from collections import defaultdict, Counter

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

def parse_file(filename):
    recipes = {}
    with open(filename, 'r') as f:
        for line in f:
            ins, out = line.split('=>')
            amt, x = out.split()

            ins = ins.split(',')

            def parsein(input):
                amt, x = input.split()
                return (int(amt), x)

            ins = tuple(map(parsein, ins))

            if x in recipes:
                print(f'ERR: {x} has multiple recipes')

            # lines.append((ins, int(amt), x))
            recipes[x] = (int(amt), ins)

    return recipes


def produce(recipes, extra, n=1):
    # queue = list(map(lambda x: (x[0]*n,x[1]), recipes['FUEL'][1]))
    queue = [(n, 'FUEL')]
    ore = 0

    while len(queue) > 0:
        amt, x = queue.pop(0)

        if x == 'ORE':
            ore += amt
            continue

        recipe = recipes[x]

        needed = amt - extra[x]

        n = math.ceil(needed / recipe[0])
        # print(f'producing {n * recipe[0]} {x} to satisfy need of {amt} ({extra[x]} extra)')

        extra[x] += n * recipe[0] - amt

        for amt, x in recipe[1]:
            needed = max(0, n*amt - extra[input])
            queue.append((needed, x))
    return ore

def part1(filename):
    recipes = parse_file(filename)
    # print(recipes)
    extra = defaultdict(int)
    ans = produce(recipes, extra)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    recipes = parse_file(filename)
    extra = defaultdict(int)
    ore = 1000000000000
    ans = 0

    full_speed = 0
    iterations = 100000

    i = 0
    while True:
        print(f'produced {ans} with {ore} left. Next iteration predicted to use {full_speed} ore...')
        if sum(extra.values()) > 100000 or ore < full_speed or iterations == 1 or ore < 1000000:
            if ore < full_speed and iterations > 1:
                iterations //= 10
                full_speed //= 10
                continue
            print(f'running single iteration: {sum(extra.values())}/{ore}/{full_speed}/{iterations}')
            needed = produce(recipes, extra)
            if ore > needed:
                ore -= needed
                ans += 1
            else:
                print(f'needed {needed} but only have {ore}; exiting')
                break
        else:
            print(f'running {iterations} iterations')

            # e = defaultdict(int)
            n = produce(recipes, extra, n=iterations)
            if n > ore:
                print('ERROR')
                break
            # for x,a in e.items():
            #     extra[x] += a * iterations
            ore -= n
            ans += iterations
            full_speed = n # * iterations

        i += 1

    print(f'P2 {filename}: {ans} {ore}')


# part1('example_easy.txt')
# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
part2('input.txt')

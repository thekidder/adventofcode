from collections import defaultdict, Counter

import functools
import itertools
import math
import re
import sys

from helpers import *

prefix = re.compile('^[\.#]+')

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            springs, constraints = line.split()
            lines.append((springs, list(map(int, constraints.split(',')))))

    return lines


def prune2(template, constraints):
    m = prefix.match(template)
    if m is None:
        return False
    p = m.group(0)
    # print(template, p, constraints)
    p = p.replace('.', ' ')
    groups = p.split()
    gg = list(map(len, groups))
    if len(gg) > len(constraints):
        return True

    if sum(constraints[len(gg):]) > len(template) - len(p):
        return True
    
    if len(gg) == 1:
        if gg != constraints[:len(gg)]:
            return True
    else:
        if gg[:-1] != constraints[:len(gg)-1] or gg[-1] > constraints[len(gg)-1]:
            return True
    
    return False


def generate(template, constraints = None):
    if '?' not in template:
        yield template
    i = 0
    while i < len(template):
        if template[i] == '?':
            break
        i += 1
    if i == len(template) or template[i] != '?':
        return
    print(f'BRANCHING AT {i}: {template}')
    if constraints is None or not prune2(template[:i] + '#' + template[i+1:], constraints):
        print(f'RECURSE {template[:i] + "#" + template[i+1:]}')
        for p in generate(template[:i] + '#' + template[i+1:], constraints):
            # print(f'GOT {p}')
            yield p
    if constraints is None or not prune2(template[:i] + '.' + template[i+1:], constraints):
        print(f'RECURSE {template[:i] + "." + template[i+1:]}')
        for p in generate(template[:i] + '.' + template[i+1:], constraints):
            # print(f'GOT {p}')
            yield p

# @functools.cache
def potential_patterns(template, constraints):
    r = defaultdict(int)
    for p in generate(template, constraints):
        p = p.replace('.', ' ')
        groups = p.split()
        r[tuple(map(len, groups))] += 1
    return r


def match(partials, constraints, matches = 1):
    r = 0
    if len(partials) == 0 and len(constraints) == 0:
        return matches
    if len(partials) == 0:
        return 0
    # print('P', partials, constraints, matches)
    for p, cnt in partials[0].items():
        if len(p) > 0 and list(p) == constraints[:len(p)]:
            r += match(partials[1:], constraints[len(p):], cnt)
        if len(p) == 0:
            r += match(partials[1:], constraints, cnt)
    return matches * r


def matches(pattern, constraints):
    pattern = pattern.replace('.', ' ')
    groups = pattern.split()
    if len(groups) == 1:
        partials = list(map(lambda g: potential_patterns(g, constraints), groups))
        # print(partials)
        return match(partials, constraints)
    else:
        partials = list(map(lambda g: potential_patterns(g, None), groups))
        # print(partials)
        return match(partials, constraints)


def prune(template, constraints):
    template = template.replace('.', ' ')
    groups = template.split()
    # print('G', groups)
    for g in groups:
        print(g, potential_patterns(g))
    groups = list(map(potential_patterns, groups))
    if not match(groups, constraints):
        return True

    return False


def evaluate(template, constraints):
    template = template.replace('.', ' ')
    groups = template.split()
    return constraints == list(map(len, groups))


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for i,(t,c) in enumerate(input):
        print(f'iter {i}')
        for p in generate(t, c):
            if evaluate(p, c):
                ans += 1
    print(f'P1 {filename}: {ans}')


def expand_input(i):
    i = [i] * 5
    return '?'.join(i)


def expand_constraints(i):
    i = i * 5
    return i


wild = re.compile('^[\?]+')
damage = re.compile('^[\#]+')


def prefixlen(pattern, str):
    m = pattern.match(str)
    if m is None:
        return 0
    return len(m.group(0))


def matches2(pattern, constraints):
    r = 0
    permutations = [(pattern, constraints, 1)]
    # pattern = pattern.replace('.', ' ')
    # groups = pattern.split()
    
    cntr = 0
    while len(permutations) > 0:
        if cntr % 100000 == 0:
            print(len(permutations), cntr, permutations[-1][0], permutations[-1][1])
        cntr += 1
        p, c, n = permutations.pop()#0)

        if len(p) == 0 and len(c) == 0:
            r += n
            continue

        if len(c) == 0:
            continue

        if p[0] == '.':
            permutations.append((p[1:], c, n))
            continue

        need = c[0]
        nwild = prefixlen(wild, p)
        ndamage = prefixlen(damage, p)

        # print(p,c,n,nwild,need,  len(permutations))

        if ndamage > 0 and ndamage > need:
            continue
        if nwild > need:
            for i in range(need, nwild+1):
                permutations.append((p[i:],c, n))
                if len(p) == nwild or p[nwild] == '.':
                    permutations.append((p[i:],c[1:], n * (i - need + 1)))
                else:
                    if i > need and i < nwild - 1:
                        permutations.append((p[i:],c[1:], n * (i - need)))
        elif nwild == need:
            if nwild == 0:
                sys.exit(0)
            permutations.append((p[nwild:],c, n))
            if p[nwild] == '.':
                permutations.append((p[nwild:],c[1:], n))
            # else:
                # print(f'got {p} {c}, can\'t proceed')
                # sys.exit(0)
        elif nwild > 0:
            permutations.append((p[nwild:],c, n))
            next_damage = prefixlen(damage, p[nwild:])
            next_wild = prefixlen(wild, p[nwild+next_damage:])
            # print(nwild, next_damage, next_wild, need)
            need -= nwild + next_damage
            if next_wild > need:
                permutations.append((p[nwild+next_damage+need+1:],c[1:], n))
            elif next_wild == need and p[nwild+next_damage+need] == '.':
                if nwild+next_damage+need == 0:
                    sys.exit(0)

                permutations.append((p[nwild+next_damage+need:],c[1:], n))
            # else:
            #     print(f'can\'t do {p} {c}')
            #     sys.exit(0)
        else:
            next_damage = prefixlen(damage, p)
            need -= next_damage
            if need == 0 and len(p) == next_damage or p[next_damage] != '#':
                permutations.append((p[next_damage+1:],c[1:], n))
            else:
                print(f'damage: can\'t do {p} {c} {need}')
                sys.exit(0)

        # else:
        #     print(f'got {p}, can\'t proceed')
        #     sys.exit(0)
    return r


def part2(filename):
    input = parse_file(filename)
    for i in range(len(input)):
        input[i] = (expand_input(input[i][0]), expand_constraints(input[i][1]))
    input = [input[1]]
    ans = 0
    for i,(t,c) in enumerate(input):
        # print(t)
        n = matches2(t, c)

        print(f'[{i}] {t} :: {c} -> {n}')

        ans += n
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# not 5654
# part1('input.txt')

part2('example.txt')
# part2('input.txt')

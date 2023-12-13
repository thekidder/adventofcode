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
maybedamage = re.compile('^[\#\?]+')


def prefixlen(pattern, str):
    m = pattern.match(str)
    if m is None:
        return 0
    return len(m.group(0))


def matches3(pattern, constraints):
    r = matches2(pattern, constraints)
    # if r > 0:
    #     print(pattern, constraints, r)
    return r


@functools.cache
def matches2(p, c):
    if len(p) == 0 and len(c) == 0:
        return 1

    if len(p) > 0 and p[0] == '.':
        return matches3(p[1:], c)

    if len(c) == 0:
        if '#' not in p:
            return 1
        else:
            return 0
        
    if len(p) == 0:
        return 0

    need = c[0]
    next_damage = prefixlen(maybedamage, p)
    
    r = 0

    if p[0] == '?':
        r += matches3(p[1:], c)

    if next_damage >= need:
        if len(p) == need or p[need] != '#':
            r += matches3(p[need+1:], c[1:])
    return r



def part2(filename):
    input = parse_file(filename)
    for i in range(len(input)):
        input[i] = (expand_input(input[i][0]), expand_constraints(input[i][1]))
    # input = [input[1]]
    ans = 0
    for i,(t,c) in enumerate(input):
        # print(t,c, ':START')
        n = matches3(t, tuple(c))

        print(f'[{i}] {t} :: {c} -> {n}')

        ans += n
    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# not 5654
# part1('input.txt')

# matches3('???.###', (1, 1, 3))
# matches3('?.??..??...?##.', (1, 1, 3))
# matches3('??..??...?##', (1, 3))

# print(matches3('.??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.', (1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3)))
# print(matches3('?#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#?', (1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6, 1, 3, 1, 6)))
# print(matches3('?#?#?#?#?', (1, 6)))
# print(matches3('????.#...#...?????.#...#...?????.#...#...?????.#...#...?????.#...#...', (4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1)))
# print(matches3('????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####.', (1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5, 1, 6, 5)))
# print(matches3('???.######..#####', (1, 6, 5)))
# print(matches3('?###??????????###??????????###??????????###??????????###????????', (3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1)))
# print(matches3('?###????????', (3, 2, 1)))
# print(matches3('?????', ( 1,1)))

# print(matches3('??#??????#..????????#??????#..????????#??????#..????????#??????#..????????#??????#..?????', (9, 2, 1, 9, 2, 1, 9, 2, 1, 9, 2, 1, 9, 2, 1))) # maybe -> 3888

# part2('example.txt')
# not 20397109448443 (too high)
# not 16171657110006 (too high)
part2('input.txt')

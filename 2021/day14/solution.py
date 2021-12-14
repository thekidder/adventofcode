from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    rules = {}
    with open(filename, 'r') as f:
        template = f.readline().strip()
        for line in f:
            if '->' in line:
                rule = line.split('->')
                rules[rule[0].strip()] = rule[1].strip()


    return template, rules


def pairs(template):
    for i in range(len(template) - 1):
        yield template[i:i+2], i


def part1(filename):
    template,rules = parse_file(filename)
    ans = 0
    print(rules)
    for i in range(10):
        out = ''
        for pair, idx in pairs(template):
            out += pair[0]
            if pair in rules:
                out += rules[pair]
        out += template[-1]
        template = out

        print(f'ITERATION {i+1}: {out}')

    cnt = Counter(out)
    top = cnt.most_common()
    print(top[0][1] - top[-1][1])



def part2(filename):
    template,rules = parse_file(filename)
    ans = 0
    print(rules)

    first = None
    last = None

    polymer = Counter()
    for pair, idx in pairs(template):
        if first is None:
            first = pair
        polymer.update([pair])
        last = pair

    for i in range(40):
        next = Counter(polymer)

        first = first[0] + rules[first]
        last = rules[last] + last[1]

        for rule, cnt in polymer.items():
            if cnt > 0 and rule in rules:
                new_letter = rules[rule]
                next[rule] -= cnt
                next[rule[0] + new_letter] += cnt
                next[new_letter + rule[1]] += cnt

        polymer = next

        # print(f'ITERATION {i+1}: {first} {last} {polymer}')

    cnts = defaultdict(int)
    for rule, cnt in polymer.items():
        cnts[rule[0]] += cnt
        cnts[rule[1]] += cnt

    for rule, cnt in cnts.items():
        if rule in first or rule in last:
            cnts[rule] += 1

        cnts[rule] /= 2
    print(cnts)
    top = Counter(cnts).most_common()
    print(top[0][1] - top[-1][1])


part2('input.txt')

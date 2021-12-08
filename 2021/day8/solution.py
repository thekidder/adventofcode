from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    patterns = []
    outputs = []
    with open(filename, 'r') as f:
        for line in f:
            l = line.split('|')
            p = l[0].strip().split()
            o = l[1].strip().split()
            patterns.append(p)
            outputs.append(o)

    return (patterns,outputs)


def part1(filename):
    patterns,outputs = parse_file(filename)
    ans = 0
    for o in outputs:
        for x in o:
            l = len(x)
            if l == 2 or l == 4 or l == 3 or l == 7:
                ans += 1

    print(f'ANSWER: {ans}')


all_segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
def make_map():
    segment_map = {}
    for s in all_segments:
        segment_map[s] = set(all_segments[:])
    return segment_map


def collapse(m, segments, possibilities):
    possibilities = set(possibilities)
    for segment in segments:
        m[segment] &= possibilities

    clean(m)

def clean(m):
    diff = True
    while diff:
        diff = False
        for segment in all_segments:
            if len(m[segment]) == 1:
                eliminated = next(iter(m[segment]))
                for o in all_segments:
                    if o != segment and eliminated in m[o]:
                        m[o].remove(eliminated)
                        diff = True


def decode(map, digit):
    mapped = ''
    print(digit)
    for c in digit:
        print(f'{c} -> {next(iter(map[c]))}')
        mapped += next(iter(map[c]))
    print(mapped)

    digits = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }
    for c in digits:
        print(f'{digit} {c}')
        if set(mapped) == set(c):
            return digits[c]

def part2(filename):
    patterns,outputs = parse_file(filename)
    ans = 0
    for i in range(len(patterns)):
        print('LINE')
        ps = patterns[i]
        digits = outputs[i]

        segment_map = make_map()

        fives = []
        sixes = []
        for p in ps:
            if len(p) == 2:
                collapse(segment_map, p, 'cf')
            if len(p) == 3:
                collapse(segment_map, p, 'acf')
            if len(p) == 4:
                collapse(segment_map, p, 'bcdf')
            if len(p) == 5:
                fives.append(p)
            if len(p) == 6:
                sixes.append(p)
        five_cnt = defaultdict(int)
        six_cnt = defaultdict(int)
        print(fives)
        for x in fives:
            for c in x:
                five_cnt[c] += 1

        for s in all_segments:
            if five_cnt[s] == 2:
                collapse(segment_map, s, 'cf')
            if five_cnt[s] == 1:
                collapse(segment_map, s, 'eb')

        for x in sixes:
            for c in x:
                six_cnt[c] += 1

        for s in all_segments:
            if six_cnt[s] == 2:
                collapse(segment_map, s, 'cde')


        print(segment_map)
        a = ''
        for o in digits:
            i = str(decode(segment_map, o))
            a += i
        a = int(a)
        ans += a



    print(f'ANSWER: {ans}')


part2('input.txt')

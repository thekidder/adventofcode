from collections import defaultdict, Counter

import functools

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


def observe(m, segments, possibilities):
    possibilities = set(possibilities)
    for segment in segments:
        m[segment] &= possibilities

    collapse(m)

def collapse(m):
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


def map_digit(map, digit):
    mapped = ''
    for c in digit:
        mapped += next(iter(map[c]))
    return mapped


def decode(map, digit):
    mapped = map_digit(map, digit)
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
        if set(mapped) == set(c):
            return digits[c]


def count_segments(patterns):
    cnt = Counter()
    for pattern in patterns:
        cnt.update(pattern)
    return cnt


def part2(filename):
    patterns,outputs = parse_file(filename)
    ans = 0
    for ps,digits in zip(patterns,outputs):
        segment_map = make_map()

        patterns_by_len = defaultdict(list)
        for pattern in ps:
            patterns_by_len[len(pattern)].append(pattern)

        for pattern_len, p in patterns_by_len.items():
            if pattern_len == 2:
                for pattern in p:
                    observe(segment_map, pattern, 'cf')
            elif pattern_len == 3:
                for pattern in p:
                    observe(segment_map, pattern, 'acf')
            elif pattern_len == 4:
                for pattern in p:
                    observe(segment_map, pattern, 'bcdf')
            elif pattern_len == 5:
                segment_cnt = count_segments(p)
                for segment, cnt in segment_cnt.items():
                    if cnt == 1:
                        observe(segment_map, segment, 'eb')
                    elif cnt == 2:
                        observe(segment_map, segment, 'cf')
            elif pattern_len == 6:
                segment_cnt = count_segments(p)
                for segment, cnt in segment_cnt.items():
                    if cnt == 2:
                        observe(segment_map, segment, 'cde')

        a = ''
        for o in digits:
            i = str(decode(segment_map, o))
            a += i
        a = int(a)
        ans += a

    print(f'ANSWER: {ans}')


part2('example.txt')

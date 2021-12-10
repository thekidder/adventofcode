from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())

    return lines


chunks = [
    '()',
    '[]',
    '{}',
    '<>',
]

def invalid_score(c):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137


def is_open(c):
    return any(map(lambda x: x[0] == c, chunks))


def get_close(c):
    for chunk in chunks:
        if chunk[0] == c:
            return chunk[1]

def part1(filename):
    ans = 0
    lines = parse_file(filename)
    for line in lines:
        open_chunks = []
        for c in line:
            if is_open(c):
                open_chunks.append(c)
            else:
                open_chunk = open_chunks.pop()
                chunk = open_chunk + c
                if chunk not in chunks:
                    ans += invalid_score(c)
                    continue
        
    print(f'ANSWER: {ans}')


def valid_score(c):
    if c == ')':
        return 1
    elif c == ']':
        return 2
    elif c == '}':
        return 3
    elif c == '>':
        return 4


def incomplete_lines(lines):
    for line in lines:
        valid = True
        open_chunks = []
        for c in line:
            if is_open(c):
                open_chunks.append(c)
            else:
                open_chunk = open_chunks.pop()
                chunk = open_chunk + c
                if chunk not in chunks:
                    valid = False
                    continue
        if valid:
            yield line, open_chunks
            


def part2(filename):
    scores = []
    lines = parse_file(filename)
    for line, chunks in incomplete_lines(lines):
        score = 0
        while len(chunks):
            open = chunks.pop()
            close = get_close(open)
            score *= 5
            score += valid_score(close)
        scores.append(score)
    scores.sort()

    print(len(scores))
    ans = scores[int(len(scores)/2)]

    print(f'ANSWER: {ans}')



part2('input.txt')

from collections import defaultdict, Counter

import copy
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
            lines.append([c for c in line.strip()])

    return lines


def nextpos(x,y,state):
    cuke = state[y][x]
    if cuke == '>':
        return (x+1)%len(state[y]),y
    else:
        return x,(y+1)%len(state)

def printgrid(state):
    for line in state:
        for c in line:
            print(c,end='')
        print()
    print()

def part1(filename):
    input = parse_file(filename)
    printgrid(input)

    i = 0
    while True:
        last = copy.deepcopy(input)
        next = copy.deepcopy(input)
        for y,line in enumerate(input):
            for x,cuke in enumerate(line):
                if cuke == '>':
                    nx,ny = nextpos(x,y,input)
                    if input[ny][nx] == '.':
                        next[ny][nx] = '>'
                        next[y][x] = '.'

        input = next
        next = copy.deepcopy(input)
        # printgrid(input)

        for y,line in enumerate(input):
            for x,cuke in enumerate(line):
                if cuke == 'v':
                    nx,ny = nextpos(x,y,input)
                    if input[ny][nx] == '.':
                        # print(f'move at {x},{y} to {nx},{ny}')
                        next[ny][nx] = 'v'
                        next[y][x] = '.'

        input = next

        if i < 5 or i % 10 == 0:
            print(f'STEP {i}')
            # printgrid(input)

        if input == last:
            break
        i += 1




    # printgrid(input)
    print(f'ANSWER: {i+1}')


def part2(filename):
    pass


part1('input.txt')

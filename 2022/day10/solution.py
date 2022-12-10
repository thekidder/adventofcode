from collections import defaultdict, Counter

import functools
import math
import re
import sys


# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        return lines.split('\n')


buffer = ['.'] * 6 * 40


def draw(pos):
    pos = pos - 1
    if pos < 0 or pos >= len(buffer):
        return
    buffer[pos] = '#'


def printscrn():
    for i in range(len(buffer)):
        print(buffer[i], end = '')
        if (i+1) % 40 == 0:
            print()


def part1(filename):
    global buffer
    buffer = ['.'] * 6 * 40
    cycle = 1
    input = parse_file(filename)
    pipeline = []
    x = 1
    ans = 0
    while len(input):
        popped_arg = None
        if len(pipeline) > 0:
            popped_arg = pipeline.pop(0)
        else:
            line = input[0]
            input = input[1:]
            if line.startswith('noop'):
                pass
            else:
                # print(line)
                _, arg = line.split(' ')
                arg = int(arg)
                # print(x,arg)
                pipeline.append(arg)

        pos = cycle % 40
        if pos == (x) or pos == x+1 or pos == (x+2):
            draw(cycle)

        if cycle >= 20 and (cycle + 20) % 40 == 0:
            print(ans,x,cycle)
            ans += (x * cycle)

        cycle += 1
        if popped_arg is not None:
            x += popped_arg
    print(f'P1 {filename}: {ans}')
    printscrn()


part1('example.txt')
part1('input.txt')

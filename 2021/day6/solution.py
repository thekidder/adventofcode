from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    with open(filename, 'r') as f:
        fishes = f.readline().split(',')
        return [int(n) for n in fishes]


def part1(filename):
    fishes = parse_file(filename)
    print(f'Initial State: {fishes}')

    days = 256
    i = 0
    while days > 0:
        new_fishes = []
        for i in range(len(fishes)):
            fishes[i] -= 1
            if fishes[i] == -1:
                fishes[i] = 6
                new_fishes.append(8)
        fishes.extend(new_fishes)
        i += 1
        print(f'After {i} days: {fishes}')

        days -= 1
    ans = 0
    print(f'ANSWER: {len(fishes)}')


def total(counter):
    cnt = 0
    for val in counter.values():
        cnt += val
    return cnt

def part2(filename):
    fishes = parse_file(filename)
    fishes = Counter(fishes)
    print(f'Initial State: {fishes}')

    days = 256
    day = 0
    while days > 0:
        next_fishes = Counter()
        for i in range(9, -1, -1):
            num_fishes_of_day = fishes[i]
            print(f'got {num_fishes_of_day} at {i}')
            if i == 0:
                next_fishes[6] += num_fishes_of_day
                next_fishes[8] += num_fishes_of_day
            else:
                next_fishes[i-1] += num_fishes_of_day

        fishes = next_fishes
                
        day += 1
        print(fishes)
        print(f'After {day} days: {total(fishes)}')

        days -= 1
    ans = 0
    print(f'ANSWER: {len(fishes)}')


part2('input.txt')

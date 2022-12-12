from collections import defaultdict

import operator
import sys


def parse_file(filename):
    with open(filename, 'r') as f:
        result = defaultdict(lambda:None)
        for y,line in enumerate(f.readlines()):
            for x,val in enumerate(line):
                result[(x,y)] = val
        return result


def find(m, symbol):
    for coord,val in m.items():
        if val == symbol:
            return coord


neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
def candidates(m, coord):
    x = m[coord]
    for dir in neighbors:
        n = tuple(map(operator.add, coord, dir))
        y = m[n]
        if y is not None and ord(x) - ord(y) <= 1:
            yield n


def solve(filename):
    input = parse_file(filename)
    start = find(input, 'S')
    end = find(input, 'E')
    input[start] = 'a'
    input[end] = 'z'
    distances_from_end = {}
    # queue is of coord, num_steps
    queue = [(end, 1)]
    while len(queue) > 0:
        c, d = queue.pop(0)
        for n in candidates(input, c):
            if n not in distances_from_end or distances_from_end[n] > d:
                distances_from_end[n] = d
                queue.append((n, d+1))

    ans = sys.maxsize
    for c,v in distances_from_end.items():
        if input[c] == 'a':
            ans = min(ans, v)
    print(f'P1 {filename}: dist to E: {distances_from_end[start]}; dist to any a: {ans}')


solve('example.txt')
solve('input.txt')

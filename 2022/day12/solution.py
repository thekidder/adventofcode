from collections import defaultdict

import operator
import sys


def parse_file(filename):
    with open(filename, 'r') as f:
        result = defaultdict(lambda:-1000)
        for y,line in enumerate(f.readlines()):
            for x,val in enumerate(line):
                coord = (x,y)
                if val == 'S':
                    result[coord] = 0
                    start = coord
                elif val == 'E':
                    result[coord] = 25
                    end = coord
                else:
                    result[coord] = ord(val) - ord('a')
        return result, start, end
        

neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
def candidates(m, coord):
    x = m[coord]
    for dir in neighbors:
        n = tuple(map(operator.add, coord, dir))
        y = m[n]
        if x-y <= 1:
            yield n


def solve(filename):
    input,start,end = parse_file(filename)
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
        if input[c] == 0:
            ans = min(ans, v)
    print(f'P1 {filename}: dist to E: {distances_from_end[start]}; dist to any a: {ans}')


solve('example.txt')
solve('input.txt')

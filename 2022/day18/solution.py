from collections import defaultdict
import operator
import sys

from helpers import *

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            r.append(tuple(map(int, l.split(','))))
            
        return r


def populate_edges(edges, coord):
    edges[vadd(coord, (-1,0,0)) + ('X',)] += 1
    edges[vadd(coord, (0,-1,0)) + ('Y',)] += 1
    edges[vadd(coord, (0,0,-1)) + ('Z',)] += 1

    edges[coord + ('X',)] += 1
    edges[coord + ('Y',)] += 1
    edges[coord + ('Z',)] += 1


def part1(filename):
    input = parse_file(filename)
    edges = defaultdict(int)
    for coord in input:
        populate_edges(edges, coord)
        
    ans = 0
    for edge in edges.values():
        if edge == 1:
            ans += 1
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    edges = defaultdict(int)

    filled = {x: True for x in input}

    min_coord = (sys.maxsize,sys.maxsize,sys.maxsize)
    max_coord = (0,0,0)

    for coord in input:
        min_coord = tuple(map(min, min_coord, coord))
        max_coord = tuple(map(max, max_coord, coord))

        populate_edges(edges, coord)
    ans = 0

    memo = {}
    def is_inside(c):
        if c in memo and memo[c]:
            return True
        q = [c]
        all = set()
        while len(q) > 0:
            c = q.pop()
            if c not in filled:                
                if c in memo and memo[c]:
                    break
                all.add(c)
                if any(map(operator.le, c, min_coord)) or any(map(operator.ge, c, max_coord)):
                    return False
                for n in [
                    vadd(c, (-1,0,0)),
                    vadd(c, (0,-1,0)),
                    vadd(c, (0,0,-1)),
                    vadd(c, (1,0,0)),
                    vadd(c, (0,1,0)),
                    vadd(c, (0,0,1)),
                ]:
                    if n not in all and n not in filled:
                        q.append(n)
        for c in all:
            memo[c] = True
        return True

    for x in range(min_coord[0], max_coord[0]+1):
        for y in range(min_coord[1], max_coord[1]+1):
            for z in range(min_coord[2], max_coord[2]+1):
                coord = (x,y,z)
                if coord in filled:
                    continue
                if is_inside(coord):
                    populate_edges(edges, coord)

    for edge in edges.values():
        if edge == 1:
            ans += 1

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

from queue import PriorityQueue
from helpers import *

slopes = {
    'E': '>',
    'W': '<',
    'N': '^',
    'S': 'v',
}

def neighbors(input, coord, ignore_slopes=False):
    for d, dir in dirs.items():
        next = vadd(coord, dir)
        if next not in input:
            continue
        v = input[next]
        if v == '.' or (ignore_slopes and v in slopes.values()):
            yield next
        if v == slopes[d]:
            yield next


def find_longest(input, start, end):
    paths = PriorityQueue()
    paths.put((-1, start, set([start])))
    mlen = 0
    while not paths.empty():
        # print(paths.qsize())
        p = paths.get()
        for n in neighbors(input, p[1]):
            if n in p[2]:
                continue
            if n == end:
                mlen = max(mlen, -p[0])
            else:
                paths.put((p[0] - 1, n, p[2] | set([n])))
    return mlen


def find_neighbors(input, start, intersections):
    pathlens = {}
    paths = [(0, start, set([start]))]
    while len(paths) > 0:
        p = paths.pop()
        for n in neighbors(input, p[1], ignore_slopes=True):
            if n in p[2]:
                continue
            if n in intersections:
                pathlens[n] = p[0] + 1
            else:
                paths.append((p[0] + 1, n, p[2] | set([n])))
    return pathlens


def part1(filename):
    input,mx,my = parse_grid(filename)
    start = (1, 0)
    end = (mx-1,my)

    ans = find_longest(input, start, end)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input,mx,my = parse_grid(filename)
    start = (1, 0)
    end = (mx-1,my)

    intersections = set([start,end])
    for c,v in input.items():
        if v == '#':
            continue
        ns = [n for n in neighbors(input, c, ignore_slopes=True)]
        if len(ns) > 2:
            intersections.add(c)
    graph = {}
    for i in intersections:
        graph[i] = find_neighbors(input, i, intersections)

    paths = PriorityQueue()
    paths.put((0, start, set([start])))
    ans = 0
    while not paths.empty():
        p = paths.get()
        for c,d in graph[p[1]].items():
            if c in p[2]:
                continue
            if c == end:
                ans = max(ans, -p[0]+d)
            else:
                paths.put((p[0] - d, c, p[2] | set([c])))

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

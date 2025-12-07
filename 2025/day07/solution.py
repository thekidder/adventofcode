from collections import defaultdict

from helpers import *

def parse_file(filename):
    grid, sx, sy = parse_grid(filename)

    for x in range(sx):
        if grid[(x, 0)] == 'S':
            return grid, sx, sy, x
    return None


def part1(filename):
    grid, sx, sy, start = parse_file(filename)
    ans = 0
    beams = set([start])

    for y in range(1, sy):
        next = set()
        for beam in beams:
            if grid[(beam, y)] == '^':
                ans += 1
                next.add(beam-1)
                next.add(beam+1)
            else:
                next.add(beam)
        beams = next

    print(f'P1 {filename}: {ans}')


def part2(filename):
    grid, sx, sy, start = parse_file(filename)
    ans = 0
    beams = defaultdict(int)
    beams[start] += 1

    for y in range(1, sy):
        next = defaultdict(int)
        for beam, cnt in beams.items():
            if grid[(beam, y)] == '^':
                next[beam+1] += cnt
                next[beam-1] += cnt
            else:
                next[beam] += cnt
        beams = next

    for beam, cnt in beams.items():
        ans += cnt

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

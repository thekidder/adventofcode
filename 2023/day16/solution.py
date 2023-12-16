from collections import defaultdict

from helpers import *


def empty(dir): 
    return [dir]


def slash(dir):
    if dir == 'N' or dir == 'S':
        return turn_right(dir)
    return turn_left(dir)


def backslash(dir):
    if dir == 'N' or dir == 'S':
        return turn_left(dir)
    return turn_right(dir)


def split_vert(dir):
    if dir == 'N' or dir == 'S':
        return [dir]
    return ['N', 'S']


def split_horz(dir):
    if dir == 'E' or dir == 'W':
        return [dir]
    return ['E', 'W']


next = {
    '.': empty,
    '/': slash,
    '\\': backslash,
    '-': split_horz,
    '|': split_vert,
}


def part1(filename):
    input,mx,my = parse_grid(filename)
    # print_grid(input,mx,my)

    beam_grid = defaultdict(list)

    beams = [(((0,0),'E'))]

    while len(beams) > 0:
        coord,dir = beams.pop()
        if coord not in input:
            continue
        beam_grid[coord].append(dir)
        next_dirs = next[input[coord]](dir)
        for ndir in next_dirs:
            ncoord = vadd(dirs[ndir], coord)
            if ndir not in beam_grid[ncoord]:
                beams.append((ncoord,ndir))

    # print(beam_grid)

    ans = sum(map(lambda dirs: 1 if len(dirs) > 0 else 0, beam_grid.values()))
    print(f'P1 {filename}: {ans}')


def energy(input, coord, dir):
    beam_grid = defaultdict(list)

    beams = [((coord,dir))]

    while len(beams) > 0:
        coord,dir = beams.pop()
        if coord not in input:
            continue
        beam_grid[coord].append(dir)
        next_dirs = next[input[coord]](dir)
        for ndir in next_dirs:
            ncoord = vadd(dirs[ndir], coord)
            if ndir not in beam_grid[ncoord]:
                beams.append((ncoord,ndir))            

    return sum(map(lambda dirs: 1 if len(dirs) > 0 else 0, beam_grid.values()))

def part2(filename):
    input,mx,my = parse_grid(filename)

    maxe = 0

    for x in range(mx+1):
        maxe = max(maxe, energy(input, (x,0), 'S'))
        maxe = max(maxe, energy(input, (x,my), 'N'))

    for y in range(my+1):
        maxe = max(maxe, energy(input, (0,y), 'E'))
        maxe = max(maxe, energy(input, (mx,y), 'W'))

     
    print(f'P2 {filename}: {maxe}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

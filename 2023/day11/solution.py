import itertools

from helpers import *

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append([x for x in line.strip()])

    return lines


def col(input, idx):
    for j in range(len(input)):
        yield input[j][idx]


def print_galaxy(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end = '')
        print()


def expand(input):
    output = []
    for row in input:
        output.append(row)
        if all(map(lambda c: c == '.', row)):
            output.append(['.'] * len(row))

    cols = len(output[0])
    i = 0
    while i < cols:
        if all(map(lambda c: c == '.', col(output, i))):
            for row in output:
                row.insert(i, '.')
            i += 1
            cols += 1
        i += 1

    return output


def part1(filename):
    input = parse_file(filename)
    input = expand(input)
    ans = 0
    galaxies = []
    for y,line in enumerate(input):
        for x,c in enumerate(line):
            if c == '#':
                galaxies.append((x,y))
    for a,b in itertools.combinations(galaxies, 2):
        ans += mhn_dist(a,b)
    print(f'P1 {filename}: {ans}')


def empty_row(input, y, mx):
    for x in range(mx+1):
        if input[(x,y)] == '#':
            return False
        
    return True


def empty_col(input, x, my):
    for y in range(my+1):
        if input[(x,y)] == '#':
            return False
        
    return True


def expand2(input,mx,my):
    expand_rows = []
    expand_cols = []
    
    for y in range(my):    
        if empty_row(input, y, mx):
            expand_rows.append(y)

    for x in range(mx):    
        if empty_col(input, x, my):
            expand_cols.append(x)

    for coord in input.copy().keys():
        if input[coord] == '.':
            del input[coord]

    galaxies = list(input.keys())

    for row in reversed(expand_rows):
        for i, galaxy in enumerate(galaxies):
            if galaxy[1] > row:
                galaxies[i] = (galaxies[i][0], galaxies[i][1] + 999999)

    for row in reversed(expand_cols):
        for i, galaxy in enumerate(galaxies):
            if galaxy[0] > row:
                galaxies[i] = (galaxies[i][0] + 999999, galaxies[i][1])

    return galaxies
        

def part2(filename):
    input,mx,my = parse_grid(filename)
    galaxies = expand2(input,mx,my)
    ans = 0
    for a,b in itertools.combinations(galaxies, 2):
        ans += mhn_dist(a,b)

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

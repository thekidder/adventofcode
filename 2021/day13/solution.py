from collections import defaultdict, Counter

import re
import math
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

fold_x = re.compile('x=(\d+)')
fold_y = re.compile('y=(\d+)')

max_y = 0
max_x = 0

def parse_file(filename):
    global max_x,max_y
    folds = []
    with open(filename, 'r') as f:
        grid = defaultdict(bool)
        for line in f:
            pos = line.split(',')
            if len(pos) == 2:
                x = int(pos[0])
                y = int(pos[1])
                max_x = max(x, max_x)
                max_y = max(y, max_y)
                grid[(x,y)] = True
            elif len(line.strip()) != 0:
                m = fold_x.search(line)
                if m is not None:
                    folds.append(('x', int(m.group(1))))
                else:
                    m = fold_y.search(line)
                    folds.append(('y', int(m.group(1))))

    board = []
    for y in range(max_y+1):
        line = []
        for x in range(max_x+1):
            line.append(grid[(x,y)])

        board.append(line)


    return board,folds




def part1(filename):
    global max_x,max_y
    input,folds = parse_file(filename)
    ans = 0
    # print(input)
    print(max_x,max_y)
    print(folds)

    fold = folds[0]
    pos = fold[1]
    if fold[0] == 'x':
        for x in range(pos):
            for y in range(max_y + 1):
                input[y][pos - x - 1] = input[y][pos - x - 1] | input[y][pos + x + 1]
        for line in input:
            line = line[:pos]
        max_x = pos - 1
    else:
        for y in range(pos):
            for x in range(max_x + 1):
                input[pos - y - 1][x] = input[pos - y - 1][x] | input[pos + y + 1][x]
        input = input[:pos]
        max_y = pos - 1

    # print(input)

    for y in range(max_y+1):
        for x in range(max_x+1):
            if input[y][x]:
                ans += 1


    print(f'ANSWER: {ans}')


def p(c):
    if c == True:
        return '#'
    return '.'

def part2(filename):
    global max_x,max_y
    input,folds = parse_file(filename)
    ans = 0
    # print(input)
    print(max_x,max_y)
    print(folds)

    for fold in folds:
        pos = fold[1]
        if fold[0] == 'x':
            for x in range(pos):
                for y in range(max_y + 1):
                    input[y][pos - x - 1] = input[y][pos - x - 1] | input[y][pos + x + 1]
            for y in range(len(input)):
                input[y] = input[y][:pos]
            max_x = pos - 1
        else:
            for y in range(pos):
                for x in range(max_x + 1):
                    input[pos - y - 1][x] = input[pos - y - 1][x] | input[pos + y + 1][x]
            input = input[:pos]
            max_y = pos - 1

    print(max_x,max_y)

    for line in input:
        print(''.join(map(p, line)))

    # print(input)

    # for y in range(max_y+1):
    #     for x in range(max_x+1):
    #         if input[y][x]:
    #             ans += 1


    # print(f'ANSWER: {ans}')


part2('input.txt')

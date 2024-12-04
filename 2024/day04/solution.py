from helpers import *


def find(input, word, pos, direction, index):
    if index == len(word):
        return True
    if pos not in input:
        return False
    if input[pos] != word[index]:
        return False
    return find(input, word, vadd(pos, direction), direction, index + 1)


def part1(filename):
    input,_,_ = parse_grid(filename)
    ans = 0
    for pos in input.keys():
        for dir in all_directions():
            if find(input, 'XMAS', pos, dir, 0):
                ans += 1

    print(f'P1 {filename}: {ans}')


diagonals = [
    (-1,-1),
    ( 1,-1),
    (-1, 1),
    ( 1, 1),
]

def part2(filename):
    input,_,_ = parse_grid(filename)
    ans = 0
    for pos in input.keys():
        cnt = 0
        for dir in diagonals:
            cnt += find(input, 'MAS', vadd(pos, dir), vneg(dir), 0)

        if cnt == 2:
            ans += 1

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

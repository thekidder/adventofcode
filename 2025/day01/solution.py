from helpers import *

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append((line[0], int(line[1:])))

    return lines


def part1(filename):
    input = parse_file(filename)
    position = 50
    ans = 0
    for ins, amt in input:
        if ins == 'L':
            position = (position - amt) % 100
        else:
            position = (position + amt) % 100
        if position == 0:
            ans += 1

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    position = 50
    ans = 0
    for ins, amt in input:
        old = position
        if ins == 'L':
            rot_dir = -1
            raw = position - amt
        else:
            rot_dir = 1
            raw = position + amt
        position = raw % 100
        final_dir = sign(position - old)
        spins = amt // 100
        # print(f'rotate {ins}{a mt}: {old} -> {position} ({raw}) [{rot_dir}, {final_dir}, {spins}]')
        if position == 0:
            # print(f'  landed at zero')
            ans += 1
        if rot_dir != final_dir and old != 0 and position != 0:
            # print(f'  passed zero once')
            ans += 1
        if spins > 0:
            # print(f'  spun around zero {spins} times')
            ans += spins

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt') 

import re

from helpers import *

a = re.compile('Button A: X\+(\d+), Y\+(\d+)')
b = re.compile('Button B: X\+(\d+), Y\+(\d+)')
p = re.compile('Prize: X=(\d+), Y=(\d+)')

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        for section in sections:
            m = a.search(section)
            a_coord = (int(m.group(1)), int(m.group(2)))
            m = b.search(section)
            b_coord = (int(m.group(1)), int(m.group(2)))
            m = p.search(section)
            prize_coord = (int(m.group(1)), int(m.group(2)))
            r.append((a_coord, b_coord, prize_coord))

        return r


def tokens(x):
    a_amt, b_amt, prize = x
    for i in range(100):
        for j in range(100):
            pos = vadd((a_amt[0]*i, a_amt[1]*i), (b_amt[0]*j, b_amt[1]*j))
            if pos == prize:
                return i * 3 + j
    return 0


def tokens2(x):
    a_amt, b_amt, prize = x
    a = 1
    b = 1
    while a > 0 and b > 0:
        b1 = (prize[0] - (a_amt[0] * a)) // b_amt[0]
        b2 = (prize[1] - (a_amt[1] * a)) // b_amt[1]
        if b1 == b2:
            b = b1
            pos = vadd((a_amt[0]*a, a_amt[1]*a), (b_amt[0]*b, b_amt[1]*b))
            if pos == prize:
                return a * 3 + b

        a += max(1, abs(b1 - b2) // 10000)
        b = b1
    return 0


def part1(filename):
    input = parse_file(filename)
    ans = 0

    for x in input:
        ans += tokens(x)

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0

    for i,x in enumerate(input):
        x = (x[0], x[1], (x[2][0] + 10000000000000, x[2][1] + 10000000000000))
        ans += tokens2(x)
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

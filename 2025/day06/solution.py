import functools

from helpers import *


def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        for l in lines:
            if l[0] == '*' or l[0] == '+':
                r.append(l.split())
            else:
                r.append(mapl(int, l.split()))
    
        return r
    

def parse_file2(filename):
    ops = []
    nums = []
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        input = lines[:-1]
        group = []
        for col in range(len(input[0])):
            x = 0
            num = False
            for row in range(len(input)):
                digit = input[row][col]
                if digit != ' ':
                    num = True
                    x *= 10
                    x += int(digit)
            if num:
                group.append(x)
            else:
                nums.append(group)
                group = []
        nums.append(group)
    
    for op in lines[-1].split():
        ops.append(op)

    return nums, ops


def part1(filename):
    input = parse_file(filename)
    ans = 0

    ops = input[-1]
    input = input[:-1]

    for i in range(len(input[0])):
        if ops[i] == '*':
            op = operator.mul
        else:
            op = operator.add
        operands = [input[j][i] for j in range(len(input))]
        ans += functools.reduce(op, operands)

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input, ops = parse_file2(filename)
    ans = 0

    # print(input, ops)
    print(len(input), len(ops))

    for i in range(len(ops)):
        if ops[i] == '*':
            op = operator.mul
        else:
            op = operator.add
        operands = input[i]
        # print(ops[i], i, operands)
        ans += functools.reduce(op, operands)


    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

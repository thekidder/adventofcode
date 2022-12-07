from collections import defaultdict, Counter

import functools
import math
import re
import sys

# regex example
# pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
# m = line_pattern.match(line)
# x = int(m.group(1)) # 0 is the entire capture group

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)

    return lines


def size(tree):
    s = 0
    for k,v in tree.items():
        if type(v) is dict:
            s += size(v)
        else:
            s += v
    return s


def store(tree, stack, file):
    ptr = tree
    stack = stack[:]
    while(len(stack) > 0):
        dir = stack.pop(0)
        ptr = ptr[dir]

    if file.startswith('dir'):
        file = file[4:].strip()
        ptr[file] = {}
    else:
        size, name = file.split(' ')
        ptr[name.strip()] = int(size)


def p1(tree):
    ans = 0
    for k, v in tree.items():
        if type(v) is dict:
            s = size(v)
            if s < 100000:
                # print(f'{k} has size {s}')
                ans += s
            ans += p1(v)
    return ans


def p2(tree, min, used):
    needed = 30000000 - (70000000 - used)
    print(needed)
    for k, v in tree.items():
        if type(v) is dict:
            s = size(v)
            if s >= needed and (min == -1 or s < min):
                print(f'min i {s}')
                min = s
            min = p2(v, min, used)
    return min


def part1(filename):
    input = parse_file(filename)
    stack = []
    tree = {}
    while len(input) > 0:
        l = input[0].strip()
        input = input[1:]
        if l.startswith('$'):
            command = l[2:].strip()
            if command.startswith('ls'):
                while len(input) > 0 and not input[0].startswith('$'):
                    file = input[0]
                    store(tree, stack, file)
                    input = input[1:]
            elif command.startswith('cd'):
                dir = command[2:].strip()
                if dir == '/':
                    stack = []
                elif dir == '..':
                    stack.pop()
                else:
                    stack.append(dir)
                print(stack)
            else:
                print('ERROR')
            
    ans = p1(tree)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    stack = []
    tree = {}
    while len(input) > 0:
        l = input[0].strip()
        input = input[1:]
        if l.startswith('$'):
            command = l[2:].strip()
            if command.startswith('ls'):
                while len(input) > 0 and not input[0].startswith('$'):
                    file = input[0]
                    store(tree, stack, file)
                    input = input[1:]
            elif command.startswith('cd'):
                dir = command[2:].strip()
                if dir == '/':
                    stack = []
                elif dir == '..':
                    stack.pop()
                else:
                    stack.append(dir)
                print(stack)
            else:
                print('ERROR')
            
    used = size(tree)
    ans = p2(tree, -1, used)
    print(f'P2 {filename}: {ans}')

# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

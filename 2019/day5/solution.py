from collections import defaultdict, Counter

import functools
import math
import re
import sys


def parse(s):
    return [x for x in map(int, s.strip().split(','))]


def parse_file(filename):
    with open(filename, 'r') as f:
        return parse(f.read())


def load(memory, ptr, mode):
    if ptr >= len(memory):
        print(f'PTR ERR {mode} {ptr}')
        return None
    addr = memory[ptr]
    if mode == 1:
        return addr
    if addr >= len(memory) or addr < 0:
        print(f'ADDR ERR {mode} {ptr} {addr}')
        return None
    return memory[addr]

    
def run(memory, input):
    cnt = 0
    mode = 0
    while True:
        instr = memory[cnt]
        op = instr % 100
        instr //= 100
        modes = []
        for i in range(3):
            modes.append(instr % 10)
            instr //= 10

        if op == 1:
            print(modes,'ADD ',memory[cnt+1],memory[cnt+2],memory[cnt+3])
            if cnt+3 >= len(memory):
                print('ERROR')
                return None
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 is None or p2 is None:
                return None
            memory[memory[cnt+3]] = p1 + p2
            cnt += 4
        elif op == 2:
            print(modes,'MULT',memory[cnt+1],memory[cnt+2],memory[cnt+3])
            if cnt+3 >= len(memory):
                print('ERROR')
                return None
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 is None or p2 is None:
                return None
            memory[memory[cnt+3]] = p1 * p2
            cnt += 4
        elif op == 3:
            print(modes,'LOAD',len(input), memory[cnt+1])
            i = input.pop(0)
            memory[memory[cnt+1]] = i
            cnt += 2
        elif op == 4:
            print(modes,'STOR',memory[cnt+1])
            p1 = load(memory, cnt+1, modes[0])
            print(f'OUTPUT {p1}')
            cnt += 2
        elif op == 5:
            print(modes,'JMPT',i, memory[cnt+1],memory[cnt+2])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 != 0:
                cnt = p2
            else:
                cnt += 3
        elif op == 6:
            print(modes,'JMPF',i, memory[cnt+1],memory[cnt+2])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 == 0:
                cnt = p2
            else:
                cnt += 3
        elif op == 7:
            print(modes,'LESS',i, memory[cnt+1],memory[cnt+2],memory[cnt+3])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 < p2:
                memory[memory[cnt+3]] = 1
            else:
                memory[memory[cnt+3]] = 0
            cnt += 4
        elif op == 8:
            print(modes,'EQUL',i, memory[cnt+1],memory[cnt+2],memory[cnt+3])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 == p2:
                memory[memory[cnt+3]] = 1
            else:
                memory[memory[cnt+3]] = 0
            cnt += 4
        elif op == 99:
            break
        else:
            print(f'ERROR {op}')
            return None

    return memory


def part1(filename):
    input = parse_file(filename)
    run(input, [1])


def part2(filename):
    input = parse_file(filename)
    run(input, [5])


part2('input.txt')
# run(parse('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'), [0])

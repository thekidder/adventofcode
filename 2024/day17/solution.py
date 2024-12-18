import math
import re

num = re.compile('(\d+)')

def parse_file(filename):
    with open(filename, 'r') as f:
        registers,prog =  f.read().split('\n\n')
        registers = registers.splitlines()
        a = int(num.search(registers[0]).group(1))
        b = int(num.search(registers[1]).group(1))
        c = int(num.search(registers[2]).group(1))

        _, prog = prog.split(':')
        prog = list(map(int, prog.split(',')))
        
        return a, b, c, prog


def combo(a,b,c,arg):
    if arg < 4:
        return arg
    elif arg == 4:
        return a
    elif arg == 5:
        return b
    elif arg == 6:
        return c
    print(f'ERR received combo operand 7')


def part1(filename, debug=False):
    a, b, c, prog = parse_file(filename)
    ans = []
    ip = 0
    while True:
        if ip >= len(prog):
            break
        op = prog[ip]
        arg = None
        if ip +1 < len(prog):
            arg = prog[ip+1]
        if op == 0:
            a = a // int(math.pow(2, combo(a,b,c,arg)))
        elif op == 1:
            b = b ^ arg
        elif op == 2:
            b = combo(a,b,c,arg) % 8
        elif op == 3:
            if a != 0:
                ip = arg
                continue
        elif op == 4:
            b = b ^ c
        elif op == 5:
            ans.append(combo(a,b,c,arg)%8)
            if debug:
                print(f'{a}:{b}:{c} ans: {ans}')
        elif op == 6:
            b = a // int(math.pow(2, combo(a,b,c,arg)))
        elif op == 7:
            c = a // int(math.pow(2, combo(a,b,c,arg)))
        else:
            print(f'ERR unknown opcode {op}')
        ip += 2

    print(f'P1 {filename}: {",".join(map(str, ans))}')


def part2(filename):
    _, b, c, prog = parse_file(filename)
    target = list(reversed(prog))
    options = set([0])
    for x in target:
        # print(f'looking for {x} in {len(options)}')
        next = set()
        for cur in options:
            for a in range(cur, cur+8):
                b = a%8
                b = b^1
                c = a // int(math.pow(2,b))
                b = b^c
                b = b^4
                # # a = a // 8
                # print(a, b%8)
                if b%8 == x:
                    # print(f'must divide down to {a}')
                    next.add(a*8)
        if len(next) == 0:
            print(f'failed at {x}')
            return False
        options = next
    print(f'P2 {filename}: {min(map(lambda x: x // 8, options))}')


part1('example.txt')
part1('input.txt')

part2('input.txt')

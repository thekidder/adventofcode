from collections import defaultdict
import sys

def parse(s):
    return defaultdict(int, [(i,x) for i,x in enumerate(map(int, s.strip().split(',')))])


def get_address(relative_base, addr, mode):
    if mode == 0:
        return addr
    elif mode == 2:
        return addr + relative_base
    else:
        print(f'INVALID ADDR MODE {mode}')


def load(memory, relative_base, ptr, mode):
    if ptr >= len(memory):
        print(f'PTR ERR {mode} {ptr}')
        return None
    addr = memory[ptr]
    if mode == 0:
        if addr < 0:
            print(f'ADDR ERR {mode} {ptr} {addr}')
            return None
        return memory[addr]
    elif mode == 1:
        return addr
    elif mode == 2:
        addr += relative_base
        if addr < 0:
            print(f'ADDR ERR {mode} {ptr} {addr}')
            return None
        return memory[addr]
    else:
        print(f'INVALID PARAMETER MODE {mode}')


def run(memory,get_input,debug):
    cnt = 0
    relative_base = 0
    while True:
        instr = memory[cnt]
        op = instr % 100
        instr //= 100
        modes = []
        for i in range(3):
            modes.append(instr % 10)
            instr //= 10

        if op == 1:
            if debug:
                print(modes,'ADD ',memory[cnt+1],memory[cnt+2],memory[cnt+3])
            if cnt+3 >= len(memory):
                print('ERROR NO MEMORY')
                return None
            p1 = load(memory, relative_base, cnt+1, modes[0])
            p2 = load(memory, relative_base, cnt+2, modes[1])
            output = get_address(relative_base, memory[cnt+3], modes[2])
            if p1 is None:
                print(f'ERROR INVALID P1 ADDRESS {cnt+1} (mode {modes[0]})')
                return None
            if p2 is None:
                print(f'ERROR INVALID P2 ADDRESS {cnt+2} (mode {modes[1]})')
                return None
            memory[output] = p1 + p2
            cnt += 4
        elif op == 2:
            if debug:
                print(modes,'MULT',memory[cnt+1],memory[cnt+2],memory[cnt+3])
            if cnt+3 >= len(memory):
                print('ERROR NO MEMORY')
                return None
            p1 = load(memory, relative_base, cnt+1, modes[0])
            p2 = load(memory, relative_base, cnt+2, modes[1])
            output = get_address(relative_base, memory[cnt+3], modes[2])
            if p1 is None:
                print(f'ERROR INVALID P1 ADDRESS {cnt+1} {modes[0]}')
                return None
            if p2 is None:
                print(f'ERROR INVALID P2 ADDRESS {cnt+2} {modes[1]}')
                return None
            memory[output] = p1 * p2
            cnt += 4
        elif op == 3:
            output = get_address(relative_base, memory[cnt+1], modes[0])
            if debug:
                print(modes,'LOAD', output)
            i = next(get_input)
            memory[output] = i
            cnt += 2
        elif op == 4:
            p1 = load(memory, relative_base, cnt+1, modes[0])
            if debug:
                print(f'OUTPUT {p1}')
            yield p1
            cnt += 2
        elif op == 5:
            if debug:
                print(modes,'JMPT',i, memory[cnt+1],memory[cnt+2])
            p1 = load(memory, relative_base, cnt+1, modes[0])
            p2 = load(memory, relative_base, cnt+2, modes[1])
            if p1 != 0:
                cnt = p2
            else:
                cnt += 3
        elif op == 6:
            if debug:
                print(modes,'JMPF',i, memory[cnt+1],memory[cnt+2])
            p1 = load(memory, relative_base, cnt+1, modes[0])
            p2 = load(memory, relative_base, cnt+2, modes[1])
            if p1 == 0:
                cnt = p2
            else:
                cnt += 3
        elif op == 7:
            if debug:
                print(modes,'LESS',i, memory[cnt+1],memory[cnt+2],memory[cnt+3])
            p1 = load(memory, relative_base, cnt+1, modes[0])
            p2 = load(memory, relative_base, cnt+2, modes[1])
            output = get_address(relative_base, memory[cnt+3], modes[2])
            if p1 < p2:
                memory[output] = 1
            else:
                memory[output] = 0
            cnt += 4
        elif op == 8:
            if debug:
                print(modes,'EQUL',i, memory[cnt+1],memory[cnt+2],memory[cnt+3])
            p1 = load(memory, relative_base, cnt+1, modes[0])
            p2 = load(memory, relative_base, cnt+2, modes[1])
            output = get_address(relative_base, memory[cnt+3], modes[2])
            if p1 == p2:
                memory[output] = 1
            else:
                memory[output] = 0
            cnt += 4
        elif op == 9:
            p1 = load(memory, relative_base, cnt+1, modes[0])
            relative_base += p1
            if debug:
                print(f'RELATIVE BASE NOW {relative_base} (adj. by {p1})')
            cnt += 2
        elif op == 99:
            break
        else:
            print(f'ERROR INVALID OPCODE {op}')
            return None

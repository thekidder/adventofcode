import sys

def parse(s):
    return [x for x in map(int, s.strip().split(','))]


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


def run(memory,input,debug):
    cnt = 0
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
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 is None or p2 is None:
                return None
            memory[memory[cnt+3]] = p1 + p2
            cnt += 4
        elif op == 2:
            if debug:
                print(modes,'MULT',memory[cnt+1],memory[cnt+2],memory[cnt+3])
            if cnt+3 >= len(memory):
                print('ERROR NO MEMORY')
                return None
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 is None or p2 is None:
                return None
            memory[memory[cnt+3]] = p1 * p2
            cnt += 4
        elif op == 3:
            if debug:
                print(modes,'LOAD',len(input), memory[cnt+1])
            if len(input) == 0:
                print('ERROR NO INPUT')
                sys.exit(1)
            i = input.pop(0)
            memory[memory[cnt+1]] = i
            cnt += 2
        elif op == 4:
            if debug:
                print(modes,'STOR',memory[cnt+1])
            p1 = load(memory, cnt+1, modes[0])
            if debug:
                print(f'OUTPUT {p1}')
            yield p1
            cnt += 2
        elif op == 5:
            if debug:
                print(modes,'JMPT',i, memory[cnt+1],memory[cnt+2])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 != 0:
                cnt = p2
            else:
                cnt += 3
        elif op == 6:
            if debug:
                print(modes,'JMPF',i, memory[cnt+1],memory[cnt+2])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 == 0:
                cnt = p2
            else:
                cnt += 3
        elif op == 7:
            if debug:
                print(modes,'LESS',i, memory[cnt+1],memory[cnt+2],memory[cnt+3])
            p1 = load(memory, cnt+1, modes[0])
            p2 = load(memory, cnt+2, modes[1])
            if p1 < p2:
                memory[memory[cnt+3]] = 1
            else:
                memory[memory[cnt+3]] = 0
            cnt += 4
        elif op == 8:
            if debug:
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

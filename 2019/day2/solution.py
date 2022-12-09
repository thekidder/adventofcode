import sys

def parse_file(filename):
    with open(filename, 'r') as f:
        return [x for x in map(int, f.read().split(','))]


def load(memory, ptr):
    if ptr >= len(memory):
        return None
    addr = memory[ptr]
    if addr >= len(memory):
        return None
    return memory[addr]

    
def run(memory):
    cnt = 0
    while True:
        op = memory[cnt]
        if op == 1:
            if cnt+3 >= len(memory):
                print('ERROR')
                return None
            p1 = load(memory, cnt+1)
            p2 = load(memory, cnt+2)
            if p1 is None or p2 is None:
                return None
            memory[memory[cnt+3]] = p1 + p2
            cnt += 4
        elif op == 2:
            if cnt+3 >= len(memory):
                print('ERROR')
                return None
            p1 = load(memory, cnt+1)
            p2 = load(memory, cnt+2)
            if p1 is None or p2 is None:
                return None
            memory[memory[cnt+3]] = p1 * p2
            cnt += 4
        elif op == 99:
            break
        else:
            print('ERROR {op}')
            return None

    return memory


def part1(filename):
    input = parse_file(filename)
    input = run(input)
    ans = input[0]
    print(f'P1 {filename}: {ans}')


def part2(filename):
    original_input = parse_file(filename)
    for noun in range(100):
        for verb in range(100):
            input = original_input[:]
            input[1] = noun
            input[2] = verb
            input = run(input)
            if input is None:
                continue
            if input[0] == 19690720:
                print(f'P2 {filename}: {noun*100+verb}')
                sys.exit(0)


# part1('example.txt')
# part1('input.txt')

part2('example.txt')
part2('input.txt')

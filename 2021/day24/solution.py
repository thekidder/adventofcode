import copy
import sys

registers = set(['x','y','w','z'])

def parse_code(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            ins = line.strip().split()
            if len(ins) == 3 and ins[2] not in registers:
                ins[2] = int(ins[2])

            lines.append(ins)

    return lines


def parse(state, val):
    if val in registers:
        return state[val]
    return val


def execute(state, instruction):
    if instruction[0] == 'inp':
        state[instruction[1]] = state['input'].pop(0)
    elif instruction[0] == 'add':
        state[instruction[1]] = parse(state, instruction[1]) + parse(state, instruction[2])
    elif instruction[0] == 'mul':
        state[instruction[1]] = parse(state, instruction[1]) * parse(state, instruction[2])
    elif instruction[0] == 'div':
        state[instruction[1]] = int(parse(state, instruction[1]) / parse(state, instruction[2]))
    elif instruction[0] == 'mod':
        state[instruction[1]] = parse(state, instruction[1]) % parse(state, instruction[2])
    elif instruction[0] == 'eql':
        state[instruction[1]] = 1 if parse(state, instruction[1]) == parse(state, instruction[2]) else 0


def encode(input, s):
    return {'input':[input],'x':s[0],'y':s[1],'z':s[2],'w':s[3]}

def decode(s):
    return (s['x'],s['y'],s['z'],s['w'])

def part1():
    code = parse_code('code.txt')
    # state = {'input':[],'x':0,'y':0,'z':0,'w':0}
    state = (0,0,0,0)

    universes = {
        state: []
    }

    for digit in range(14):
        next = dict()
        code_index = -1
        for i in range(1,10):
            print(f'DIGIT {digit} i {i} l {len(universes)}')
            for s,d in universes.items():
                state = encode(i, s)

                for j,ins in enumerate(code):
                    if ins[0] == 'inp' and len(state['input']) == 0:
                        code_index = j
                        break
                    execute(state, ins)

                n = decode(state)
                if n not in next:
                    next[n] = d + [i]
                elif int(''.join([str(c) for c in next[n]])) < int(''.join([str(c) for c in d + [i]])):
                    next[n] = d + [i]
        universes = next
        code = code[code_index:]

    for s,d in universes.items():
        if s[2] == 0:
            print(d)

                
        
    #         if check_model(state, input, code):
    #             print(f'SUCCESS FOR {"".join(input)} at {state}')
    #             sys.exit(0)
    #             # break
    #         print(state)
    #         if z is None:
    #             z = state['z']
    #         elif digit not in digits and z != state['z']:
    #             digits.append(digit)
    #         # model -= 1
    # print(digits)


def check_model(state, input, code):
    if any([x == 0 for x in input]):
        return False

    # print(input)

    state['input'] = input
    state['x'] = 0
    state['y'] = 0
    state['w'] = 0
    state['z'] = 0

    for line in code:
        execute(state, line)
    if state['z'] == 0:
        print(input,state)
        return True
    return False


def part2(filename):
    pass


def run(state, code):
    for line in code:
        execute(state, line)
    print(state)


# code = parse_code('28.txt')
# state = {'input':[3,5],'x':0,'y':0,'z':0,'w':0}
# run(state, code)

# code = parse_code('code.txt')
# state = {'input':[],'x':0,'y':0,'z':0,'w':0}
# print(check_model(state, [int(c) for c in '92171126131911'], code))

part1()

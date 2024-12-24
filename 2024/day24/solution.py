import re
pattern = re.compile('(\w+) (AND|OR|XOR) (\w+) -> (\w+)')

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        wires, gates = lines.split('\n\n')

        wires = wires.split('\n')
        wires = { w.split(':')[0]:int(w.split(':')[1]) for w in wires }

        g = []
        for gate in gates.split('\n'):
            m = pattern.match(gate) 
            g.append((m.group(1), m.group(3), m.group(2), m.group(4)))

        return wires,g


def get_num(wires, prefix):
    wires = reversed(sorted([(k,v) for k,v in wires.items() if k[0] == prefix]))
    
    bits = ''
    for bit in wires:
        bits += str(bit[1])

    return int(bits, 2)


def sim(wires, gates):
    while len(gates):
        for i,g in enumerate(gates):
            in1, in2, op, out = g

            if in1 in wires and in2 in wires:
                if op == 'AND':
                    wires[out] = wires[in1] & wires[in2]
                elif op == 'OR':
                    wires[out] = wires[in1] | wires[in2]
                elif op == 'XOR':
                    wires[out] = wires[in1] ^ wires[in2]
                else:
                    print('ERR')
                del gates[i]
                break
                
    return get_num(wires, 'z')


def part1(filename):
    wires,gates = parse_file(filename)
    ans = sim(wires,gates)

    print(f'P1 {filename}: {ans}')


def replace(gates, a, b):
    for i,g in enumerate(gates):
        in1,in2,op,out = g
        if in1 == a:
            in1 = b
        if in2 == a:
            in2 = b
        if out == a:
            out = b
        gates[i] = (in1,in2,op,out)
    # print(f'replaced {a} with {b}')


def matches_gate(want_op, want_in1, want_in2, i, j, g):
    in1,in2,op,_ = g
    ins = sorted([in1, in2])
    in1 = ins[0]
    in2 = ins[1]
    if in1 == want_in1 + str(i).zfill(2) and in2 == want_in2 + str(j).zfill(2) and op == want_op:
        return True
    return False


def get_gate(want_op, want_in1, want_in2, i, j, gates):
    for g in gates:
        if matches_gate(want_op, want_in1, want_in2, i, j, g):
            return g


def build_adder(wires, gates):
    for i in range(45):
        if i > 0:
            g = get_gate('XOR', 'x', 'y', i, i, gates)
            if g is None:
                break
            replace(gates, g[3], 'i' + str(i).zfill(2))

            g = get_gate('AND', 'x', 'y', i, i, gates)
            if g is None:
                break
            replace(gates, g[3], 'j' + str(i).zfill(2))
        else:
            g = get_gate('AND', 'x', 'y', i, i, gates)
            if g is None:
                break
            replace(gates, g[3], 'l' + str(i).zfill(2))

        if i > 0:
            g = get_gate('AND', 'i', 'l', i, i-1, gates)
            if g is None:
                break
            replace(gates, g[3], 'k' + str(i).zfill(2))

        if i > 0 and i < 44:
            g = get_gate('OR', 'j', 'k', i, i, gates)
            if g is None:
                break
            replace(gates, g[3], 'l' + str(i).zfill(2))

    # if we break early need to manually go in and find inconsistent outputs to swap

    # for g in gates:
    #     print(g)
    x = get_num(wires, 'x')
    y = get_num(wires, 'y')

    # if we did everything right these should match
    print(x+y) 
    print(sim(wires,gates))


def part2(filename):
    wires,gates = parse_file(filename)
    ans = build_adder(wires,gates)

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('input.txt')

from collections import defaultdict
import re
# BBB = (DDD, EEE)
pattern = re.compile('(\w+) = \((\w+), (\w+)\)')

def parse_file(filename):
    r = []
    with open(filename, 'r') as f:
        lines = f.read()
        sections = lines.split('\n\n')
        instructions = sections[0].strip()

        nodes = sections[1].split('\n')
        for l in nodes:
            m = pattern.match(l)
            r.append((m[1], (m[2], m[3])))

        return instructions, dict(r)


def part1(filename):
    ins, nodes = parse_file(filename)
    print(nodes)
    ans = 0
    node = 'AAA'
    while node != 'ZZZ':
        n = ins[ans % len(ins)]
        if n == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        ans += 1
    print(f'P1 {filename}: {ans}')


def to_ind(c):
    if c == 'L':
        return 0
    return 1

cycles = defaultdict(int)

def get_cycle(n, ins, nodes):
    global cycles
    orig = n
    while n[2] != 'Z':
        ind = ins[cycles[orig] % len(ins)]
        n = nodes[n][ind]
        cycles[orig] += 1
        print(cycles)


def part2BAD(filename):
    global cycles
    ins, nodes = parse_file(filename)
    ins = list(map(to_ind, ins))
    # print(nodes)
    node = []
    # dests = {}
    for n in nodes.keys():
        if n[2] == 'A':
            node.append(n)

    for n in node:
        get_cycle(n, ins, nodes)

    next_nodes = {}

    print(cycles)

    for n in nodes.keys():
        orig = n
        next_nodes[n] = [n]
        for i in range(max(cycles.values())):
            ind = ins[i % len(ins)]
            n = nodes[n][ind]
            next_nodes[orig].append(n)
    
    print(next_nodes)

    ans = 0
    nsteps = 0
    while not all(map(lambda n: n[2] == 'Z', node)):
        print(node)
        for n in node:
            if cycles[n] == 0:
                get_cycle(n, ins, nodes)
        steps = [cycles[n] for n in node]
        min_steps = max(steps)
        for i in range(len(node)):
            node[i] = next_nodes[node[i]][min_steps]
        ans += min_steps
        nsteps += 1
        if nsteps % 1000000 == 0:
            print(ans)



    # ans = 1
    # for v in cycles.values():
    #     ans *= v
    
    # while not all(map(lambda n: n[2] == 'Z', node)):
    #     n = ins[ans % len(ins)]
    #     for i, nn in enumerate(node):
    #         node[i] = nodes[nn][n]
    #     ans += 1
    #     if ans % 1000000 == 0:
    #         print(ans)
    print(f'P2 {filename}: {ans}')


# def build_map(node, nodes, ins):
#     next = []
#     for ind in ins:
#         node = nodes[node][ind]
#         next.append(node)
#     return next

def next_z(node, nodes, ins, mod):
    i = mod
    while node[2] != 'Z':
        ind = ins[i % len(ins)]
        node = nodes[node][ind]
        i += 1
        # print(node)
    return i - mod


def sim(node, nodes, ins, mod, iterations):
    history = [0] * iterations
    i = mod
    while i < iterations + mod:
        ind = ins[i % len(ins)]
        history[i-mod] = node
        i += 1
        node = nodes[node][ind]
    return history

def part2(filename):
    ins, nodes = parse_file(filename)
    ins = list(map(to_ind, ins))
    ans = 0
    node = []

    node = []
    for n in nodes.keys():
        if n[2] == 'A':
            node.append(n)

    max_z = 18157
    sims = {}
    for n in nodes.keys():
        print(n)
        for i in range(len(ins)):
            sims[(n, i)] = sim(n, nodes, ins, i, max_z)

    print('calc next z...')

    next_zs = {}
    max_z = 0
    for n in nodes.keys():
        for i in range(len(ins)):
            next_zs[(n, i)] = next_z(n, nodes, ins, i)


    # print(next)
    # for i in range(len(ins)):
    #     su
    while not all(map(lambda n: n[2] == 'Z', node)):
        mod = ins[ans % len(ins)]
        min_steps = []
        for n in node:
            min_steps.append(next_zs[(n,mod)])
        steps = max(min_steps)
        ans += steps
        for i in range(node):
            node[i] = sims[(node[i], mod)]
        print(ans, node)
    print(f'P2 {filename}: {ans}')


def p(filename):
    ins, nodes = parse_file(filename)
    ins = list(map(to_ind, ins))
    ans = 0
    node = []

    node = []
    max_z= {}
    for n in nodes.keys():
        orig = n
        last = 0
        if n[2] == 'A':
            i = 0
            while n[2] != 'Z':
                idx = ins[i % len(ins)]
                n = nodes[n][idx]
                i += 1
            max_z[orig] = i
    print(max_z)
    ans = 1
    for n in max_z.values():
        print(n%len(ins), n, len(ins))
        ans *= n

    print(f'P2 {filename}: {ans}')


# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
# not 20216105529489301725275989
# not 20216105529489301725275989
# not 63813912189311648
# not 234609971284234
# 13830919117339
p('example.txt')
# p('input.txt')

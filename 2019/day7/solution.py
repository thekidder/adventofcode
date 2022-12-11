from intcode import *

import itertools

def parse_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def build_amp(prog, phase):
    prog = prog[:]
    input = [phase]
    def run_amp():
        for out in run(prog, input, False):
            yield out
    return run_amp(), input


def run_amp(programs):
    v = 0
    while True:
        for prog, input in programs:
            input.append(v)
            try:
                v = prog.__next__()
            except StopIteration:
                return v


def solve(prog_txt, phase):
    input = parse(prog_txt)
    m = 0
    for candidate in itertools.permutations(phase):
        programs = list(map(lambda x: build_amp(input, x), candidate))
        m = max(m, run_amp(programs))
    print(f'solve with phase {phase}: {m}')


solve('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', range(0,5))
solve(parse_file('input.txt'), range(0,5))

solve('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', range(5,10,1))
solve('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10', range(5,10,1))
solve(parse_file('input.txt'), range(5,10,1))

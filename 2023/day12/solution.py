import functools
import re

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            springs, constraints = line.split()
            lines.append((springs, tuple(map(int, constraints.split(',')))))

    return lines


maybe_damage = re.compile('^[\#\?]*')
@functools.cache
def num_matches(input):
    p,c = input
    if len(c) == 0:
        return 1 if '#' not in p else 0
        
    if len(p) == 0:
        return 0

    need = c[0]
    next_damage = maybe_damage.match(p).span()[1]
    
    r = 0

    if p[0] != '#':
        r += num_matches((p[1:], c))

    if next_damage >= need:
        if len(p) == need or p[need] != '#':
            r += num_matches((p[need+1:], c[1:]))
    return r



def solve(filename, expand = False):
    input = parse_file(filename)
    if expand:
        input = map(lambda input: ('?'.join([input[0]] * 5), input[1]*5), input)

    ans = sum(map(num_matches, input))
    part = 'P2' if expand else 'P1'
    print(f'{part} {filename}: {ans}')


solve('example.txt')
solve('input.txt')

solve('example.txt', expand = True)
solve('input.txt', expand = True)

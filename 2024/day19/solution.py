import bisect
import functools

def parse_file(filename):
   with open(filename, 'r') as f:
        lines = f.read()
        towels, designs = lines.split('\n\n')
        towels = list(map(lambda x: x.strip(), towels.split(',')))
        return sorted(towels), designs.split()


def solve(filename):
    towels, designs = parse_file(filename)
    p1_ans = p2_ans = 0

    @functools.cache
    def can_make(design, partial = ''):
        r = 0
        if design == '':
            return 1
        pos = bisect.bisect_left(towels, design[:1])
        for i in range(pos, len(towels)):
            t = towels[i]
            if t > design:
                break
            if design[:len(t)] == t:
                r += can_make(design[len(t):], partial + t)
        return r

    for d in designs:
        r = can_make(d, '')
        p1_ans += min(r, 1)
        p2_ans += r

    print(f'{filename}: P1 {p1_ans} P2 {p2_ans}')


solve('example.txt')
solve('input.txt')

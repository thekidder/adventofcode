from collections import defaultdict
import re

def file(name):
    with open(name, 'r') as f:
        return f.read()


def parse_file(filename):
    return list(map(lambda x: x.strip(), file(filename).split(',')))


def hash(str):
    r = 0
    for c in str:
        r += ord(c)
        r *= 17
        r = r % 256
    return r


def part1(filename):
    input = parse_file(filename)
    ans = sum(map(hash, input))
    print(f'P1 {filename}: {ans}')


pattern = re.compile('^(\w+)([=-])(\d*)')

def part2(filename):
    input = parse_file(filename)
    data = defaultdict(list)
    for i in input:
        m = pattern.match(i)

        label = m.group(1)
        box = hash(label)
        op = m.group(2)
        if op == '=':
            focal = int(m.group(3))
            found = False
            for i, (l,f) in enumerate(data[box]):
                if l == label:
                    data[box][i] = (label, focal)
                    found = True
                    break
            if not found:
                data[box].append((label, focal))

        else:
            for i, (l,f) in enumerate(data[box]):
                if l == label:
                    data[box].pop(i)
                    break
    ans = 0
    for box, lenses in data.items():
        for i, (_, focal) in enumerate(lenses):
            ans += (box + 1) * (i + 1) * focal
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

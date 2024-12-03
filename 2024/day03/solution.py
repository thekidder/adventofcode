import re


pattern = re.compile('mul\((\d+),(\d+)\)')
pattern2 = re.compile('(?:mul\((\d+),(\d+)\))|(?:do\(\))|(?:don\'t\(\))')

def parse_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def part1(filename):
    input = parse_file(filename)
    ans = 0
    for m in pattern.findall(input):
        ans += int(m[0]) * int(m[1])
    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file(filename)
    ans = 0
    enabled = True
    for m in pattern2.finditer(input):
        if m.group(0) == 'don\'t()':
            enabled = False
        elif m.group(0) == 'do()':
            enabled = True
        else:
            if enabled:
                ans += int(m.group(1)) * int(m.group(2))
    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example2.txt')
part2('input.txt')

def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.split())

    return lines


def sc(round):
    if ord(round[0]) - ord('A') == ord(round[1]) - ord('X'):
        return 3
    if round[1] == 'X' and round[0] == 'C':
        return 6
    if round[1] == 'Y' and round[0] == 'A':
        return 6
    if round[1] == 'Z' and round[0] == 'B':
        return 6
    return 0


def part1(filename):
    print(filename)
    score = 0
    input = parse_file(filename)
    for round in input:
        score += (ord(round[1]) - ord('X')) + 1
        score += sc(round)

    print(f'ANSWER: {score}\n')


def sc2(round):
    if round[1] == 'Y':
        return (ord(round[0]) - ord('A') + 1) + 3
    if round[1] =='X':
        if round[0] == 'A':
            return 3
        if round[0] == 'B':
            return 1
        if round[0] == 'C':
            return 2

    if round[0] == 'A':
        return 2 + 6
    if round[0] == 'B':
        return 3 + 6
    if round[0] == 'C':
        return 1 + 6


def part2(filename):
    print(filename)
    score = 0
    input = parse_file(filename)
    for round in input:
        score += sc2(round)

    print(f'ANSWER: {score}\n')


part2('example.txt')
part2('input.txt')

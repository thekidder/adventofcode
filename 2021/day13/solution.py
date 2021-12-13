from collections import defaultdict

def parse_file(filename):
    max_x = 0
    max_y = 0
    folds = []
    with open(filename, 'r') as f:
        grid = defaultdict(bool)
        for line in f:
            if ',' in line:
                pos = tuple(map(int, line.split(',')))
                grid[pos] = True
                max_x = max(pos[0], max_x)
                max_y = max(pos[1], max_y)
            if '=' in line:
                line = line.split('=')
                if 'x' in line[0]:
                    folds.append(('x', int(line[1])))
                else:
                    folds.append(('y', int(line[1])))

    board = []
    for y in range(max_y+1):
        line = []
        for x in range(max_x+1):
            line.append(grid[(x,y)])

        board.append(line)


    return board,folds


def do_fold(input, fold):
    pos = fold[1]
    if fold[0] == 'x':
        for x in range(pos):
            for y in range(len(input)):
                input[y][pos - x - 1] = input[y][pos - x - 1] | input[y][pos + x + 1]
        for line in input:
            del line[pos:]
    else:
        for y in range(pos):
            for x in range(len(input[0])):
                input[pos - y - 1][x] = input[pos - y - 1][x] | input[pos + y + 1][x]
        del input[pos:]


def part1(filename):
    input,folds = parse_file(filename)
    ans = 0

    fold = folds[0]
    do_fold(input, fold)

    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x]:
                ans += 1

    print(f'ANSWER: {ans}')


def part2(filename):
    global max_x,max_y
    input,folds = parse_file(filename)

    for fold in folds:
        do_fold(input, fold)

    for line in input:
        print(''.join(map(lambda x: '#' if x else ' ', line)))


part2('input.txt')

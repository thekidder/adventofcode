def parse_file(filename):
    r = []
    id = 0
    with open(filename, 'r') as f:
        lines = f.read()
        for i,c in enumerate(map(int, lines)):
            if i % 2 == 0:
                for _ in range(c):
                    r.append(id)
                id += 1
            else:
                for _ in range(c):
                    r.append(None)
    return r


def parse_file2(filename):
    r = []
    id = 0
    pos = 0
    with open(filename, 'r') as f:
        lines = f.read()
        for i,c in enumerate(map(int, lines)):
            if i % 2 == 0:
                r.append((pos, id, c))
                id += 1
                pos += c
            else:
                pos += c
    return r


def last(li):
    for i in reversed(range(len(li))):
        if li[i] is not None:
            return i


def part1(filename):
    input = parse_file(filename)

    while True:
        try:
            gap = input.index(None)
            m = last(input)
            if gap >= m:
                break
            input[gap] = input[m]
            input[m] = None
        except:
            break

    ans = 0
    for i,x in enumerate(input):
        if x is not None:
            ans += i*x

    print(f'P1 {filename}: {ans}')


def part2(filename):
    input = parse_file2(filename)
    id = input[-1][1]

    for id in reversed(range(id+1)):
        ind = next((i for i,x in enumerate(input) if x[1] == id), None)
        pos,id,ln = input[ind]

        for i in range(ind):
            gap_start = input[i][0] + input[i][2]
            gap_size = input[i+1][0] - gap_start
            if gap_size >= ln:
                del input[ind]
                input.insert(i+1, (gap_start, id, ln))
                break

    ans = 0
    for pos,id,ln in input:
        for offset in range(ln):
            ans += (pos + offset) * id

    print(f'P2 {filename}: {ans}')


part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt') 

def parse_file(filename):
    tree = {}
    with open(filename, 'r') as f:
        input = f.readlines()
        stack = []      
        while len(input) > 0:
            command = input[0][2:].strip()
            input = input[1:]
            if command.startswith('ls'):
                while len(input) > 0 and not input[0].startswith('$'):
                    file = input[0]
                    store(tree, stack, file)
                    input = input[1:]
            elif command.startswith('cd'):
                dir = command[2:].strip()
                if dir == '/':
                    stack = []
                elif dir == '..':
                    stack.pop()
                else:
                    stack.append(dir)
            else:
                print('ERROR')
    return tree


def size(tree):
    s = 0
    for k,v in tree.items():
        if type(v) is dict:
            s += size(v)
        else:
            s += v
    return s


def store(tree, stack, file):
    ptr = tree
    stack = stack[:]
    while len(stack) > 0:
        ptr = ptr[stack.pop(0)]

    if file.startswith('dir'):
        file = file[4:].strip()
        ptr[file] = {}
    else:
        size, name = file.split(' ')
        ptr[name.strip()] = int(size)


def calc_p1(tree):
    ans = 0
    for v in tree.values():
        if type(v) is dict:
            s = size(v)
            if s < 100000:
                ans += s
            ans += calc_p1(v)
    return ans


def calc_p2(tree, min, used):
    needed = 30000000 - (70000000 - used)
    for v in tree.values():
        if type(v) is dict:
            s = size(v)
            if s >= needed and (min == -1 or s < min):
                min = s
            min = calc_p2(v, min, used)
    return min


def part1(filename):
    tree = parse_file(filename)
    ans = calc_p1(tree)
    print(f'P1 {filename}: {ans}')


def part2(filename):
    tree = parse_file(filename)
    used = size(tree)
    ans = calc_p2(tree, -1, used)
    print(f'P2 {filename}: {ans}')

part1('example.txt')
part1('input.txt')

part2('example.txt')
part2('input.txt')

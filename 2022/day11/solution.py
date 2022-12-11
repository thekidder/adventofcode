import operator

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        monkies = lines.split('\n\n')
        r = []
        for monkey in monkies:
            lines = monkey.split('\n')
            items = []
            if len(lines[1][18:]) > 0:
                items = list(map(int, lines[1][18:].split(',')))
            op,arg = lines[2][23:].split(' ')
            if op == '*':
                op = operator.mul
            else:
                op = operator.add
            test = int(lines[3][21:])
            true_monkey = int(lines[4][29:])
            false_monkey = int(lines[5][29:])
            r.append({
                'items': items,
                'op': op,
                'arg': arg,
                'test': test,
                'true_monkey': true_monkey,
                'false_monkey': false_monkey,
                'inspected': 0,
            })

        return r


def part1(filename):
    input = parse_file(filename)
    print(input)
    for r in range(20):
        for i in range(len(input)):
            while len(input[i]['items']) > 0:
                input[i]['inspected'] += 1
                item = input[i]['items'].pop(0)
                if input[i]['arg'] =='old':
                    item = input[i]['op'](item, item)
                else:
                    item = input[i]['op'](item, int(input[i]['arg']))
                item //= 3
                if item % input[i]['test'] == 0:
                    input[input[i]['true_monkey']]['items'].append(item)
                else:
                    input[input[i]['false_monkey']]['items'].append(item)
    for i, m in enumerate(input):
        print(i, m['inspected'])


def mod(input):
    m = 1
    for i in range(len(input)):
        m *= input[i]['test']
    return m

def part2(filename):
    input = parse_file(filename)
    total_m = mod(input)

    print(input)
    for r in range(10000):
        for i in range(len(input)):
            while len(input[i]['items']) > 0:
                input[i]['inspected'] += 1
                item = input[i]['items'].pop(0)
                if input[i]['arg'] =='old':
                    item = input[i]['op'](item, item)
                else:
                    item = input[i]['op'](item, int(input[i]['arg']))
                item = item % total_m
                if item % input[i]['test'] == 0:
                    input[input[i]['true_monkey']]['items'].append(item)
                else:
                    input[input[i]['false_monkey']]['items'].append(item)
    print(f'round {r}')
    for i, m in enumerate(input):
        print(i, m['inspected'])


# part1('example.txt')
# part1('input.txt')

# part2('example.txt')
part2('input.txt')

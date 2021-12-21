def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append([int(c) for c in line.strip()])

    return lines


dirs = [
    (-1, 0), 
    (0, -1), (0, 1),
    (1, 0),
]

def neighbors(grid, pos):
    x,y = pos
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
            yield (nx,ny)


def map_cost(grid, enter, exit):
    costs = {
        enter: 0
    }

    open = set([enter])

    while len(open) > 0:
        pos = open.pop()
        cost = costs[pos]
        for nx,ny in neighbors(grid, pos):
            ncost = cost + grid[ny][nx]
            if (nx,ny) not in costs or ncost < costs[(nx,ny)]:
                costs[(nx,ny)] = ncost
                open.add((nx,ny))
    
    return costs[exit]


def part1(filename):
    input = parse_file(filename)
    enter = (0,0)
    exit = (len(input[0]) - 1, len(input) - 1)

    print(f'ANSWER: {map_cost(input, enter, exit)}')


def add_cost(cost):
    return cost + 1 if cost < 9 else 1


def transform_line(input):
    return map(add_cost, input)


def build_map(input):
    output = []
    for y in range(5):
        for line in input:
            output_line = []
            for x in range(5):
                output_line.extend(line)
                line = [x for x in transform_line(line)]
            output.append(output_line)
        for i in range(len(input)):
            input[i] = [x for x in transform_line(input[i])]

    return output


def part2(filename):
    input = parse_file(filename)
    input = build_map(input)
    enter = (0,0)
    exit = (len(input[0]) - 1, len(input) - 1)

    print(f'ANSWER: {map_cost(input, enter, exit)}')


part2('input.txt')

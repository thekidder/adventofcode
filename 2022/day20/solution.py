def parse_file(filename, key):
    r = []
    with open(filename, 'r') as f:
        return list(map(lambda l: int(l)*key, f.readlines()))


def solve(filename, iterations, key):
    input = parse_file(filename, key)
    indices = list(range(len(input)))
    
    print(f'Initial arrangement:\n{input}')
    for i in range(iterations):
        for x in range(len(input)):
            ind = indices.index(x)
            val = input.pop(ind)

            next_ind = (ind + val) % len(input)
            if val != 0 and next_ind == 0:
                next_ind = len(input)
            elif next_ind == len(input):
                next_ind = 0

            input.insert(next_ind, val)

            indices.pop(ind)
            indices.insert(next_ind, x)
        print(f'After {i+1} round of mixing:\n{input}')
        print(indices)

    
    ind = input.index(0)
    ans = input[(ind + 1000) % len(input)] + \
        input[(ind + 2000) % len(input)] + \
        input[(ind + 3000) % len(input)]
    print(f'Mix {filename} {iterations} time(s): {ans}')


# solve('example.txt', 1, 1)
# solve('input.txt', 1, 1)

solve('example.txt', 10, 811589153)
# solve('input.txt', 10, 811589153)

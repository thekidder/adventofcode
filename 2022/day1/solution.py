import functools

def parse_file(filename):
    with open(filename, 'r') as f:
        return [
            [x for x in map(int, l.split('\n'))] 
            for l in f.read().split('\n\n')
        ]

def solution(filename):
    cals = [functools.reduce(lambda a,b: a+b, x) for x in parse_file(filename)]
    cals.sort()
    print(cals[-1])
    print(functools.reduce(lambda a,b: a+b, cals[-3:]))

solution('example.txt')
solution('input.txt')

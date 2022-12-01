def grouped_input(filename, parse_func):
    with open(filename, 'r') as f:
        return [
            [x for x in map(parse_func, l.split('\n'))] 
            for l in f.read().split('\n\n')
        ]

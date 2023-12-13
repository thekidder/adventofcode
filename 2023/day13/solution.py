def parse_grid(text):
    r = {}
    mx = 0
    my = 0
    f = text.split('\n')
    for (y, l) in enumerate(f):
        my = y
        for (x, c) in enumerate(l.strip()):
            r[(x,y)] = c
            mx = x

    return r,mx,my


def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read()
        grids = lines.split('\n\n')
        return list(map(parse_grid, grids))


def is_mirror_col(grid,mx,my,col,nfaults=0):
    faults = 0
    ncols = min(col, mx - col + 1)
    for i in range(ncols):
        for y in range(my+1):
            if grid[(col-i-1,y)] != grid[(col+i,y)]:
                faults += 1
    return faults == nfaults


def is_mirror_row(grid,mx,my,row,nfaults=0):
    faults = 0
    nrows = min(row, my - row + 1)
    for i in range(nrows):
        for x in range(mx+1):
            if grid[(x,row-i-1)] != grid[(x,row+i)]:
                faults += 1
    return faults == nfaults


def pattern(input, nfaults):
    grid,mx,my = input
    for col in range(1, mx+1):
        if is_mirror_col(grid,mx,my,col,nfaults):
            return col
    for row in range(1, my+1):
        if is_mirror_row(grid,mx,my,row,nfaults):
            return row * 100
    return 0

def solve(filename):
    input = parse_file(filename)
    ans = sum(map(lambda i: pattern(i, 0), input))
    print(f'P1 {filename}: {ans}')

    ans = sum(map(lambda i: pattern(i, 1), input))
    print(f'P1 {filename}: {ans}')


solve('example.txt')
solve('input.txt')

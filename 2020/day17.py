import collections
import math

def neighbors(pos):
  for i in range(pos[0]-1, pos[0]+2):
    for j in range(pos[1]-1, pos[1]+2):
      for k in range(pos[2]-1, pos[2]+2):
        for l in range(pos[3]-1, pos[3]+2):
          coord = (i, j, k, l)
          if coord == pos:
            continue
          yield coord


def patch(grid):
  x = [math.inf, -math.inf]
  y = [math.inf, -math.inf]
  z = [math.inf, -math.inf]
  w = [math.inf, -math.inf]

  for pos in grid.keys():
    x[0] = min(x[0], pos[0])
    x[1] = max(x[1], pos[0])
    y[0] = min(y[0], pos[1])
    y[1] = max(y[1], pos[1])
    z[0] = min(z[0], pos[2])
    z[1] = max(z[1], pos[2])
    w[0] = min(w[0], pos[3])
    w[1] = max(w[1], pos[3])

  for i in range(x[0]-1, x[1]+2):
    for j in range(y[0]-1, y[1]+2):
      for k in range(z[0]-1, z[1]+2):
        for l in range(w[0]-1, w[1]+2):
          coord = (i, j, k, l)
          if coord not in grid:
            grid[coord] = False

def step(grid):
  patch(grid)
  next_grid = collections.defaultdict(bool)
  for pos,active in grid.items():
    cnt = 0
    for neighbor in neighbors(pos):
      if neighbor in grid and grid[neighbor]:
        cnt += 1
    if active and (cnt == 2 or cnt == 3):
        next_grid[pos] = True
    elif not active and (cnt == 3):
      next_grid[pos] = True
    else:
      next_grid[pos] = False
  return next_grid


def run(filename):
  grid = collections.defaultdict(bool)
  with open(filename, 'r') as f:
    y = 0
    for line in f:
      line = line.strip()
      for x in range(len(line)):
        pos = (x, y, 0, 0)
        if line[x] == '#':
          grid[pos] = True
        else:
          grid[pos] = False
      y += 1

  for i in range(6):
    grid = step(grid)
  cnt = 0
  for pos,active in grid.items():
    if active:
      cnt += 1
  print(cnt)

# run('day17_ex.txt')
run('day17.txt')
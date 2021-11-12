import math

map = []
w = 0
h = 0

def parse(line):
  global w, h, map
  lw = len(map)
  for letter in line:
    map.append(letter)
  lw = len(map) - lw
  if lw != w and w != 0:
    print('unequal map width!')
  w = lw
  h += 1

with open('day11.txt', 'r') as f:
  for line in f:
    parse(line.strip())


def fromindex(i):
  return (i % w, math.floor(i / w))

def toindex(coord):
  (x, y) = coord
  return y * w + x

def valid(coord):
  return coord[0] >= 0 and coord[0] < w and coord[1] >= 0 and coord[1] < h

def neighbors(idx, m):
  (x, y) = fromindex(idx)

  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      coord = (x+i,y+j)
      while valid(coord) and m[toindex(coord)] == '.':
        coord = (coord[0]+i,coord[1]+j)
      if valid(coord):
        yield toindex(coord)


def printmap(m):
  for idx in range(len(m)):
    if idx % w == 0:
      print()
    print(m[idx], end='')
  print()

def iterate(m):
  n = []
  print('iterate...')
  for idx in range(len(m)):
    if m[idx] == '.':
      n.append('.')
      continue
    ncnt = 0
    for nidx in neighbors(idx, m):
      if m[nidx] == '#':
        ncnt += 1
    if m[idx] == 'L' and ncnt == 0:
      n.append('#')
    elif m[idx] == '#' and ncnt >= 5:
      n.append('L')
    else:
      n.append(m[idx])
  return n

prev = map.copy()
curr = iterate(prev)
while curr != prev:
  prev = curr
  curr = iterate(prev)

cnt = 0
for letter in curr:
  if letter == '#':
    cnt += 1

print(cnt)



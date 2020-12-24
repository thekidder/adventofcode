import collections
import math

from copy import copy

debug = False

valid_directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']


# coords are (row, col)
# “odd-r” horizontal layout
# https://www.redblobgames.com/grids/hexagons/
def neighbor(coord, direction):
  if direction == 'e':
    return (coord[0]+1, coord[1])
  elif direction == 'w':
    return (coord[0]-1, coord[1])
  elif direction == 'ne':
    x = coord[0]
    if coord[1] % 2 == 1:
      x += 1
    return (x, coord[1]-1)
  elif direction == 'nw':
    x = coord[0]
    if coord[1] % 2 == 0:
      x -= 1
    return (x, coord[1]-1)
  elif direction == 'se':
    x = coord[0]
    if coord[1] % 2 == 1:
      x += 1
    return (x, coord[1]+1)
  else:
    x = coord[0]
    if coord[1] % 2 == 0:
      x -= 1
    return (x, coord[1]+1)

def tile_neighbors(coord):
  for d in valid_directions:
    yield neighbor(coord, d)

def parse_direction(directions):
  coord = (0, 0)
  for direction in directions:
    coord = neighbor(coord, direction)

  return coord

def next_day(tiles):
  min_coords = [math.inf, math.inf] # row, col
  max_coords = [-math.inf, -math.inf]
  for coord in tiles.keys():
    min_coords[0] = min(min_coords[0], coord[0])
    min_coords[1] = min(min_coords[1], coord[1])

    max_coords[0] = max(max_coords[0], coord[0])
    max_coords[1] = max(max_coords[1], coord[1])

  min_coords[0] -= 2
  min_coords[1] -= 2
  max_coords[0] += 2
  max_coords[1] += 2

  debug and print(min_coords, max_coords)

  next_day_tiles = copy(tiles)

  for r in range(min_coords[0], max_coords[0]+1):
    for c in range(min_coords[1], max_coords[1]+1):
      coord = (r, c)

      cnt = 0
      for n in tile_neighbors(coord):
        if tiles[n]:
          cnt += 1

      if tiles[coord] and (cnt == 0 or cnt > 2):
        next_day_tiles[coord] = False
      elif not tiles[coord] and cnt == 2:
        next_day_tiles[coord] = True

  return next_day_tiles


def tile_count(tiles):
  cnt = 0
  for v in tiles.values():
    if v:
      cnt += 1
  return cnt

def run(filename):
  with open(filename, 'r') as f:
    is_tile_black = collections.defaultdict(bool)
    for line in f:
      line = line.strip()
      directions = []
      current_direction = ''
      for c in line:
        current_direction += c
        if current_direction in valid_directions:
          directions.append(current_direction)
          current_direction = ''
      coord = parse_direction(directions)
      print(directions, coord)
      is_tile_black[coord] = not is_tile_black[coord]
  print(is_tile_black)
  print(tile_count(is_tile_black))
  for i in range(100):
    is_tile_black = next_day(is_tile_black)
    print(f'{i+1}: {tile_count(is_tile_black)}')


# run('day24_ex.txt')
run('day24.txt')
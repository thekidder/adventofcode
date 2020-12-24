import collections
import functools
import math

from copy import copy

debug = False

valid_directions = {
  # axial coords, +x = e, +y = se
  # https://www.redblobgames.com/grids/hexagons/
  'e':  [ 1,  0],
  'w':  [-1,  0],
  'ne': [ 1, -1],
  'nw': [ 0, -1],
  'se': [ 0,  1],
  'sw': [-1,  1],
}


# coords are (row, col)
# “odd-r” horizontal layout
def neighbor(coord, direction):
  return tuple(map(sum, zip(coord, valid_directions[direction])))

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
    min_coords = [min(a, b-1) for a, b in zip(min_coords, coord)]
    max_coords = [max(a, b+1) for a, b in zip(max_coords, coord)]

  debug and print(min_coords, max_coords)

  next_day_tiles = copy(tiles)

  for r in range(min_coords[0], max_coords[0]+1):
    for c in range(min_coords[1], max_coords[1]+1):
      coord = (r, c)
      cnt = functools.reduce(lambda a, v: a + int(tiles[v]), [n for n in tile_neighbors(coord)], 0)

      if tiles[coord] and (cnt == 0 or cnt > 2):
        next_day_tiles[coord] = False
      elif not tiles[coord] and cnt == 2:
        next_day_tiles[coord] = True

  return next_day_tiles


def tile_count(tiles):
  return functools.reduce(lambda a, v: a + int(v), tiles.values(), 0)

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
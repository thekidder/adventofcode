import collections
import functools
import math
import re
import sys

directions = [
  0, # top
  1, # right
  2, # bottom
  3, # left
]

opposites = [
  2, # top
  3, # right
  0, # bottom
  1, # left
]

def coord_with_direction(coord, direction):
  (x, y) = coord
  if direction == 0:
    return (x, y+1)
  elif direction == 1:
    return (x-1, y)
  elif direction == 2:
    return (x, y-1)
  else:
    return (x+1, y)

w = 10
h = 10

def fromindex(i, w, h):
  return (i % w, math.floor(i / w))

def toindex(coord, w, h):
  (x, y) = coord
  return y * w + x

def edgematches(e1, e2):
  return e1 == e2 or e1 == list(reversed(e2))

def rotate(l, n):
  return l[n:] + l[:n]

def printtiles(tiles, key):
  for idx, tile in tiles.items():
    print(f'{idx}: {tile[key]}')

def missing_orientations(tiles):
  for tile in tiles.values():
    if 'orientation' not in tile:
      return True
  return False

def rotate(img, w, h):
  rotated = ['.'] * (w * h)
  for y in range(h):
    for x in range(w):
      coord = (h-y-1, x)
      rotated[toindex(coord, w, h)] = img[toindex((x, y), w, h)]
  return rotated

def flipy(img, w, h):
  flipped = ['.'] * (w * h)
  for y in range(h):
    for x in range(w):
      coord = (x, h-y-1)
      flipped[toindex(coord, w, h)] = img[toindex((x, y), w, h)]
  return flipped

def flipx(img, w, h):
  flipped = ['.'] * (w * h)
  for y in range(h):
    for x in range(w):
      coord = (w-x-1, y)
      flipped[toindex(coord, w, h)] = img[toindex((x, y), w, h)]
  return flipped

def permutations(img, w, h):
  for i in range(8):
    n = img[:]
    for j in range(i%4):
      n = rotate(n, w, h)
    if i > 3:
      n = flipx(n, w, h)
    if i % 2 == 1:
      n = flipy(n, w, h)
    yield n



def print_img(img, tile_size, size):
  total_size = tile_size*size
  img = flipy(img, total_size, total_size)
  for y in range(total_size):
    for x in range(total_size):
      print(img[toindex((x, y), total_size, total_size)], end='')
      if x > 0 and x % tile_size == tile_size-1:
        print(' ', end='')
    print('')
    if y > 0 and y % tile_size == tile_size-1:
      print('')

def draw_tile(img, tile, x, y, w, h, s):
  for i in range(w*h):
    (xp, yp) = fromindex(i, w, h)
    coord = (x*w+xp, y*h+yp)
    img[toindex(coord, s * w, s * h)] = tile[i]
  # for i in range(w):
  #   row = row_from_edge(tile, 3, i)

  #   for j in range(len(row)):
  #     coord = (x*w+i, y*h+j)
  #     img[toindex(coord, s * w, s * h)] = row[j]


def find_matching(tiles, used_tiles, row, w, h, direction):
  for idx, t in tiles.items():
    if idx in used_tiles:
      continue
    for permutation in permutations(t['tile'], w, h):
      if row == row_from_edge(permutation, direction, 0):
        return permutation, idx
  return None, None

def neighbor_cnt(tile):
  cnt = 0
  for direction in directions:
    if len(tile['possible_neighbors'][direction]) > 0:
      cnt += 1
  return cnt

def has_dir(tile, direction):
  return len(tile['possible_neighbors'][direction]) > 0

def row_from_edge(tile, direction, idx):
  row = []
  if direction == 0:
    for x in range(w):
      row.append(tile[toindex((x, idx), w, h)])
    return row
  elif direction == 1:
    for y in range(h):
      row.append(tile[toindex((w - idx - 1, y), w, h)])
    return row
  elif direction == 2:
    for x in range(w):
      row.append(tile[toindex((x, h - idx - 1), w, h)])
    return row
  else:
    for y in range(h):
      row.append(tile[toindex((idx, y), w, h)])
    return row

def run(filename):
  with open(filename, 'r') as f:
    tile_id = None
    tile = []
    tiles = {}
    for line in f:
      line = line.strip()
      m = re.match('Tile (\d+):', line)
      if m is not None:
        tile_id = int(m.groups()[0])
      else:
        if len(line) == 0:
          tiles[tile_id] = {'tile': tile}
          tile = []
        tile.extend(line)

    tiles[tile_id] = {'tile': tile}

  for idx, tile in tiles.items():
    tile['edges'] = [[], [], [], []]
    tile['possible_neighbors'] = collections.defaultdict(list)
    for x in range(w):
      tile['edges'][0].append(tile['tile'][toindex((x, 0), w, h)])
      tile['edges'][2].append(tile['tile'][toindex((x, h - 1), w, h)])
    for y in range(h):
      tile['edges'][1].append(tile['tile'][toindex((w-1, y), w, h)])
      tile['edges'][3].append(tile['tile'][toindex((0, y), w, h)])

  print(tiles)

  for idx, tile in tiles.items():
    for direction in directions:
      for idx2, tile2 in tiles.items():
        if idx == idx2:
          break
        for direction2 in directions:
          if edgematches(tile['edges'][direction], tile2['edges'][direction2]):
            if (idx2, direction2) not in tile['possible_neighbors'][direction]:
              tile['possible_neighbors'][direction].append((idx2, direction2))
            if (idx, direction) not in tile2['possible_neighbors'][direction2]:
              tile2['possible_neighbors'][direction2].append((idx, direction))

  for idx, tile in tiles.items():
    print(f'{idx}: {tile["possible_neighbors"]}')


  dirty = True
  while dirty:
    dirty = False
    for idx, tile in tiles.items():    
      for direction in directions:
        if len(tile['possible_neighbors'][direction]) == 1:
          removal = tile['possible_neighbors'][direction][0]
          for idx2, tile2 in tiles.items():
            if idx == idx2:
              break
            for direction2 in directions:
              if removal in tile2['possible_neighbors'][direction2]:
                dirty = True
                tile2['possible_neighbors'][direction2] = [n for n in tile2['possible_neighbors'][direction2] if n != removal]

  first = None

  cnt = 1
  sanity = 0
  for idx, tile in tiles.items():
    num_sides = 0
    for v in tile["possible_neighbors"].values():
      num_sides += int(bool(len(v)))
    if num_sides == 2:
      cnt *= idx
      sanity += 1
    print(f'{idx}, {num_sides}: {tile["possible_neighbors"]}')
  print(cnt, sanity)

  # first_idx = 0
  # for idx, tile in tiles.items():
  #   neighbors = []
  #   for d, v in tile["possible_neighbors"].items():
  #     if len(v) > 0:
  #       neighbors.append(d)
  #   neighbors.sort()
  #   if neighbors == [1, 2]:
  #     first = tile
  #     first_idx = idx


  # print(first_idx)

  s = int(math.sqrt(len(tiles.keys())))
  img = []
  for i in range(s*s*w*h):
    img.append('.')




  # draw_tile(img, first['tile'], 0, 0, w, h, s)
  # print_img(img, w*s, h*s)

  # used_tiles = set([first_idx])

  # row_first = first['tile']
  # for j in range(s):
  #   last = row_first
  #   if j > 0:
  #     r = row_from_edge(row_first, 2, 0)
  #     (last, last_idx) = find_matching(tiles, used_tiles, r, w, h, 0)
  #     row_first = last
  #     draw_tile(img, last, 0, j, w, h, s)
  #     used_tiles.add(last_idx)
  #   for i in range(s-1):
  #     r = row_from_edge(last, 1, 0)
  #     (tile, idx) = find_matching(tiles, used_tiles, r, w, h, 3)
  #     draw_tile(img, tile, i+1, j, w, h, s)
  #     last = tile
  #     last_idx = idx
  #     used_tiles.add(last_idx)

  # print_img(img, w*s,h*s)

  started = False
  all_permutations = []
  for idx,t in tiles.items():
    if not started:
      all_permutations.append((idx, t['tile']))
      started = True
    else:
      for permutation in permutations(t['tile'], w, h):
        all_permutations.append((idx, permutation))

  arrangement = {}
  search = set()
  used_tiles = set()
  for x in range(0, s):
    for y in range(0, s):
      arrangement[(x,y)] = all_permutations[:]
      search.add((x,y))

  def matches_any(idx_a, perm_a, perms_b, direction):
    r = row_from_edge(perm_a, opposites[direction], 0)
    # print(f'{direction} -> {len(perms_b)}: {r}')
    for (idx_b, p_b) in perms_b:
      # print(f'{row_from_edge(p_b, opposites[direction], 0)}')
      if idx_a == idx_b:
        continue
      if r == row_from_edge(p_b, direction, 0):
        return True
    return False

  def matches_in_all_directions(coord, idx, perm):
    for direction in directions:
      neighbor = coord_with_direction(coord, direction)
      if neighbor in arrangement:
        if not matches_any(idx, perm, arrangement[neighbor], direction):
          return False
    return True

  while len(search):
    coord = search.pop()
    if coord not in arrangement:
      continue
    orig_len = len(arrangement[coord])
    arrangement[coord] = [p for p in arrangement[coord] if matches_in_all_directions(coord, p[0], p[1])]
    if len(arrangement[coord]) != orig_len:
      for direction in directions:
        search.add(coord_with_direction(coord, direction))
    print(f'{coord} len: {len(arrangement[coord])}')

  for (x,y) in arrangement:
    print(f'{x},{y} len: {len(arrangement[(x,y)])}')


  for (x,y) in arrangement:
    print(f'{arrangement[(x,y)]}')
    draw_tile(img, arrangement[(x,y)][0][1], x, y, w, h, s)
  print_img(img, w, s)

  def fix_img(img, tile_size, num_tiles):
    fixed_tile_size = tile_size-2
    fixed = ['.'] * fixed_tile_size*fixed_tile_size*num_tiles*num_tiles

    for x in range(num_tiles):
      for y in range(num_tiles):
        for xt in range(fixed_tile_size):
          for yt in range(fixed_tile_size):
            tocoord = (xt+x*fixed_tile_size,yt+y*fixed_tile_size)
            fromcoord = (xt+x*tile_size+1,yt+y*tile_size+1)
            fixed[toindex(tocoord, num_tiles*fixed_tile_size, num_tiles*fixed_tile_size)] = img[toindex(fromcoord, num_tiles*tile_size, num_tiles*tile_size)]

    return fixed

  img = fix_img(img, w, s)
  img_size = (w-2)*s
  print_img(img, (w-2), s)
  sea_monster = [
    (18,2),
    (0,1),
    (5,1),
    (6,1),
    (11,1),
    (12,1),
    (17,1),
    (18,1),
    (19,1),
    (1,0),
    (4,0),
    (7,0),
    (10,0),
    (13,0),
    (16,0),
  ]


  def has_sea_monster(img, size):
    for x in range(size-19):
      for y in range(size-2):
        found = True
        for (xx, yy) in sea_monster:
          coord = (x+xx,y+yy)
          if img[toindex(coord, size, size)] != '#':
            found = False
            break
        if found:
          return True
    return False

  def draw_sea_monsters(img, size):
    for x in range(size-19):
      for y in range(size-2):
        found = True
        for (xx, yy) in sea_monster:
          coord = (x+xx,y+yy)
          if img[toindex(coord, size, size)] != '#':
            found = False
            break
        if found:
          for (xx, yy) in sea_monster:
            coord = (x+xx,y+yy)
            img[toindex(coord, size, size)] = 'O'
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

  for perm in permutations(img, img_size, img_size):
    if has_sea_monster(perm, img_size):
      print('sea monster!')
      img = perm
      break


  draw_sea_monsters(img, img_size)
  print_img(img, (w-2), s)

  cnt = 0
  for i in range(img_size*img_size):
    if img[i] == '#':
      cnt += 1
  print(cnt)


  # first_idx = list(tiles.keys())[0]
  # arrangement = {(0,0): {'tile': tiles[first_idx]['tile'], 'idx': first_idx}}
  # used_tiles = set([first_idx])
  # search = []
  # for direction in directions:
  #   search.append( ((0,0),direction) )

  # while len(used_tiles) < len(tiles) and len(search) > 0:
  #   (coord,direction) = search.pop()
  #   print(coord)
  #   tile = arrangement[coord]['tile']
  #   r = row_from_edge(tile, direction, 0)
  #   (tile, idx) = find_matching(tiles, used_tiles, r, w, h, opposites[direction])
  #   if tile is not None and idx is not None:
  #     used_tiles.add(idx)
  #     coord = coord_with_direction(coord, direction)
  #     arrangement[coord] = {'tile': tile, 'idx': idx}
  #     for direction in directions:
  #       if coord_with_direction(coord, direction) not in arrangement:
  #         search.append( (coord,direction) )
  #   print(arrangement.keys())

  # min_x = math.inf
  # min_y = math.inf
  # for (x, y) in arrangement.keys():
  #   min_x = min(min_x, x)
  #   min_y = min(min_y, y)

  # print(min_x, min_y)

  # for x in range(min_x, min_x+s):
  #   for y in range(min_y, min_y+s):
  #     coord = (x,y)
  #     draw_tile(img, arrangement[coord]['tile'], x-min_x, y-min_y, w, h, s)
  # print_img(img, w*s, h*s)




  # tile = first
  # last = None
  # last_down = None
  # last_row = None
  # down = 2
  # right = 1
  # flip_x = False
  # flip_y = False
  # cnt = 0
  # print(first['possible_neighbors'])
  # if not has_dir(first, down):
  #   down = 0
  #   flip_y = True
  # if not has_dir(first, right):
  #   down = 0
  #   flip_x = True
  # for y in range(s):
  #   tile = first
  #   last_down = None
  #   last = None
  #   for i in range(y):
  #     idx = tile['possible_neighbors'][down][0][0]
  #     tile = tiles[idx]

  #     if last_down is not None and last_row != row_from_edge(tile, opposites[down], 0):
  #       flip_y = True
  #       down = opposites[last_down['possible_neighbors'][down][0][1]]
  #     if neighbor_cnt(tile) == 2:
  #       for direction in directions:
  #         if direction != down and has_dir(tile, direction):
  #           print('COR right to ' + str(right))
  #           right = direction
  #           break
  #     else:
  #       for direction in directions:
  #         if not has_dir(tile, direction):
  #           print('MID right to ' + str(right))
  #           right = opposites[direction]
  #           break

  #     last_down = tile      
  #     last_row = row_from_edge(last_down, down, 0)

  #   for x in range(s):
  #     print(f'X {x}')
  #     for i in range(x):
  #       print(tile['possible_neighbors'], right)
  #       idx = tile['possible_neighbors'][right][0][0]
  #       tile = tiles[idx]

  #     if last is not None:
  #       print(last['possible_neighbors'][right][0])
  #       last_row = row_from_edge(last, right, 0)
  #       right = opposites[last['possible_neighbors'][right][0][1]]
        
  #     print(last_row)
  #     print(row_from_edge(tile, opposites[right], 0))
  #     if last is not None and last_row != row_from_edge(tile, opposites[right], 0):
  #       flip_x = True

  #     for i in range(w):
  #       row = row_from_edge(tile, opposites[right], i)
  #       if flip_x:
  #         row.reverse()

  #       for j in range(len(row)):
  #         coord = (x*w+i, y*h+j)
  #         img[toindex(coord, s * w, s * h)] = row[j]
  #     last = tile
  #     print(flip_x, flip_y)
  #     print_img(img, w*s, h*s)

  #     cnt += 1
  #     if cnt == 6:
  #       sys.exit(0)
  #   last = None
  # sys.exit(0)


  # while missing_orientations(tiles):
  #   for tile in tiles.values():
  #     if 'orientation' not in tile:
  #       continue
  #     for direction in directions:
  #       if len(tile['possible_neighbors'][direction]) == 0:
  #         continue
  #       (neighbor_idx, direction2) = tile['possible_neighbors'][direction][0]
  #       neighbor_tile = tiles[neighbor_idx]
  #       rot = (direction - opposites[direction2]) % 4
  #       neighbor_tile['orientation'] = rotate([0, 1, 2, 3], rot)
  #       if 

  # printtiles(tiles, 'orientation')







# run('day20_ex.txt')
run('day20.txt')
import math

x = 0
y = 0

wx = 10
wy = 1

# def toquadrant():
#   global wx, wy
#   if wx >=0 and wy >= 0:
#     return 0
#   elif wx >= 0 and wy < 0:
#     return 3
#   elif wx < 0 and wy >= 0:
#     return 1
#   else:
#     return 2

# def fromquadrant(q):
#   global wx, wy
#   if q == 0:
#     wx = math.fabs(wx)
#     wy = math.fabs(wy)
#   elif q == 1:
#     wx = -math.fabs(wx)
#     wy = math.fabs(wy)
#   elif q == 2:
#     wx = -math.fabs(wx)
#     wy = -math.fabs(wy)
#   else:
#     wx = math.fabs(wx)
#     wy = -math.fabs(wy)

def dir_to_coord(dir):
  if dir == 0:
    return (1, 0)
  elif dir == 1:
    return (0, 1)
  elif dir == 2:
    return (-1, 0)
  elif dir == 3:
    return (0, -1)
  else:
    print('HELP')
    return (0, 0)

def rotate(f, deg):
  global wx, wy
  # quadrant = toquadrant()
  if f == 'L':
    for i in range(deg // 90):
      ox = wx
      wx = -wy
      wy = ox
    # return (quadrant + (deg / 90)) % 4
  else:
    for i in range(deg // 90):
      ox = wx
      wx = wy
      wy = -ox

def parse(line):
  global facing, x, y, wx, wy
  action = line[:1]
  val = int(line[1:])
  if action == 'N':
    wy += val
  elif action == 'S':
    wy -= val
  elif action == 'E':
    wx += val
  elif action == 'W':
    wx -= val
  elif action == 'F':
    # (xi, yi) = dir_to_coord(facing)
    # x += xi * val
    # y += yi * val
    x += wx * val
    y += wy * val
  else:
    # print('BQ ' + str(toquadrant()) )
    rotate(action, val)
    # print('Q ' + str(q) )
    # fromquadrant(q)

with open('day12.txt', 'r') as f:
  for line in f:
    parse(line.strip())
    print(wx, wy)
    print(x, y)

print(x, y)

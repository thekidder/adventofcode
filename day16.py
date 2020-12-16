import re

def validf(f, field):
  if (f >= field[0] and f <= field[1]) or (f >= field[2] and f <= field[3]):
    return True
  return False


def valid(f, fields):
  for field in fields:
    if (f >= field[0] and f <= field[1]) or (f >= field[2] and f <= field[3]):
      return True
  return False

def collapsed(possibilities):
  for p in possibilities:
    if len(p) > 1:
      return False
  return True

def run(filename):
  ticket = None
  nearby = []
  validtickets = []
  fields = []
  names = []

  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      # departure location: 50-688 or 707-966
      m = re.match('([\w\s]+)\: (\d+)-(\d+) or (\d+)-(\d+)', line)

      if m is not None:
        g = m.groups()
        name = g[0]
        names.append(name)
        for i in range(1, len(g), 4):
          # print(int(g[i]), int(g[i+1]))
          fields.append((int(g[i]), int(g[i+1]), int(g[i+2]), int(g[i+3])))

      elif len(line) == 0 or line.startswith('your ticket') or line.startswith('nearby tickets'):
        pass
      elif ticket is None:
        ticket = [int(f) for f in line.split(',')]
      else:
        nearby.append([int(f) for f in line.split(',')])
    print(fields)
    # print(ticket)
    # print(nearby)

  inv = 0
  for t in nearby:
    v = True
    for f in t:
      if not valid(f, fields):
        v = False
        break
    if v:
      validtickets.append(t)
  print(validtickets)

  ticketlen = len(ticket)

  possibilities = []
  for p in range(ticketlen):
    possibilities.append([i for i in range(len(fields))])
  print(possibilities)
  for v in validtickets:
    for i in range(len(v)):
      f = v[i]
      print(f)
      for j in range(len(fields)):
        possible = fields[j]
        if not validf(f, possible):
          print(f'!! {f} not valid for {possible}')
          possibilities[i] = [p for p in possibilities[i] if p != j]
  print(possibilities)
  while not collapsed(possibilities):
    for i in range(len(possibilities)):
      possible = possibilities[i]
      if len(possible) == 1:
        for j in range(len(possibilities)):
          if i == j:
            continue
          possibilities[j] = [p for p in possibilities[j] if p != possible[0]]

  print(possibilities)
  mult = 1
  for i in range(len(possibilities)):
    idx = possibilities[i][0]
    print(f'{names[idx]} = {idx}: {ticket[i]}')
    if names[idx].startswith('departure'):
      print(ticket[i])
      mult *= ticket[i]
  print(mult)
# run('day16_ex.txt')
# run('day16_ex2.txt')
run('day16.txt')
def part1(t, busses):
  print('PART 1')
  bus = 0
  minb = None

  busses = [int(b) for b in busses.split(',') if b != 'x']
  for b in busses:
    i = 0
    while True:
      if (t + i) % b == 0:
        if minb is None or t + i < minb:
          minb = t + i
          bus = b
        break
      i += 1

  print((minb - t) * bus)


def part2(line):
  print('PART 2')
  busses = line.split(',')

  offsets = {}
  for i in range(len(busses)):
    if busses[i] == 'x':
      continue
    offsets[int(busses[i])] = i

  t = 0
  i = 0
  while True:
    if valid(t, offsets):
      print(f'found {t} after {i} iterations')
      break

    lcm = 1
    for bus,offset in offsets.items():
      if (t + offset) % bus == 0:
        lcm *= bus
    t += lcm
    i += 1


def valid(t, offsets):
  for bus,offset in offsets.items():
    if (t + offset) % bus != 0:
      return False
  return True


with open('day13.txt', 'r') as f:
  t = int(f.readline())
  binput = f.readline().strip()
  part1(t, binput)
  part2(binput)


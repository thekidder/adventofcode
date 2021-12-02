def part1():
  x = 0
  depth = 0
  with open('input.txt', 'r') as f:
    for row in f:
      line = row.strip().split(' ')

      direction = line[0].strip()
      amt = int(line[1])

      if direction == 'forward':
        x += amt
      elif direction == 'down':
        depth += amt
      elif direction == 'up':
        depth -= amt
      else:
        print('ERROR')

  print(f"x: {x} depth: {depth}; total: {x * depth}")

def part2():
  x = 0
  depth = 0
  aim = 0
  with open('input.txt', 'r') as f:
    for row in f:
      line = row.strip().split(' ')

      direction = line[0].strip()
      amt = int(line[1])

      if direction == 'forward':
        x += amt
        depth += aim * amt
      elif direction == 'down':
        aim += amt
      elif direction == 'up':
        aim -= amt
      else:
        print('ERROR')

  print(f"x: {x} depth: {depth}; total: {x * depth}")

part2()
import functools

def part1():
  last = None
  total = 0
  with open('input.txt', 'r') as f:
    for row in f:
      measurement = int(row.strip())

      if last is not None and measurement > last:
        total += 1

      last = measurement

  print(f"total increases: {total}")

def add(x,y): return x+y

def part2():
  last_window = []
  current_window = []
  total = 0
  with open('input.txt', 'r') as f:
    for row in f:
      measurement = int(row.strip())

      last_window = current_window[:]
      current_window.append(measurement)

      if len(current_window) > 3:
        current_window = current_window[1:]

      if len(current_window) == 3 and len(last_window) == 3:
        last_sum = functools.reduce(add, last_window)
        current_sum = functools.reduce(add, current_window)
        print(f"cur {current_sum} last {last_sum}")

        if current_sum > last_sum:
          total += 1

      last = measurement

  print(f"total increases: {total}")

part2()
    

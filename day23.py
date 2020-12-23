debug = False

def rotate(l, n):
  return l[n:] + l[:n]

def run(input):
  cups = [int(c) for c in input]
  min_cup = min(cups)
  max_cup = max(cups)

  cups.extend(range(max_cup+1, 1000001))
  max_cup = max(cups)
  debug and print(len(cups))

  cup_map = {}

  for i in range(len(cups)):
    cup = cups[i]
    prev_cup = None
    prev_cup = cups[i-1]
    next_cup = None
    if i < len(cups) - 1:
      next_cup = cups[i+1]
    else:
      next_cup = cups[0]
    cup_map[cup] = [prev_cup, next_cup]
  debug and print(cup_map)

  cur = cups[0]

  for i in range(10000000):
    debug and print(f'{i} BEGIN ({cur}): {cup_map}')
    # picked_up = [cups.pop(1) for i in range(3)]
    n = cup_map[cur][1]

    picked_up = []
    for j in range(3):
      picked_up.append(n)
      n = cup_map[n][1]
    cup_map[cur][1] = n
    cup_map[n][0] = cur

    debug and print(f'{i} CUR: {cur} PICKED UP: {picked_up}')
    dest = cur - 1
    while dest in picked_up or dest < min_cup:
      dest -= 1
      if dest < min_cup:
        dest = max_cup

    dest_n = cup_map[dest][1]

    for p in picked_up:
      cup_map[dest][1] = p
      cup_map[p][0] = dest
      dest = p

    cup_map[dest][1] = dest_n

    cur = n

    debug and print(f'{i} Next current - {cur}')

    if (i+1) % 100000 == 0:
      print(f'iteration {i+1}')

  el = 1
  if debug:
    for i in range(len(cups)-1):
      print(f'{cup_map[el][1]}', end='')
      el = cup_map[el][1]
    print()
  num = cup_map[1][1]
  debug and print(cup_map)
  print(num, cup_map[num][1], cup_map[num][1] * num)


# run('389125467') # example
run('643719258') # problem
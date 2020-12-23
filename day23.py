debug = False

def rotate(l, n):
  return l[n:] + l[:n]

def run(input):
  cups = [int(c) for c in input]
  min_cup = 1
  max_cup = len(cups)

  cups.extend(range(max_cup+1, 1000001))
  max_cup = len(cups)
  debug and print(len(cups))

  # map of number -> next number. essentially a linked list
  cup_map = {}

  for i in range(len(cups)):
    cup = cups[i]
    next_cup = None
    if i < len(cups) - 1:
      next_cup = cups[i+1]
    else:
      next_cup = cups[0]
    cup_map[cup] = next_cup
  debug and print(cup_map)

  cur = cups[0]

  for i in range(10000000):
    debug and print(f'{i} BEGIN ({cur}): {cup_map}')
    n = cup_map[cur]

    picked_up = []
    for j in range(3):
      picked_up.append(n)
      n = cup_map[n]
    cup_map[cur] = n

    debug and print(f'{i} CUR: {cur} PICKED UP: {picked_up}')
    dest = cur - 1
    while dest in picked_up or dest < min_cup:
      dest -= 1
      if dest < min_cup:
        dest = max_cup

    dest_n = cup_map[dest]

    for p in picked_up:
      cup_map[dest] = p
      dest = p

    cup_map[dest] = dest_n
    cur = n

    if (i+1) % 100000 == 0:
      print(f'iteration {i+1}')

  el = 1
  if debug:
    for i in range(len(cups)-1):
      print(f'{cup_map[el]}', end='')
      el = cup_map[el]
    print()
  num = cup_map[1]
  debug and print(cup_map)
  print(num, cup_map[num], cup_map[num] * num)


# run('389125467') # example
run('643719258') # problem
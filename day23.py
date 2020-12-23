debug = True

def rotate(l, n):
  return l[n:] + l[:n]

def run(input):
  cups = [int(c) for c in input]
  min_cup = min(cups)
  max_cup = max(cups)

  cups.extend(range(max_cup+1, 1000001))
  # debug and print(cups)

  pos = 0

  for i in range(1000):
    cur = cups[pos]
    picked_up = [cups[i%len(cups)] for i in range(pos+1, pos+4)]
    debug and print(f'{i} CUR: {cur} PICKED UP: {picked_up}')
    dest = cur - 1
    while dest in picked_up or dest < min_cup:
      dest -= 1
      if dest < min_cup:
        dest = max_cup

    debug and print(f'DEST {dest}')
    dest_pos = pos
    cnt = 0
    while cups[dest_pos] != dest:
      dest_pos = (dest_pos + 1) % len(cups)
      cups[dest_pos] = cups[(dest_pos + 3) % len(cups)]
      if pos == dest_pos + 3:
        pos = (pos - 3) % len(cups)
      cnt += 1

    for j in range(3):
      cups[(dest_pos+1+j)%len(cups)] = picked_up[j]

    pos = (pos + 1) % len(cups)

    debug and print(f'{i} STEP COMPLETE: cups[{pos}] = {cups[pos]} {cnt}')

    if (i+1) % 10 == 0:
      print(f'iteration {i+1}')

  one_cup = cups.index(1)
  cups = rotate(cups, one_cup)
  debug and print(''.join([str(c) for c in cups[1:]]))
  print(cups[1])
  print(cups[2])


run('389125467') # example
# run('643719258') # problem
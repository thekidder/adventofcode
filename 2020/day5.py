def parse(seat):
  row = seat[:7]
  col = seat[-3:]

  row = row.replace('F', '0')
  row = row.replace('B', '1')
  row = int(row, 2)

  col = col.replace('L', '0')
  col = col.replace('R', '1')
  col = int(col, 2)

  return (row, col, row * 8 + col)

highest = 0
all_ids = []
with open('day5.txt', 'r') as f:
  for line in f:
    line = line.strip()
    (row, col, sid) = parse(line)
    all_ids.append(sid)
    if sid > highest:
      highest = sid

all_ids = sorted(all_ids)
for i in range(1, len(all_ids) - 1):
  prev = all_ids[i-1]
  curr = all_ids[i]
  next = all_ids[i+1]

  if prev + 1 != curr or curr +1 != next:
    print(prev, curr, next)


print(highest)

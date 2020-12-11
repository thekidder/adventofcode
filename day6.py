
cnt = 0
group = []
with open('day6.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) == 0:
      print(group)
      common = group[0].intersection(*group[1:])
      print(len(common))
      cnt += len(common)
      group = []
    else:
      g = set()
      for q in line:
        g.add(q)
      group.append(g)

common = group[0].intersection(*group[1:])

cnt += len(common)
print(cnt)


map = []
with open('day3.txt', 'r') as f:
  for i, row in enumerate(f):
    # print(i, row)
    row = row.strip()
    map.append([])
    for col in row:
      # print(col)
      map[i].append(col == '#')
    print(map[i])

x = 3
y = 1

slopes = [
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2),
]

t = 1

for (x, y) in slopes:
  i = 0
  j = 0
  trees = 0
  while i < len(map):
    if map[i][j%len(map[i])]:
      trees+=1

    i += y
    j += x
  t *= trees

print(t)
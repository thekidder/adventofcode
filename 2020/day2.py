def check_valid(pw, letter, low, high):
  cnt = 0
  for x in pw:
    if x == letter:
      cnt += 1

  return cnt >= low and cnt <= high

# v = 0
# with open('day2.txt', 'r') as f:
#   for row in f:
#     row = row.strip()
#     components = row.split(':')
#     rule = components[0].split(' ')
#     pw = components[1].strip()
#     letter = rule[1]
#     constraint = rule[0].split('-')
#     low = int(constraint[0])
#     high = int(constraint[1])

#     if check_valid(pw, letter, low, high):
#       v +=1
#     # else:
#     #   if row != f'{low}-{high} {letter}: {pw}':
#     #     print(f'{low}-{high} {letter}: {pw}')

# print(v)

def check_valid2(pw, letter, a, b):
  return (pw[a-1] == letter or pw[b-1] == letter) and pw[a-1] != pw[b-1]

v = 0
with open('day2.txt', 'r') as f:
  for row in f:
    row = row.strip()
    components = row.split(':')
    rule = components[0].split(' ')
    pw = components[1].strip()
    letter = rule[1]
    constraint = rule[0].split('-')
    low = int(constraint[0])
    high = int(constraint[1])

    if check_valid2(pw, letter, low, high):
      v +=1
    # else:
    #   if row != f'{low}-{high} {letter}: {pw}':
    #     print(f'{low}-{high} {letter}: {pw}')

print(v)
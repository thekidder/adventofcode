import re

rules = {}

# vibrant purple bags contain 2 dotted tan bags, 1 wavy fuchsia bag, 5 plaid lime bags.
# light gold bags contain no other bags.
# wavy teal bags contain 4 muted olive bags, 2 muted purple bags.
def parse_rule(rule):
  rule = rule.strip()
  components = rule.split(' bags contain ', 1)
  bag_color = components[0]
  bag_rule = components[1]
  if bag_rule == 'no other bags.':
    rules[bag_color] = []
    return
  # print(bag_rule)
  rules[bag_color] = []
  for m in re.finditer('(\d+) ([a-z\s]+) bags?(?:, )?', bag_rule):
    tup = (int(m.group(1)), m.group(2))
    rules[bag_color].append(tup)

def contains(root, color):
  if len(rules[root]) == 0:
    return False
  for (num, c) in rules[root]:
    if c == color:
      return True
  for (num, c) in rules[root]:
    if contains(c, color):
      return True
  return False


def nested(root):
  if len(rules[root]) == 0:
    return 0
  total = 0
  for (num, c) in rules[root]:
    total += num * (1 + nested(c))
  return total

with open('day7.txt', 'r') as f:
  for line in f:
    parse_rule(line)

print(rules)
cnt = 0
for c in rules:
  # print('TESTING ' + c)
  if contains(c, 'shiny gold'):
    cnt += 1

print(cnt)
print(nested('shiny gold'))


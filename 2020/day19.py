valid_msgs = set()
rules = {}
msgs = []
all_prefixes = set()

def generate(remaining_rules, prefix=''):
  if prefix not in all_prefixes:
    return
  if len(remaining_rules) == 0:
    yield prefix
  else:
    first = remaining_rules[0]
    rule = rules[first]
      
    if isinstance(rule, list):
      for possibility in rule:
        for m in generate(possibility + remaining_rules[1:], prefix):
          yield m
    else:
      for m in generate(remaining_rules[1:], prefix + rule):
        yield m

def run(filename):
  global msgs
  with open(filename, 'r') as f:
    lines = f.read()
    c = lines.split('\n\n')
    rule_strs = c[0].split('\n')
    msgs = [m.strip() for m in c[1].split('\n')]

    for r in rule_strs:
      c = r.split(':')
      idx = int(c[0].strip())
      rule = c[1].strip()
      if '"' in rule:
        rules[idx] = rule.replace('"','')
      else:
        rules[idx] = [list(map(int, r.strip().split(' '))) for r in rule.strip().split('|')]

    longest_len = 0
    for m in msgs:
      if len(m) > longest_len:
        longest_len = len(m)

    # generate all possible permutations of prefixes of the messages
    all_prefixes.add('')
    for i in range(1, longest_len+1):
      for m in msgs:
        if len(m) >= i:
          all_prefixes.add(m[0:i])

    for m in generate([0]):
      valid_msgs.add(m)

    cnt = 0
    for m in msgs:
      if m in valid_msgs:
        cnt += 1
    print(cnt)

# run('day19_ex.txt')
run('day19.txt')
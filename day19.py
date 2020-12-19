# def valid(msg, rulemap):
  # pass

v = set()
rulemap = {}
msgs = []
all_prefixes = set()

def generate(rulelist, prefix=''):
  # print(f'GEN {prefix} {rulelist}')
  if prefix not in all_prefixes:
    # print('  (quit)')
    return
  if len(rulelist) == 0:
    yield prefix
  else:
    first = rulelist[0]
    rule = rulemap[first]
      
    if not isinstance(rule, list):
      # print('leaf ' + rule)
      for m in generate(rulelist[1:], prefix + rule):
        yield m
    else:
      for possibility in rule:
        # print(f'{rulelist[1:]} +++ {possibility}')
        for m in generate(possibility + rulelist[1:], prefix):
          yield m

def run(filename):
  global msgs
  with open(filename, 'r') as f:
    lines = f.read()
    c = lines.split('\n\n')
    rules = c[0].split('\n')
    msgs = [m.strip() for m in c[1].split('\n')]

    for r in rules:
      c = r.split(':')
      idx = int(c[0].strip())
      rule = c[1].strip()
      if '"' in rule:
        rulemap[idx] = rule.replace('"','')
      else:
        rulemap[idx] = [list(map(int, r.strip().split(' '))) for r in rule.strip().split('|')]
    print(rulemap)
    print(msgs)

    longest_len = 0
    for m in msgs:
      if len(m) > longest_len:
        longest_len = len(m)

    all_prefixes.add('')
    for i in range(1, longest_len+1):
      for m in msgs:
        if len(m) >= i:
          all_prefixes.add(m[0:i])



    for m in generate([0]):
      v.add(m)
    print('aaabbbbbbaaaabaababaabababbabaaabbababababaaa' in all_prefixes)

    print(len(v))
    print('~~~~')

    cnt = 0
    for m in msgs:
      if m in v:
        print(m)
        cnt += 1
    print(cnt)

# run('day19_ex.txt')
run('day19.txt')
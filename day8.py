import sys
prog = []

def parse_arg(arg):
  if arg.startswith('+'):
    return int(arg[1:])
  elif arg.startswith('-'):
    return -int(arg[1:])

def parse_op(line):
  parts = line.strip().split()
  op = parts[0].strip()
  arg = parse_arg(parts[1].strip())
  prog.append((op, arg))

with open('day8.txt', 'r') as f:
  for line in f:
    parse_op(line)

cngs = set()

while True:
  acc = 0
  idx = 0
  visited = set()
  changed = False

  print('RUNNING; ' + str(cngs))
  while idx not in visited:
    if idx == len(prog):
      print('terminate!')
      print(acc)
      sys.exit(0)
      break
    visited.add(idx)
    (op, arg) = prog[idx]
    print('exec ' + op + ', ' + str(arg))
    if op == 'acc':
      acc += arg
      idx += 1
    elif op == 'jmp':
      if idx not in cngs and not changed:
        cngs.add(idx)
        changed = True
        idx += 1
        print('change instruction ' + str(idx) + ' to nop')
      else:
        idx += arg
    elif op == 'nop':
      if idx not in cngs and not changed:
        changed = True
        cngs.add(idx)
        print('change instruction ' + str(idx) + ' to jmp')
        idx += arg
      else:
        idx += 1
    else:
      print('invalid instruction! ' + op + ', ' + str(arg))

  print('loop')
  print(acc)
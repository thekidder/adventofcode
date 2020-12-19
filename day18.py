import collections
import math

def calc(expr, indent = ''):
  print(f'{indent}CALC {expr}')

  i = 0
  # first simplify parens
  while i < len(expr):
    token = expr[i]
    if token == '(':
      j = i+1
      cnt = 1
      while j < len(expr) and cnt != 0:
        if expr[j] == '(':
          cnt += 1
        elif expr[j] == ')':
          cnt -= 1
        j += 1
      expr = expr[:i] + [calc(expr[i+1:j-1], indent + '  ')] + expr[j:]
    i += 1

  # next do addition
  i = 0
  while i < len(expr):
    token = expr[i]
    if token == '+':
      expr = expr[:i-1] + [int(expr[i-1]) + int(expr[i+1])] + expr[i+2:]
    else:
      i += 1

  # finally, mult
  i = 0
  while i < len(expr):
    token = expr[i]
    if token == '*':
      expr = expr[:i-1] + [int(expr[i-1]) * int(expr[i+1])] + expr[i+2:]
    else:
      i += 1

  print(f'{indent}CALC return {expr[0]}')
  return int(expr[0])


def tokenize(expr):
  expr = expr.strip().replace(' ', '')
  return [t for t in expr]


def run(filename):
  sum = 0
  with open(filename, 'r') as f:
    for line in f:
      r = calc(tokenize(line))
      sum += r
      print(r)

  print(sum)

run('day18.txt')
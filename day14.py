import re

mem = {}

def run(filename):
  with open(filename, 'r') as f:
    onesmask = 0
    notxmask = 0
    xmask = []
    for line in f:
      line = line.strip()
      if line.startswith('mask = '):
        onesmask = 0
        notxmask = 0
        xmask = []
        mask = line[-36:]
        print(mask)
        for i in range(len(mask)):
          bit = mask[-i - 1]
          if bit == '1':
            onesmask += 1 << i
          if bit != 'X':
            notxmask += 1 << i
          else:
            xmask.append(i)
      else:
        m = re.match('mem\[(\d+)\] \= (\d+)', line)
        g = m.groups()
        addr = int(g[0])
        val = int(g[1])

        maskaddr = (addr | onesmask) & notxmask
        all_addr(mem, val, maskaddr, xmask)

  s = 0
  for addr, val in mem.items():
    s += val
  print(mem)
  print(s)

def all_addr(mem, val, base, bits):
  if len(bits) == 0:
    return
  bits = bits[:]
  bit = bits.pop()
  mem[base] = val
  mem[base | (1 << bit)] = val
  all_addr(mem, val, base, bits)
  all_addr(mem, val, base | (1 << bit), bits)


# run('day14_ex.txt')
run('day14.txt')
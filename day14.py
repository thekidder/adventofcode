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
            # print(f'1 bit at {i}')
            onesmask += 1 << i
          if bit != 'X':
            # print(f'0 bit at {i}')
            notxmask += 1 << i
          else:
            xmask.append(i)

        # print(onesmask)
        # print(zerosmask)
      else:
        m = re.match('mem\[(\d+)\] \= (\d+)', line)
        g = m.groups()
        addr = int(g[0])
        val = int(g[1])

        maskaddr = (addr | onesmask) & notxmask
        all_addr(mem, val, maskaddr, xmask)
        # for i in range(68719476735):
        #   if (i & notxmask) == (maskaddr & notxmask):
        #     mem[i] = val
        

        # mem[addr] = (val | onesmask) ^ (val & zerosmask)
        # print(addr, mem[addr])

  s = 0
  for addr, val in mem.items():
    s += val
  print(mem)
  print(s)
  # NOT 9889493670975

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
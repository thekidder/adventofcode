import re

def is_yr(x, min, max):
  try:
    xi = int(x)
    return xi >= min and xi <= max
  except:
    return False

def is_hgt(x):
  try:
    if x.endswith('cm'):
      xcm = int(x[:-2])
      return xcm >= 150 and xcm <= 193
    elif x.endswith('in'):
      xin = int(x[:-2])
      return xin >= 59 and xin <= 76
    return False
  except:
    return False

def is_hcl(x):
  return re.match('^#[a-f0-9]{6}$', x) is not None

def is_ecl(x):
  return x in ['amb','blu','brn','gry','grn','hzl','oth']

def is_pid(x):
  return re.match('^[0-9]{9}$', x) is not None


req_fields = {
  'byr': lambda x: is_yr(x, 1920, 2002),
  'iyr': lambda x: is_yr(x, 2010, 2020),
  'eyr': lambda x: is_yr(x, 2020, 2030),
  'hgt': is_hgt,
  'hcl': is_hcl,
  'ecl': is_ecl,
  'pid': is_pid,
}

def is_valid(passport):
  for k,v in req_fields.items():
    if k not in passport:
      return False
    if not v(passport[k]):
      print('invalid:' + str(passport))
      return False
  return True

v = 0
curr_passport = {}
with open('day4.txt', 'r') as f:
  for line in f:
    if len(line.strip()) == 0:
      if is_valid(curr_passport):
        v += 1
      curr_passport = {}
    fields = line.split()
    for field in fields:
      components = field.split(':', maxsplit=1)
      curr_passport[components[0]] = components[1]

if is_valid(curr_passport):
  v += 1

print(v)
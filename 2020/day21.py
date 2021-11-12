import collections
import functools
import re


def run(filename):
  ingredients = set()
  ingredient_count = collections.defaultdict(int)
  allergens = {}
  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      m = re.match('([\w\s]+) \(contains ([\w, ]+)\)', line)
      g = m.groups()
      if m is None:
        print('ERROR')
      item_ingredients = set([i.strip() for i in g[0].split(' ')])
      item_allergens = [a.strip() for a in g[1].split(',')]
      for i in item_ingredients:
        ingredient_count[i] += 1
      ingredients |= item_ingredients
      for allergen in item_allergens:
        if allergen in allergens:
          allergens[allergen] &= item_ingredients
        else:
          allergens[allergen] = set(item_ingredients)

  allergen_ingredients = functools.reduce(lambda a, b: a | b, allergens.values())
  safe_ingredient_count = functools.reduce(lambda a, b: a + ingredient_count[b], ingredients - allergen_ingredients, 0)
  print(safe_ingredient_count)

  done = False

  while not done:
    done = True
    for name, a in allergens.items():
      if len(a) == 1:
        for nameb, b in allergens.items():
          if name == nameb:
            continue
          b -= a
      else:
        done = False

  danger = []
  for allergen in sorted(allergens.keys()):
    ingredient = list(allergens[allergen])[0]
    danger.append(ingredient)

  print(allergens)
  print(','.join(danger))


# run('day21_ex.txt')
run('day21.txt')
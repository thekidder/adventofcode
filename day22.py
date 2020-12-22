import functools

debug = False

def roundhash(game):
  return ':'.join([','.join([str(c) for c in p]) for p in game])

def winnerof(cards):
  if cards[0] > cards[1]:
    return 0
  return 1

def endround(game, winner, cards):
  if winner == 1:
    cards = reversed(cards)
  game[winner].extend(cards)

def scoreof(game):
  def playerscore(p):
    return functools.reduce(lambda a, p: a + (p[0]+1)*p[1], enumerate(reversed(p)), 0)
  return functools.reduce(lambda a, p: a + playerscore(p), game, 0)

def draw(game):
  return [x.pop(0) for x in game]

def part2_game(game, root = True):
  debug and print(f'START GAME: {game}')
  prevrounds = set()
  while all(len(p) > 0 for p in game):
    state = roundhash(game)
    if state in prevrounds:
      return 0
    prevrounds.add(state)
    cards = draw(game)
    if all(len(g) >= c for g, c in zip(game, cards)):
      winner = part2_game([g[:c] for g, c in zip(game, cards)], root = False)
      endround(game, winner, cards)
    else:
      endround(game, winnerof(cards), cards)

  (debug or root) and print(f'Part 2: {scoreof(game)}')
  if len(game[0]) > 0:
    return 0
  return 1

def run(filename):
  with open(filename, 'r') as f:
    data = f.read()
    players = data.split('\n\n')

    part1 = []
    part2 = []

    for p in players:
      cards = [int(c) for c in p.split('\n') if not c.startswith('Player')]
      part1.append(cards[:])
      part2.append(cards[:])

    while all(len(p) > 0 for p in part1):
      cards = draw(part1)
      endround(part1, winnerof(cards), cards)
    print(f'Part 1: {scoreof(part1)}')
    part2_game(part2)

# run('day22_ex.txt')
run('day22.txt')
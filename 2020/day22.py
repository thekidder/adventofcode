import functools

debug = False

def roundhash(game):
  return ':'.join([','.join([str(c) for c in p]) for p in game])

def draw(game):
  return [x.pop(0) for x in game]

def winnerof(cards):
  return cards.index(max(cards))

def endround(game, winner, cards):
  game[winner].extend(cards if winner == 0 else reversed(cards))

def scoreof(game):
  def playerscore(p):
    return functools.reduce(lambda a, p: a + (p[0]+1)*p[1], enumerate(reversed(p)), 0)
  return functools.reduce(lambda a, p: a + playerscore(p), game, 0)

def part1(game):
  while all(len(p) > 0 for p in game):
    cards = draw(game)
    endround(game, winnerof(cards), cards)
  print(f'Part 1: {scoreof(game)}')

def part2(game, root = True):
  debug and print(f'START GAME: {game}')
  prevrounds = set()
  while all(len(p) > 0 for p in game):
    state = roundhash(game)
    if state in prevrounds:
      return 0
    prevrounds.add(state)
    cards = draw(game)
    if all(len(g) >= c for g, c in zip(game, cards)):
      winner = part2([g[:c] for g, c in zip(game, cards)], root = False)
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

    part1_game = []
    part2_game = []

    for p in players:
      cards = [int(c) for c in p.split('\n') if not c.startswith('Player')]
      part1_game.append(cards[:])
      part2_game.append(cards[:])

    part1(part1_game)
    part2(part2_game)

# run('day22_ex.txt')
run('day22.txt')
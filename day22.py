import functools

def roundhash(game):
  return ','.join(map(str, game[0])) + ':' + ','.join(map(str, game[1]))

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
    score = 0
    for i, c in enumerate(reversed(p)):
      score += (i + 1) * c
    return score
  return functools.reduce(lambda a, p: a + playerscore(p), game, 0)

def draw(game):
  return [x.pop(0) for x in game]

def part2_game(game):
  print(f'START GAME: {game}')
  prevrounds = set()
  while len(game[0]) > 0 and len(game[1]) > 0:
    state = roundhash(game)
    # print(state)
    if state in prevrounds:
      return 0
    prevrounds.add(state)
    cards = draw(game)
    if len(game[0]) >= cards[0] and len(game[1]) >= cards[1]:
      winner = part2_game([game[0][:cards[0]], game[1][:cards[1]]])
      endround(game, winner, cards)
    else:
      endround(game, winnerof(cards), cards)

  print(f'SCORE: {scoreof(game)}')
  if len(game[0]) > 0:
    return 0
  return 1

def run(filename):
  with open(filename, 'r') as f:
    data = f.read()
    players = data.split('\n\n')
    print(players)

    part1 = []
    part2 = []

    for p in players:
      cards = p.split('\n')
      cards = filter(lambda x: not x.startswith('Player'), cards)
      cards = list(map(int, cards))
      part1.append(cards[:])
      part2.append(cards[:])

    while len(part1[0]) > 0 and len(part1[1]) > 0:
      cards = draw(part1)
      endround(part1, winnerof(cards), cards)
    print(scoreof(part1))

    part2_game(part2)

# run('day22_ex.txt')
run('day22.txt')
def roundhash(game):
  return ','.join(map(str, game[0])) + ':' + ','.join(map(str, game[1]))

def endround(game, c0, c1):
  if c0 > c1:
    game[0].append(c0)
    game[0].append(c1)
  else:
    game[1].append(c1)
    game[1].append(c0)

def part2_game(game):
  print(f'START GAME: {game}')
  prevrounds = set()
  while len(game[0]) > 0 and len(game[1]) > 0:
    state = roundhash(game)
    # print(state)
    if state in prevrounds:
      return 0
    prevrounds.add(state)
    c0 = game[0].pop(0)
    c1 = game[1].pop(0)
    if c0 <= len(game[0]) and c1 <= len(game[1]):
      winner = part2_game([game[0][:c0], game[1][:c1]])
      if winner == 0:
        game[0].append(c0)
        game[0].append(c1)
      else:
        game[1].append(c1)
        game[1].append(c0)
    else:
      endround(game, c0, c1)

  winner = 0
  if len(game[1]) > 0:
    winner = 1

  score = 0
  for i, c in enumerate(reversed(game[winner])):
    score += (i + 1) * c
  print(f'SCORE: {score}')
  return winner


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
      c0 = part1[0].pop(0)
      c1 = part1[1].pop(0)

      endround(part1, c0, c1)

      print(part1)

    winner = 0
    if len(part1[1]) > 0:
      winner = 1

    score = 0
    for i, c in enumerate(reversed(part1[winner])):
      score += (i + 1) * c
    print(score)

    part2_game(part2)

# run('day22_ex.txt')
run('day22.txt')
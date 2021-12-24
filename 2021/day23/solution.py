import copy

room_pos = (2, 4, 6, 8)
room_pos_set = set(room_pos)
hall_len = 11

destinations = dict((chr(c+ord('A')), c) for c in range(4))
costs = dict((chr(c+ord('A')), 10**c) for c in range(4))

def solved(state):
    if any([c != '.' for c in state['hall']]):
        return False
    for i, room in enumerate(state['rooms']):
        for bot in room:
            if bot == '.' or destinations[bot] != i:
                return False
    return True


def hall_clear(state, x, y):
    begin = min(x,y)
    end = max(x,y)
    for i in range(begin,end+1):
        if state['hall'][i] != '.':
            return False
    return True


def can_enter(state, room_index):
    room = state['rooms'][room_index]
    room_len = len(room)

    if any([b != '.' and destinations[b] != room_index for b in room]):
        return -1

    for i in range(room_len):
        if room[room_len-i-1] == '.':
            return room_len-i-1

    return -1
    

def encode(s):
    return (''.join(s['hall']) + ''.join([''.join(r) for r in s['rooms']]), s['cost'])


def decode(s):
    room_len = (len(s[0]) - hall_len) / 4
    return {
        'hall': [c for c in s[0][:hall_len]],
        'rooms': [
            [c for c in s[0][hall_len:hall_len+room_len]],
            [c for c in s[0][hall_len+room_len:hall_len+room_len*2]],
            [c for c in s[0][hall_len+room_len*2:hall_len+room_len*3]],
            [c for c in s[0][hall_len+room_len*3:hall_len+room_len*4]]
        ],
        'cost': s[1]
    }


def moves(state):
    room_len = len(state['rooms'][0])

    # moves into rooms
    room_moves = False
    for i in range(len(state['hall'])):
        bot = state['hall'][i]
        if bot == '.':
            continue
        dest_room = destinations[bot]
        begin = i - 1 if i > room_pos[dest_room] else i + 1
        if not hall_clear(state, room_pos[dest_room], begin):
            continue
        dest = can_enter(state, dest_room)
        if dest != -1:
            n = copy.deepcopy(state)
            n['hall'][i] = '.'         
            n['rooms'][dest_room][dest] = bot
            n['cost'] += costs[bot] * (abs(i - room_pos[dest_room]) + 1 + dest)
            yield n
            room_moves = True

    if room_moves:
        return

    # moves into the hallway
    for i, room in enumerate(state['rooms']):
        room_loc = room_pos[i]
        for spot in range(room_len):
            if all([b not in destinations or destinations[b] == i for b in room]):
                break

            if room[spot] == '.':
                continue

            bot = room[spot]
            for j in range(len(state['hall'])):
                if hall_clear(state, room_loc, j) and j not in room_pos_set:
                    n = copy.deepcopy(state)
                    n['hall'][j] = bot
                    n['rooms'][i][spot] = '.'
                    n['cost'] += costs[bot] * (abs(j - room_loc) + 1 + spot)
                    yield n

            if spot != '.':
                break


def solve(state):
    visited = dict()
    min_cost = 100000000000
    i = 0
    universes = [state]
    while len(universes):
        s = universes.pop(0)
        ss, c = encode(s)
        if ss in visited and visited[ss] <= c:
            continue
        visited[ss] = c
        if solved(s):
            min_cost = min(s['cost'], min_cost)
        else:
            for n in moves(s):
                universes.append(n)
        i += 1
    print(f'ANSWER: {min_cost}')


example = {
    'hall': ['.'] * hall_len,
    'rooms': [['B','A'],['C','D'],['B','C'],['D','A']],
    'cost': 0
}

example2 = {
    'hall': ['.'] * hall_len,
    'rooms': [['B','D','D','A'],['C','C','B','D'],['B','B','A','C'],['D','A','C','A']],
    'cost': 0
}

input = {
    'hall': ['.'] * hall_len,
    'rooms': [['C','B'],['D','A'],['D','B'],['A','C']],
    'cost': 0
}

input2 = {
    'hall': ['.'] * hall_len,
    'rooms': [['C','D','D','B'],['D','C','B','A'],['D','B','A','B'],['A','A','C','C']],
    'cost': 0
}

solve(input)


import sys

BOARD_SIZE = 5

def has_bingo(board):
    # horiz
    for line in board:
        bingo = True
        for num in line:
            if num != None:
                bingo = False
        if bingo:
            return True
    # vert
    for i in range(BOARD_SIZE):
        bingo = True
        for row in range(BOARD_SIZE):
            if board[row][i] != None:
                bingo = False
        if bingo:
            return True

def mark(board, num):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == num:
                board[row][col] = None

def read_board(f):
    board = []
    while len(board) < 5:
        line = f.readline()
        if line == '\n':
            continue
        if len(line) == 0:
            return None
        line = line.strip()
        board.append([int(n) for n in line.split()])
    return board

def score(board, n):
    sum = 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] is not None:
                sum += board[row][col]
    return sum * n


def part1(file):
    with open(file, 'r') as f:
        nums = f.readline()

        nums = [int(num) for num in nums.split(',')]
        boards = []

        while True:
            board = read_board(f)
            if board is None:
                break
            boards.append(board)

        for n in nums:
            for board in boards:
                mark(board, n)
                if has_bingo(board):
                    print(f'WINNER: {score(board, n)}')
                    sys.exit(0)
                print(board)


def part2(file):
    with open(file, 'r') as f:
        nums = f.readline()

        nums = [int(num) for num in nums.split(',')]
        boards = []

        while True:
            board = read_board(f)
            if board is None:
                break
            boards.append(board)

        for n in nums:
            for board in boards:
                if has_bingo(board):
                    continue
                mark(board, n)
                if has_bingo(board):
                    print(f'WINNER: {score(board, n)}')
                print(board)


part2('input.txt')

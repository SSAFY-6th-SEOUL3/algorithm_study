from sys import stdin
from copy import deepcopy

DIRECTIONS = ['left', 'right', 'up', 'down']


def push(board, direction):
    """
    주어진 2차원 배열의 수들을 빈 공간이 없도록 direction 방향으로 밀어넣는다.
    """
    global N

    if direction == 'left':
        for r in range(N):
            board[r] = [int(x) for x in board[r] if x > 0]
            board[r] += ([0] * (N - len(board[r])))

    elif direction == 'right':
        for r in range(N):
            board[r] = [int(x) for x in board[r] if x > 0]
            board[r] = [0] * (N - len(board[r])) + board[r]

    elif direction == 'up':
        for c in range(N):
            i = 0
            for r in range(N):
                if board[r][c]:
                    board[i][c] = board[r][c]
                    i += 1

            for r in range(i, N):
                board[r][c] = 0

    else:
        for c in range(N):
            i = N - 1
            for r in range(N - 1, -1, -1):
                if board[r][c]:
                    board[i][c] = board[r][c]
                    i -= 1

            for r in range(i + 1):
                board[r][c] = 0


def merge(temp, direction):
    """
    2차원 배열에서 direction 방향으로 이동했을 때 수들이 합쳐진 결과를 리턴한다.
    """
    global N
    board = deepcopy(temp)
    push(board, direction)

    if direction == 'left':
        for r in range(N):
            for c in range(N - 1):
                if board[r][c] and board[r][c] == board[r][c + 1]:
                    board[r][c] *= 2
                    board[r][c + 1] = 0

    elif direction == 'right':
        for r in range(N):
            for c in range(N - 1, 0, -1):
                if board[r][c] and board[r][c] == board[r][c - 1]:
                    board[r][c] *= 2
                    board[r][c - 1] = 0

    elif direction == 'up':
        for c in range(N):
            for r in range(N - 1):
                if board[r][c] and board[r][c] == board[r + 1][c]:
                    board[r][c] *= 2
                    board[r + 1][c] = 0

    else:
        for c in range(N):
            for r in range(N - 1, 0, -1):
                if board[r][c] and board[r][c] == board[r - 1][c]:
                    board[r][c] *= 2
                    board[r - 1][c] = 0

    push(board, direction)
    return board


def get_max_block(board, count):
    """
    주어진 보드를 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 구한다.
    Args:
        count: 현재까지 보드를 이동시킨 횟수
    """
    if count < 5:
        # 사방으로 이동한 결과에 대하여, 재귀적으로 함수를 다시 호출한다.
        for i in range(4):
            get_max_block(merge(board, DIRECTIONS[i]), count + 1)
    else:
        # 5번 이동한 결과에 대하여, 블록의 최대값을 max_block에 업데이트한다.
        global max_block

        for r in range(N):
            for c in range(N):
                if board[r][c] > max_block:
                    max_block = board[r][c]


N = int(stdin.readline())
board = []

for _ in range(N):
    board.append([int(x) for x in stdin.readline().split()])

max_block = 0

get_max_block(board, 0)
print(max_block)

from sys import stdin

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def is_possible(board, R, C):
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if board[r][c] == 'S':
                for i in range(4):
                    if board[r + dr[i]][c + dc[i]] == 'W':
                        return 0
    return 1


R, C = map(int, stdin.readline().split())

board = ['.' * (C + 2)]
for _ in range(R):
    board.append('.' + stdin.readline().rstrip() + '.')
board.append('.' * (C + 2))

result = is_possible(board, R, C)
print(result)

if result:
    for r in range(1, R + 1):
        print(board[r][1:C + 1].replace('.', 'D'))

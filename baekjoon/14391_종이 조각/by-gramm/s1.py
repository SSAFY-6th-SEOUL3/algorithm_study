"""
가로 or 세로로 쭉 채우면 최댓값이 된다고 생각했으나 틀림.

예외  0 0 1
     0 0 1
     1 1 1
"""

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([x for x in list(input())])

col_max_value = sum([int("".join(sub_board)) for sub_board in board])
row_max_value = 0

for c in range(M):
    current = ""

    for r in range(N):
        current += board[r][c]

    row_max_value += int(current)

print(max(col_max_value, row_max_value))

from sys import stdin


N = int(stdin.readline())
board = []

for _ in range(N):
    board.append([int(x) for x in stdin.readline().split()])

counts = [[0] * N for _ in range(N)]
counts[0][0] = 1

for r in range(N):
    for c in range(N):
        for i in range(1, 10):
            if r >= i and board[r - i][c] == i:
                counts[r][c] += counts[r - i][c]
            if c >= i and board[r][c - i] == i:
                counts[r][c] += counts[r][c - i]

print(counts[N - 1][N - 1])

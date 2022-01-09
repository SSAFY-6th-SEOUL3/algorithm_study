import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
ans = 0
for i in range(1 << N * M):
    used = [0] * N * M
    for j in range(N * M):
        if i & (1 << j):
            used[j] = 1

    total = 0
    for y in range(N):
        row_sum = 0
        for x in range(M):
            idx = y * M + x
            if used[idx]:
                row_sum = row_sum * 10 + board[y][x]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum
        row_sum = 0

    for x in range(M):
        col_sum = 0
        for y in range(N):
            idx = y * M + x
            if not used[idx]:
                col_sum = col_sum * 10 + board[y][x]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
        col_sum = 0

    ans = max(total, ans)

print(ans)

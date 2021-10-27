# 동적 프로그래밍으로 풀이함 (0-1 Knapsack Problem)

N, K = map(int, input().split())
weights = [0]
values = [0]

for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

"""
board[r][c]: r번 물건까지 선택 가능한 경우, 무게 합을 ckg 이하로 고른 경우의 가치의 최대합
board[r][c] = max(board[r - 1][c], board[r - 1][c - weights[r]] + values[r])
"""
board = [[0] * (K + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, K + 1):
        # r번 물건을 선택할 수 없는 경우
        if c < weights[r]:
            board[r][c] = board[r - 1][c]
        # r번 물건을 선택할 수 있는 경우
        else:
            board[r][c] = max(board[r - 1][c], board[r - 1][c - weights[r]] + values[r])

print(board[N][K])

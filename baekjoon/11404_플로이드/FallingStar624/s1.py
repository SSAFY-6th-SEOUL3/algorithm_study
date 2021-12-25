import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())
INF = 9876543210
FW = [[INF]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    FW[i][i] = 0

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    FW[start][end] = min(FW[start][end], cost)

for k in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            FW[start][end] = min(FW[start][end], FW[start][k] + FW[k][end])

for i in range(1, N+1):
    for j in range(1, N+1):
        if FW[i][j] == INF:
            FW[i][j] = 0

for row in FW[1:]:
    tmp = list(map(str, row[1:]))
    print(' '.join(tmp))



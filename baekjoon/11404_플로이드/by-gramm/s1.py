# 그냥 input()으로 입력받으면 4824ms
# stdin.readline()으로 입력받으면 724ms

from sys import stdin


n = int(stdin.readline())
m = int(stdin.readline())
INF = 12345678

distances = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distances[i][i] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    distances[a][b] = min(distances[a][b], c)

"""
A에서 B로 가는 최단 거리 = min(A에서 B로 가는 최단 거리, A에서 node를 거쳐 B로 가는 최단 거리)
distances[a][b] = min(distances[a][b], distances[a][node] + distances[node][b])
"""
for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            distances[start][end] = min(distances[start][end],
                                        distances[start][mid] + distances[mid][end])

for r in range(1, n + 1):
    for c in range(1, n + 1):
        if distances[r][c] == INF:
            distances[r][c] = 0
        print(distances[r][c], end=" ")
    print()

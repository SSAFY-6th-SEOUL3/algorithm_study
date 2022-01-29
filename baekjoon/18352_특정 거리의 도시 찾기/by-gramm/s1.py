"""
1. 최대 백만 줄의 입력이 주어지므로 sys.stdin 사용
2. 도시의 개수가 최대 300,000개이므로, 인접 행렬 대신 인접 그래프 사용
3. 도로의 거리가 모두 동일하므로, 다익스트라 대신 BFS 사용
"""

from sys import stdin
from collections import deque


N, M, K, X = map(int, stdin.readline().split())
adj_graph = [set() for _ in range(N + 1)]
distances = [-1] * (N + 1)

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    adj_graph[A].add(B)

queue = deque()
queue.append(X)
distances[X] = 0

while queue:
    node = queue.popleft()

    for i in adj_graph[node]:
        if distances[i] == -1:
            distances[i] = distances[node] + 1

            if distances[i] < K:  # 거리가 K 이상이면 더 이상 탐색 필요 X
                queue.append(i)

flag = False  # 최단 거리가 K인 도시가 존재하는지의 여부

for i in range(1, N + 1):
    if distances[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)

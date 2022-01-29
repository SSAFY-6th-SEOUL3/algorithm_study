#pyp3는 통과, python3는 시간초과...?
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

visited = [0] * (N+1)
dist = [9876543210] * (N+1)
Q = deque([X])

while Q:
    # 출발점 Q에서 선택
    start = Q.popleft()
    # 출발지점 방문 표시
    visited[start] = 1
    # start 지점 기준으로 update
    for i in graph[start]:
        if not visited[i] or dist[i] > dist[start]+1:
            dist[i] = dist[start]+1
            visited[i] = 1
            Q.append(i)

exist = False
for city in range(N+1):
    if dist[city] == K:
        exist = True
        print(city)

if not exist:
    print(-1)

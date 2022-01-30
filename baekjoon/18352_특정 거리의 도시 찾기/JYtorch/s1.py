import sys
sys.stdin = open('input.txt')

from collections import deque
N, M, K, X = map(int, sys.stdin.readline().split())

city = [[] for _ in range(N + 1)]
for i in range(1, M + 1):
    n1, n2 = list(map(int, sys.stdin.readline().split()))
    city[n1].append(n2)
visited = [0] * (N + 1)
q = deque([(X, 0)])

while q:
    v, d = q.popleft()

    d += 1
    for w in city[v]:
        if v == w or X == w: continue
        if visited[w]: continue
        visited[w] = d
        if d < K:
            q.append((w, d))

if K not in set(visited):
    print(-1)
else:
    for i in range(N + 1):
        if visited[i] == K:
            print(i)
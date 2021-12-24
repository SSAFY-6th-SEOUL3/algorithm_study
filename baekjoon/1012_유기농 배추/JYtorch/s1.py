import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def solution():
    ans = 0
    for y in range(M):
        for x in range(N):
            if arr[y][x] and not visited[y][x]:
                visited[y][x] = 1

                q = deque([(y, x)])

                while q:
                    r, c = q.popleft()

                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if nr < 0 or nr >= M or nc < 0 or nc >= N: continue
                        if arr[nr][nc] and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                ans += 1
    return ans

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for i in range(K):
        r, c = map(int, input().split())
        arr[r][c] = 1
    print(solution())
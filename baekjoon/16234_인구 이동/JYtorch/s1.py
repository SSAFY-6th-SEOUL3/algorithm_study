import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def divide(y, x):
    global check
    visited[y][x] = value

    q = deque()
    q.append((y, x))
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if L <= abs(arr[r][c] - arr[nr][nc]) <= R and not visited[nr][nc]:
                visited[nr][nc] = value
                q.append((nr, nc))


def sum_population():

    sum_set = {}
    for i in range(N):
        for j in range(N):
            if sum_set.get(visited[i][j]):
                sum_set[visited[i][j]][0] += arr[i][j]
                sum_set[visited[i][j]][1] += 1
            else:
                sum_set[visited[i][j]] = [arr[i][j], 1]

    for i in range(N):
        for j in range(N):
            arr[i][j] = sum_set[visited[i][j]][0] // sum_set[visited[i][j]][1]


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:

    value = 1
    visited = [[0] * N for _ in range(N)]
    # 국경선 열기(인구 이동 가능한 국가는 visited를 동일한 value로 채우기)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                divide(i, j)
                value += 1
    # 인구수 합치기
    sum_population()

    # 인구 이동이 더이상 불가능 하면 종료
    if value == N * N + 1:
        break

    ans += 1
print(ans)
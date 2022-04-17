import sys
sys.stdin = open('input.txt')
from collections import deque


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution(y, x):
    size = 0
    curr = sample[y][x]
    q = deque([(y, x)])
    while q:
        r, c = q.popleft()
        size += 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:
                continue
            if sample[nr][nc] == curr:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return curr, size


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    sample = [input() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    A_cnt = 0
    B_cnt = 0
    max_size = 0
    for i in range(N):
        for j in range(M):
            if sample[i][j] != '_' and not visited[i][j]:
                visited[i][j] = 1
                sample_type, cnt = solution(i, j)
                max_size = max(max_size, cnt)
                if sample_type == 'A':
                    A_cnt += 1
                elif sample_type == 'B':
                    B_cnt += 1

    print('#{} {} {} {}'.format(tc, A_cnt, B_cnt, max_size))

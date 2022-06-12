from sys import stdin
from heapq import heappush, heappop


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

M, N = map(int, stdin.readline().split())
board = []

for _ in range(M):
    board.append([int(x) for x in stdin.readline().split()])

counts = [[0] * N for _ in range(M)]
counts[0][0] = 1
heap = [(-board[0][0], 0, 0)]

while heap:
    height, cnt_r, cnt_c = heappop(heap)
    height = -height

    for i in range(4):
        r, c = cnt_r + dr[i], cnt_c + dc[i]

        if 0 <= r < M and 0 <= c < N and board[r][c] < height:
            if counts[r][c] == 0:
                heappush(heap, (-board[r][c], r, c))
            counts[r][c] += counts[cnt_r][cnt_c]

print(counts[M - 1][N - 1])

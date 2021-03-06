import sys
sys.stdin = open('input.txt')

import time
start = time.time()
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
"""
1. 벽 3개를 세우는 모든 경우의 수 구하기
2. 바이러스가 이동할 수 있는 범위 다 2로 채우기
3. 0의 개수를 카운트해서 최대값이면 갱신

"""
##########################################################
# bfs로 바이러스 퍼뜨리기
from collections import deque
def bfs(mat):
    global ans
    q = deque(virus)

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if not mat[nr][nc]:

                mat[nr][nc] = 2
                q.append((nr, nc))

    cnt = 0
    for l in mat:
        cnt += l.count(0)
    if ans < cnt:
        ans = cnt


# dfs로 벽 세우기
def solution(start, lev):
    global total, ans

    if lev == 3:
        mat = [a[:] for a in arr]  # deepcopy를 이용한 이차원 배열 복사보다 속도가 더 빠름
        bfs(mat)

        return

    else:
                                        # ex. N: 3, M: 3 인 경우를 예로 들어보자.
                                        # start = 0일 때,
                                        # for 반복문의 i는 0부터 8까지 돎. (N * M = 9 이므로)
                                        # i의 값에 따라 y, x 값도 다음과 같이 변함
        for i in range(start, N * M):   # i => 0 1 2 3 4 5 6 7 8
            y = i // M                  # y => 0 0 0 1 1 1 2 2 2
            x = i % M                   # x => 0 1 2 0 1 2 0 1 2
                                        # start = 0일 때, (0, 0), (0, 1), (0, 2), (1, 0), (1, 1) ... (2, 2) 8개 좌표 모두 방문
                                        # start = 1일 때, (0, 1), (0, 2), (1, 0), (1, 1) ... (2, 2) 7개 좌표 방문
                                        # start = 2일 때, (0, 2), (1, 0), (1, 1) ... (2, 2) 6개 좌표 방문
                                        # ...
                                        # start = 8일 때, (2, 2) 1개 방문


            if not arr[y][x]:
                arr[y][x] = 1           # 결국 lev = 3 이 되면 arr의 각 정점을 중복없이 모두 방문하면서 1을 세개씩 채워줄 수 있음.
                solution(i, lev + 1)
                arr[y][x] = 0

# # combination 이용하여 벽 세우기
# def solution2():
#     from itertools import combinations
#     comb = []
#     for i in range(N):
#         for j in range(M):
#             if not arr[i][j]:
#                 comb.append((i, j))
#     for comb_list in combinations(comb, 3):
#         mat = [t[:] for t in arr]
#         for r, c in comb_list:
#             mat[r][c] = 1
#
#         bfs(mat)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))

solution(0, 0)
# solution2()

print("time :", time.time() - start)
print(ans)


##########################################
# # dfs로 바이러스 퍼뜨리기
# def dfs(r, c, board):
#     if board[r][c] == 2:
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#
#             if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
#             if board[nr][nc] == 0:
#                 board[nr][nc] = 2
#                 dfs(nr, nc, board)
#
# # combination으로 벽 세우기
# def solution():
#     global ans
#     from itertools import combinations
#     comb = []
#     for i in range(N):
#         for j in range(M):
#             if not arr[i][j]:
#                 comb.append((i, j))
#     for comb_list in combinations(comb, 3):
#         ## deepcopy로 복사하기
#         # import copy
#         # mat = copy.deepcopy(arr)
#
#         # slicing으로 복사하기
#         mat = [t[:] for t in arr]
#
#         for r, c in comb_list:
#             mat[r][c] = 1
#         for vr, vc in virus:
#             dfs(vr, vc, mat)
#
#         total = 0
#         for l in mat:
#             total += l.count(0)
#         ans = max(ans, total)
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# virus = []
# ans = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 2:
#             virus.append((i, j))
# solution()
# print(ans)
# print('time:', time.time() - start)


#####################################################
# # dfs로 바이러스 퍼뜨리기
# def dfs(r, c, board):
#     if board[r][c] == 2:
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#
#             if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
#             if board[nr][nc] == 0:
#                 board[nr][nc] = 2
#                 dfs(nr, nc, board)
#
# tmp = []
# # dfs로 벽 세우기
# def solution(lev):
#     global ans
#     if lev == 3:
#
#         ## deepcopy로 복사하기
#         # import copy
#         # mat = copy.deepcopy(arr)
#
#         # slicing으로 복사하기
#         mat = [t[:] for t in arr]
#
#
#         for vr, vc in virus:
#             dfs(vr, vc, mat)
#
#         total = 0
#         for l in mat:
#             total += l.count(0)
#         ans = max(ans, total)
#
#         return
#
#     else:
#         # 이중 for 문으로 벽 세우는 방법 (used를 사용해서 중복 제거)?? 고민해보자..
#         for y in range(N):
#             for x in range(M):
#                 if arr[y][x]: continue
#                 if used[y][x]: continue
#
#                 arr[y][x] = 1
#                 solution(lev + 1)
#                 arr[y][x] = 0
#
#
# def solution2(start, lev):
#     global ans
#     if lev == 3:
#         mat = [t[:] for t in arr]
#
#         for vr, vc in virus:
#             dfs(vr, vc, mat)
#
#         total = 0
#         for l in mat:
#             total += l.count(0)
#         ans = max(ans, total)
#         return
#     else:
#         for i in range(start, N*M):
#             y = i // M
#             x = i % M
#
#             if not arr[y][x]:
#                 arr[y][x] = 1
#                 solution2(i, lev + 1)
#                 arr[y][x] = 0
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# virus = []
# used = [[0] * M for _ in range(N)]
# ans = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 2:
#             virus.append((i, j))
#             used[i][j] = 1
# # solution(0)
# solution2(0, 0) # 24804회 실행
# print(ans)
# print('time:', time.time() - start)
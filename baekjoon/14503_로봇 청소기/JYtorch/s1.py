import sys
sys.stdin = open('input.txt')

# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution1(y, x, direction):
    space = 0

    mat[y][x] = 2                           # 현재 위치 청소 (청소한 곳은 2로 채우기)

    for i in range(4):                      # 네 방향 탐색
        direction = (direction - 1) % 4     # 현재 자신이 바라보고 있는 방향에서 왼쪽으로 한번 회전
        ny = y + dy[direction]
        nx = x + dx[direction]

        if nx < 0 or nx >= M or ny < 0 or ny >= N or mat[ny][nx]: continue
        space += 1
        solution1(ny, nx, direction)    # 이동할 공간이 있으면 이동 후, 탐색 종료
        break

    # 4방향 모두 탐색했는데, 더이상 이동할 공간이 없다면(space == 0), direction을 바라본 채로 한칸 후진한다.
    if not space:
        back_direction = (direction + 2) % 4
        ny, nx = y + dy[back_direction], x + dx[back_direction]
        if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] != 1:
            solution1(ny, nx, direction)

# from collections import deque
# def solution2():
#     cnt = 0
#     q = deque([(r, c, d)])
#
#     while q:
#         space = 0
#         y, x, direction = q.popleft()
#
#         if not mat[y][x]:
#             mat[y][x] = 2
#             cnt += 1
#
#         for i in range(4):
#             direction = (direction - 1) % 4
#             ny = y + dy[direction]
#             nx = x + dx[direction]
#
#             if nx < 0 or nx >= M or ny < 0 or ny >= N or mat[ny][nx]: continue
#             space += 1
#
#             q.append((ny, nx, direction))
#             break
#
#         if not space:
#             nd = (direction + 2) % 4
#             ny, nx = y + dy[nd], x + dx[nd]
#             if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] != 1:
#                 q.append((ny, nx, direction))
#     return cnt


N, M = map(int, input().split())
r, c, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

ans = 0
solution1(r, c, d)
for l in mat:
    ans += l.count(2)       # 청소한 공간 카운트
print(ans)

# print(solution2())


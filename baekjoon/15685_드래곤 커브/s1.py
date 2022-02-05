import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def solution(r, c, d, g):

    q = deque()    # 지금까지 지나온 모든 방향을 90도 회전시킨 뒤 최신순으로 담아놓을 큐
    # 총 (g + 1)번 반복문을 돌려서 선분 긋기
    for gene in range(g + 1):
        if q:                           # q는 현재까지의 모든 세대의 정보를 담은 큐
            cur_q = deque(list(q))      # cur_q는 한 세대의 정보만 담아놓은 큐
        else:
            cur_q = deque([d])

        while cur_q:
            d = cur_q.popleft()
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위를 벗어나면 종료
            if nr < 0 or nr > 100 or nc < 0 or nc > 100:
                return

            board[nr][nc] = 1   # 1) 선분 긋기
            d = (d + 1) % 4     # 2) 현재 지나온 방향에서 90도 회전
            q.appendleft(d)     # 3) 최신순으로 q에 넣기
            r, c = nr, nc


N = int(input())
curve_info = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 101 for _ in range(101)]
for x, y, direction, generation in curve_info:
    board[y][x] = 1
    solution(y, x, direction, generation)

# 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수 찾기
ans = 0
for y in range(100):
    for x in range(100):
        if board[y][x] and board[y][x + 1] and board[y + 1][x] and board[y + 1][x + 1]:
            ans += 1
print(ans)

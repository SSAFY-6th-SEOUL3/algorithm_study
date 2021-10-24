import sys
sys.stdin = open('input.txt')
from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(rr, rc, br, bc, t):
    q = deque()
    q.append((rr, rc, br, bc, t))

    while q:
        cry, crx, cby, cbx, turn = q.popleft()

        if turn >= 10:
            continue

        # 4방향으로 기울이기
        for i in range(4):

            red_goal = False
            blue_goal = False

            # 빨간 공 벽에 닿거나 골인할 때까지 기울이기
            for j in range(1, max(N, M)):
                nry = cry + dr[i] * j
                nrx = crx + dc[i] * j

                if arr[nry][nrx] == 'O':
                    red_goal = True
                    break

                if arr[nry][nrx] == '#':
                    nry = cry + dr[i] * (j-1)
                    nrx = crx + dc[i] * (j-1)
                    break

            # 파란 공 벽에 닿거나 골인할 때까지 기울이기
            for k in range(1, max(N, M)):
                nby = cby + dr[i] * k
                nbx = cbx + dc[i] * k

                if arr[nby][nbx] == 'O':
                    blue_goal = True
                    break

                if arr[nby][nbx] == '#':
                    nby = cby + dr[i] * (k-1)
                    nbx = cbx + dc[i] * (k-1)
                    break

            # 파란 공이 들어가면 실패
            if blue_goal: continue

            # 빨간공 하나만 들어가면 기울인 횟수 return
            if red_goal and not blue_goal:
                return turn + 1

            # 기울인 두 공의 위치가 같으면, 기울인 방향에 따라 위치 조정
            if (nry, nrx) == (nby, nbx):

                # 오른쪽으로 기울이기
                if i == 0:
                    if crx > cbx: # 빨간 공이 파란공 오른쪽에 있었으면
                        nbx = nrx - 1

                    else:
                        nrx = nbx - 1
                # 아래로 기울이기
                elif i == 1:
                    if cry > cby: # 파란공이 빨간공 위에 있었으면
                        nby = nry - 1
                    else:
                        nry = nby - 1

                #왼쪽으로 기울이기
                elif i == 2:
                    if cbx > crx: # 파란공이 빨간공 오른쪽에 있었으면
                        nbx = nrx + 1
                    else:
                        nrx = nbx + 1
                #위로 기울이기
                elif i == 3:
                    if cry > cby: # 파란공이 빨간공 위에 있었으면
                        nry = nby + 1
                    else:
                        nby = nry + 1
            q.append((nry, nrx, nby, nbx, turn+1))
    return -1

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            blue = i, j
        if arr[i][j] == 'R':
            red = i, j

print(bfs(red[0], red[1], blue[0], blue[1], 0))
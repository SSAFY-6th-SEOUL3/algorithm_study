import sys
sys.stdin = open('input.txt')
from collections import deque
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(arr):
    q = deque()

    # r, c, d(방향), now_time(현재 시간), length(몸통 길이)
    q.append((0, 0, 0, 1, 1)) # (0, 0) 위치에서 몸통 길이 1인 뱀이 우(0) 방향으로 진행

    while q:
        r, c, d, now_time, length = q.popleft()

        # 정해진 시간이 되면 방향 전환
        if directions and now_time == int(directions[0][0]) + 1:
            time, direction = directions.popleft()

            if d == 0:
                if direction == 'L':
                    d = 3
                else:
                    d = 1
            elif d == 1:
                if direction == 'L':
                    d = 0
                else:
                    d = 2
            elif d == 2:
                if direction == 'L':
                    d = 1
                else:
                    d = 3
            else:
                if direction == 'L':
                    d = 2
                else:
                    d = 0

        # 한칸 이동한 위치 (nr, nc)
        nr = r + dr[d]
        nc = c + dc[d]

        # 한칸 이동한 위치가 맵을 벗어나면 종료
        if nr < 0 or nr >= N or nc < 0 or nc >= N: return now_time

        # 한칸 이동한 위치가 자신의 몸통이면 종료
        if visited[r][c] + 1 <= visited[nr][nc] + length: return now_time


        # 사과(9)가 있는 곳이면 몸통 길이를 1 늘려주고, 시간을 1 더해주면서 (nr, nc) 로 이동한다.
        if arr[nr][nc] == 9:
            length += 1
            arr[nr][nc] = 0
            q.append((nr, nc, d, now_time + 1, length))
            visited[nr][nc] = visited[r][c] + 1

        # 사과가 없는 곳이면, 그냥 시간을 1 더해주면서 (nr, nc) 로 이동한다.
        elif arr[nr][nc] == 0:
            q.append((nr, nc, d, now_time + 1, length))
            visited[nr][nc] = visited[r][c] + 1

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())

directions = deque()  # 방향 전환 리스트
for _ in range(L):
    directions.append(list(input().split()))


mat = [[0] * N for _ in range(N)]
for y, x in apples: # 사과가 있는 곳은 9로 채우기
    mat[y-1][x-1] = 9

# visited 배열에 지나온 위치를 1씩 더해가며 계속 기록하는 방식
# ex. 3x3 맵 기준으로 (0,0)에서 우로 두번 이동할 경우, visited는 [[1, 2, 3], [0, 0, 0], [0, 0, 0]]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 1

print(bfs(mat))
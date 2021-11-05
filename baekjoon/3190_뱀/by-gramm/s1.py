from collections import deque

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
K = int(input())
apples = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    r, c = map(int, input().split())
    apples[r][c] = 1

"""
snake: 뱀의 위치 정보를 저장한 배열
       (0번 인덱스가 꼬리, 마지막 인덱스가 머리)
i: 뱀의 진행 방향 (0 ~ 3이 각각 상우하좌)
"""
snake = deque()
snake.append((1, 1))  # 뱀의 시작 위치 : (1, 1)
i = 1                 # 뱀의 초기 방향 : 오른쪽

time = 0
directions = [0] * 10001
L = int(input())

for _ in range(L):
    X, C = input().split()
    if C == 'L':
        directions[int(X)] = -1
    else:
        directions[int(X)] = 1

while True:
    time += 1
    # nr, nc: 뱀의 머리 위치
    nr, nc = snake[-1][0] + dr[i], snake[-1][1] + dc[i]
    # 1. 뱀이 벽에 부딪힌 경우 => 탐색 종료
    if not (0 < nr < (N + 1) and 0 < nc < (N + 1)):
        break

    # 2. 뱀이 자기 자신과 부딪힌 경우 => 탐색 종료
    if (nr, nc) in snake:
        break

    snake.append((nr, nc))          # 뱀의 새로운 머리를 추가한다.

    if apples[nr][nc]:              # 새로운 위치에 사과가 있다면
        apples[nr][nc] = 0          # 사과를 없애준다.
    else:                           # 새로운 위치에 사과가 없다면
        snake.popleft()             # 꼬리가 위치한 칸을 비워준다.

    i = (i + directions[time]) % 4  # 뱀의 진행 방향을 업데이트한다.

print(time)

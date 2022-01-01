import sys
sys.stdin = open("14503.txt")

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 청소기 방향 d (델타 일치)
FORWARD, RIGHT, BACK, LEFT = 0, 1, 2, 3

# 청소 체크
cleaned = [[False] * m for _ in range(n)]


def next_position(r, c, d, dir):
    """
    :param r: 청소기 현재 x좌표
    :param c: 청소기 현재 y좌표
    :param i: 청소기 현재 방향
    :param dir: 특정 방향
    :return: 특정 방향의 인접 위치(r, c)를 리턴

    i = 0 즉, 앞을 보고있는 청소기의 LEFT(3) 왼쪽 방향 좌표는 (i+3)%4 = 3 즉, dr, dc의 인덱스 3
    """
    return r + dr[(d+dir) % 4], c + dc[(d+dir) % 4]


count = 0
while True:
    # 1. 현재 위치를 청소한다.
    cleaned[r][c] = True

    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접칸을 탐색한다.
    count = 0

    # 왼쪽 칸을 탐색한다.
    while count < 4:
        nr, nc = next_position(r, c, d, LEFT)

        # 청소할 공간이 있고 벽이 아니라면
        if cleaned[nr][nc] == False and board[nr][nc] == 0:
            # 해당 방향으로 회전하고
            d = (d - 1) % 4
            # 한 칸 전진하고 1번으로 돌아간다.
            r, c = nr, nc
            break

        # 청소되어 있거나 벽인 경우
        else:
            # 그 방향으로 회전하고 카운트를 하나 늘린다.
            d = (d - 1) % 4

            count += 1

    # 네 방향을 모두 탐색했고
    if count >= 4:
        nr, nc = next_position(r, c, d, BACK)

        # 후진이 불가능하다면 멈춘다.
        if board[nr][nc] == 1:
            break
        else:
            # 후진이 가능하다면 후진하고 2번으로 돌이간다.
            r, c = nr, nc



# print(cleaned)
# 최종적으로 청소한 칸의 수를 구한다.

result = 0
for i in range(n):
    for j in range(m):
        if cleaned[i][j] == True:
            result += 1


print(result)















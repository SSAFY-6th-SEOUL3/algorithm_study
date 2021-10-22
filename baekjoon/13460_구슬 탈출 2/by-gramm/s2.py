# s1.py의 코드를 정리하고자 함.

from collections import deque

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_order(red, blue, i):
    """
    두 구슬 중 어떤 구슬을 먼저 굴려야 할지 결정한다.
    (굴리는 방향에 더 가까운 구슬을 먼저 굴린다.)
    Returns:
        빨간 구슬을 먼저 굴리면 True, 파란 구슬을 먼저 굴리면 False
    """
    if i == 0:
        return red[0] < blue[0]
    elif i == 1:
        return red[1] > blue[1]
    elif i == 2:
        return red[0] > blue[0]
    else:
        return red[1] < blue[1]


def roll_marble(marble1, marble2, i):
    """
    구슬을 한 방향으로 굴렸을 때의 구슬의 위치를 구한다.
    Args:
        marble1: 굴리는 구슬의 위치
        marble2: 나머지 구슬의 위치
        i: 구슬이 굴러가는 방향
           (0: 위쪽 / 1: 오른쪽 / 2: 아래쪽 / 3: 왼쪽)
    Returns:
        1) 구슬이 구멍에 빠지는 경우 : (-1, -1)
        2) 그 외의 경우 : 굴린 후의 구슬의 위치
    """
    nr, nc = marble1
    fixed_r, fixed_c = marble2

    while True:
        nr, nc = nr + dr[i], nc + dc[i]
        if not (1 <= nr < N - 1 and 1 <= nc < M - 1
                and board[nr][nc] != '#'
                and (fixed_r != nr or fixed_c != nc)):
            nr, nc = nr - dr[i], nc - dc[i]
            break
        if nr == hole[0] and nc == hole[1]:
            nr, nc = -1, -1
            break

    return nr, nc


def incline_board(red, blue, i):
    """
    보드를 direction 방향으로 기울인 결과를 구한다.
    Args:
        red, blue: 빨간 구슬 / 파란 구슬의 위치
        i: 보드를 기울이는 방향
           (0: 위쪽 / 1: 오른쪽 / 2: 아래쪽 / 3: 왼쪽)
    Returns:
        1) 파란 구슬이 구멍에 들어간 경우 : 'hole'
        2) 파란 구슬은 들어가지 않고, 빨간 구슬만 구멍에 들어간 경우 : 'end'
        3) 그 외의 경우 : (빨간 구슬의 위치, 파란 구슬의 위치)
    """
    global N, M, board, hole

    # 빨간 구슬을 먼저 굴려야 하는 경우
    if get_order(red, blue, i):
        red = roll_marble(red, blue, i)
        blue = roll_marble(blue, red, i)
    else:
        blue = roll_marble(blue, red, i)
        red = roll_marble(red, blue, i)

    if blue[0] == -1:   # 파란 공이 구멍에 빠진 경우
        return 'hole'
    elif red[0] == -1:  # 빨간 공만 구멍에 빠진 경우
        return 'end'
    else:
        return (red, blue)


N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(input()))

# 빨간 구슬, 파란 구슬, 구멍의 위치를 저장한다.
for r in range(1, N - 1):
    for c in range(1, M - 1):
        if board[r][c] == 'R':
            red = (r, c)
        elif board[r][c] == 'B':
            blue = (r, c)
        elif board[r][c] == 'O':
            hole = (r, c)

queue = deque()
queue.append((red, blue, 0))
answer = -1

while queue:
    red, blue, count = queue.popleft()

    if count >= 10:
        break

    for i in range(4):
        result = incline_board(red, blue, i)

        if result == 'hole':
            continue
        if result == 'end':
            break

        new_red, new_blue = result
        # 구슬의 위치가 그대로라면
        if red == new_red and blue == new_blue:
            continue
        queue.append((new_red, new_blue, count + 1))

    if result == 'end':
        answer = count + 1
        break

print(answer)

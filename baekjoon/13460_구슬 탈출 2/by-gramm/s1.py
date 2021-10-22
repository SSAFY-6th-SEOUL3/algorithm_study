# 최단 거리이므로 BFS 알고리즘을 통해 풀이하고자 함.


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


def roll_marbles(red, blue, i):
    """
    보드를 direction 방향으로 기울인 결과를 구한다.
    Args:
        red, blue: 빨간 구슬 / 파란 구슬의 위치
        i: 보드를 기울이는 방향
           (0: 위쪽 / 1: 오른쪽 / 2: 아래쪽 / 3: 왼쪽)
    Returns:
        1) 파란 구슬이 구멍에 들어간 경우:
        2) 파란 구슬은 들어가지 않고, 빨간 구슬만 구멍에 들어간 경우:
        3) 그 외의 경우:
    """
    global N, M, board, hole
    red_r, red_c = red
    blue_r, blue_c = blue
    red_to_hole, blue_to_hole = False, False

    # 빨간 구슬을 먼저 굴려야 하는 경우
    if get_order(red, blue, i):
        while True:
            red_r, red_c = red_r + dr[i], red_c + dc[i]
            if not (1 <= red_r < N - 1 and 1 <= red_c < M - 1
                    and board[red_r][red_c] != '#'):
                red_r, red_c = red_r - dr[i], red_c - dc[i]
                break
            if red_r == hole[0] and red_c == hole[1]:
                red_to_hole = True
                red_r, red_c = -1, -1
                break

        while True:
            blue_r, blue_c = blue_r + dr[i], blue_c + dc[i]
            if not (1 <= blue_r < N - 1 and 1 <= blue_c < M - 1
                    and board[blue_r][blue_c] != '#'
                    and (red_r != blue_r or red_c != blue_c)):
                blue_r, blue_c = blue_r - dr[i], blue_c - dc[i]
                break
            if blue_r == hole[0] and blue_c == hole[1]:
                blue_to_hole = True
                blue_r, blue_c = -1, -1
                break
    # 파란 구슬을 먼저 굴려야 하는 경우
    else:
        while True:
            blue_r, blue_c = blue_r + dr[i], blue_c + dc[i]
            if not (1 <= blue_r < N - 1 and 1 <= blue_c < M - 1
                    and board[blue_r][blue_c] != '#'):
                blue_r, blue_c = blue_r - dr[i], blue_c - dc[i]
                break
            if blue_r == hole[0] and blue_c == hole[1]:
                blue_to_hole = True
                blue_r, blue_c = -1, -1
                break
        while True:
            red_r, red_c = red_r + dr[i], red_c + dc[i]
            if not (1 <= red_r < N - 1 and 1 <= red_c < M - 1
                    and board[red_r][red_c] != '#'
                    and (red_r != blue_r or red_c != blue_c)):
                red_r, red_c = red_r - dr[i], red_c - dc[i]
                break
            if red_r == hole[0] and red_c == hole[1]:
                red_to_hole = True
                red_r, red_c = -1, -1
                break

    if blue_to_hole:
        return 'hole'
    elif red_to_hole:
        return 'end'
    else:
        return ((red_r, red_c), (blue_r, blue_c))


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
        result = roll_marbles(red, blue, i)

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

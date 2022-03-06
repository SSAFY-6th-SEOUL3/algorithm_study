"""
pypy3에서는 통과, python3에서는 시간 초과
"""

from sys import stdin

# 상우하좌
dr = [-1 , 0, 1, 0]
dc = [0, 1, 0, -1]


def is_max_dust_over_5():
    """
    한 칸에 있는 미세먼지의 최대값이 5 이상인지 구한다.
    """
    global board, R, C

    for r in range(R):
        for c in range(C):
            if board[r][c] >= 5:
                return True

    return False


def dust_diffusion():
    """
    1초가 지난 후 먼지의 확산 결과를 구한다.
    """
    global board, R, C

    new_board = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            # 먼지의 양이 5 이상인 경우에만 확산이 발생한다.
            if board[r][c] >= 5:
                dust = board[r][c] // 5

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        new_board[nr][nc] += dust
                        board[r][c] -= dust

    for r in range(R):
        for c in range(C):
            board[r][c] += new_board[r][c]



def cleaner():
    """
    공기청정기가 순환한 이후의 먼지의 결과를 구한다.
    """
    global board, R, C, cleaner_idx

    # 위쪽 공기청정기의 바람은 반시계방향으로 순환한다.
    i = 0
    nr, nc = cleaner_idx - 1, 0
    board[nr][nc] = 0

    for _ in range(4):
        while True:
            if 0 <= nr + dr[i] <= cleaner_idx and 0 <= nc + dc[i] < C:
                board[nr][nc] = board[nr + dr[i]][nc + dc[i]]
                nr, nc = nr + dr[i], nc + dc[i]
            else:
                break
        i += 1

    board[cleaner_idx][1] = 0

    # 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    i = 2
    nr, nc = cleaner_idx + 2, 0
    board[nr][nc] = 0

    for _ in range(4):
        while True:
            if cleaner_idx + 1 <= nr + dr[i] < R and 0 <= nc + dc[i] < C:
                board[nr][nc] = board[nr + dr[i]][nc + dc[i]]
                nr, nc = nr + dr[i], nc + dc[i]
            else:
                break
        i -= 1

    board[cleaner_idx + 1][1] = 0


R, C, T = map(int, stdin.readline().split())
board = []

for _ in range(R):
    board.append([int(x) for x in stdin.readline().split()])

# 공기청정기의 위치를 저장한다.
for r in range(R):
    if board[r][0] == -1:
        cleaner_idx = r
        break

for _ in range(T):
    # 한 칸의 먼지의 최대값이 5보다 작은 경우 확산이 발생하지 않는다.
    if is_max_dust_over_5():
        dust_diffusion()
    cleaner()

print(sum([sum(x) for x in board]) + 2)

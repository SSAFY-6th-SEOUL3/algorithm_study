N, M = map(int, input().split())
r, c, i = map(int, input().split())

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

FRONT, RIGHT, BACK, LEFT = 0, 1, 2, 3


def get_near_position(r, c, i, near_dir):
    """
    (r, c)에 있고 i 방향을 보고 있는 로봇 청소기와 near_dir쪽으로 인접한 칸의 좌표를 구한다.
    ex. (2, 2)에 있고 북쪽을 보고 있는 청소기의 왼쪽 인접 칸 = (2, 1)
    """
    return r + dr[(i + near_dir) % 4], c + dc[(i + near_dir) % 4]


cleaned = [[False] * M for _ in range(N)]
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

while True:
    search_count = 0

    # 1. 현재 위치를 청소한다.
    cleaned[r][c] = True

    # 2. 현재 위치에서 현재 방향 기준 왼쪽 칸부터 차례대로 인접한 칸을 탐색한다.
    while search_count < 4:
        # a. 왼쪽 방향에 청소하지 않은 공간이 있다면
        nr, nc = get_near_position(r, c, i, LEFT)

        if board[nr][nc] == 0 and not cleaned[nr][nc]:
            # 그 방향으로 회전한 다음, 한 칸을 전진하고 1번으로 돌아간다.
            i = (i - 1) % 4
            r, c = nr, nc
            break

        # b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 탐색을 이어간다.
        i = (i - 1) % 4
        search_count += 1

    # c. 네 방향 모두 청소가 되어 있거나 벽이라면
    if search_count >= 4:
        nr, nc = get_near_position(r, c, i, BACK)

        # d. 뒤쪽 칸이 벽인 경우, 작동을 멈춘다.
        if board[nr][nc] == 1:
            break

        # 뒤쪽 칸이 벽이 아닌 경우, 한 칸 후진하고 다시 2번부터 시작한다.
        r, c = nr, nc

# 로봇 청소기가 청소하는 칸의 개수를 출력한다.
print(sum([sum(arr) for arr in cleaned]))

from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def rotate_population():
    """
    인구 이동을 수행한다.

    Returns:
        인구 이동이 발생하면 True, 발생하지 않으면 False
    """
    global board, N, L, R

    # connects[i][j][k] : A[r][c]의 나라가 k 방향으로 인접한 나라와 국경선을 여는지의 여부
    connects = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]

    is_connect = False

    # 열리는 국경선을 모두 connects에 저장한다.
    # 1. 좌우로 인접한 경우
    for r in range(N):
        for c in range(N - 1):
            if L <= abs(board[r][c] - board[r][c + 1]) <= R:
                connects[r][c][1] = 1
                connects[r][c + 1][3] = 1
                is_connect = True

    # 2. 상하로 인접한 경우
    for r in range(N - 1):
        for c in range(N):
            if L <= abs(board[r][c] - board[r + 1][c]) <= R:
                connects[r][c][2] = 1
                connects[r + 1][c][0] = 1
                is_connect = True

    # 열리는 국경선이 하나도 없다면 False를 리턴한다.
    if not is_connect:
        return False

    # 열리는 국경선이 있다면, 인구 이동을 수행한 뒤 True를 리턴한다.
    visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                count = 1
                total = board[r][c]
                cnt_nodes = [(r, c)]

                stack = deque()
                stack.append((r, c))
                visited[r][c] = True

                while stack:
                    cnt_r, cnt_c = stack.pop()

                    for i in range(4):
                        if connects[cnt_r][cnt_c][i]:
                            nr, nc = cnt_r + dr[i], cnt_c + dc[i]

                            if not visited[nr][nc]:
                                count += 1
                                total += board[nr][nc]
                                visited[nr][nc] = True

                                cnt_nodes.append((nr, nc))
                                stack.append((nr, nc))

                if count > 1:
                    avg_value = total // count

                    for nr, nc in cnt_nodes:
                        board[nr][nc] = avg_value

    return True


N, L, R = map(int, input().split())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

rotate_count = 0

while True:
    result = rotate_population()

    if not result:
        break

    rotate_count += 1

print(rotate_count)

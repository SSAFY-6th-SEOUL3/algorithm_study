from itertools import product


def get_watchable_areas(nr, nc):
    """
    (nr, nc)에서 사방으로 감시할 수 있는 구역 set을 탐색한다.
    Returns:
        areas: (nr, nc)에서 사방으로 감시 가능한 구역 set를 담은 배열
    """
    global board, N, M
    areas = []

    # 상우하좌 방향으로 각각 cctv가 감시 가능한 공간의 set를 areas에 추가한다.
    for i in range(4):
        r, c = nr, nc
        sub_area = set()

        # 좌표가 범위를 벗어났거나, 벽을 만난 경우 탐색을 종료한다.
        while 0 <= r < N and 0 <= c < M and board[r][c] != 6:
            if board[r][c] == 0:
                sub_area.add((r, c))
            r, c = r + dr[i], c + dc[i]

        areas.append(sub_area)

    return areas


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

total_areas = []
cctv_count = 0
empty_count = 0

for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            empty_count += 1

        if 1 <= board[r][c] <= 5:
            cctv_count += 1

        if board[r][c] == 1:
            total_areas.append(get_watchable_areas(r, c))
        elif board[r][c] == 2:
            up, right, down, left = get_watchable_areas(r, c)
            total_areas.append(
                [up | down, left | right]
            )
        elif board[r][c] == 3:
            up, right, down, left = get_watchable_areas(r, c)
            total_areas.append([
                up | right, right | down, down | left, left | up
            ])
        elif board[r][c] == 4:
            up, right, down, left = get_watchable_areas(r, c)
            all_sides = up | right | down | left
            total_areas.append(
                [all_sides - up, all_sides - down, all_sides - left, all_sides - right]
            )
        elif board[r][c] == 5:
            up, right, down, left = get_watchable_areas(r, c)
            total_areas.append([up | right | down | left])

least_hidden_area = empty_count

"""
itertools 모듈의 product => 데카르트 곱을 구한다.
예를 들어, A가 'abc'이고 B가 'XY'면, product(A, B)는 (aX, aY, bX, bY, cX, cY)다.

total_areas에는 각 cctv에서 볼 수 있는 공간들의 set에 저장되어 있으므로
이것의 product는 모든 경우에 대하여 각 cctv가 볼 수 있는 공간을 담은 데이터를 리턴한다.
"""
for area_set in list(product(*total_areas)):
    watched_areas = set()

    """
    area_set[i]는 i번째(0부터 시작) cctv가 볼 수 있는 공간의 set다.
    이것들을 모두 합집합 연산으로 더하면, 
    현재 경우에서 cctv가 볼 수 있는 모든 공간이 watched_areas에 저장된다. 
    """
    for i in range(cctv_count):
        watched_areas |= area_set[i]

    # 현재 경우의 사각지대의 개수 = 빈 공간의 개수 - cctv가 볼 수 있는 공간의 개수
    least_hidden_area = min(least_hidden_area, empty_count - len(watched_areas))

print(least_hidden_area)

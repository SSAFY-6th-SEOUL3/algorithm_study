
def get_next_curve(points):
    """
    주어진 드래곤 커브 좌표 리스트에 대하여, 다음 세대의 좌표 리스트를 구한다.
    """
    last_point_x, last_point_y = points[-1]
    p_len = len(points)

    # 마지막 좌표를 제외한, 현재 드래곤 커브의 각 좌표 (x, y)에 대하여
    # 해당 좌표를 마지막 좌표를 기준으로 90도 돌린 새로운 좌표를 구해 points에 추가한다.
    # 주의: 이때, 마지막 좌표에서 가까운 좌표부터 추가해야 함!
    for i in range(p_len - 2, -1, -1):
        new_x = last_point_x - (points[i][1] - last_point_y)
        new_y = last_point_y + (points[i][0] - last_point_x)
        points.append((new_x, new_y))

    return points


N = int(input())
board = [[False] * 101 for _ in range(101)]

# 우상좌하 (문제의 조건에 따름)
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    points = [(x, y), (x + dc[d], y + dr[d])]

    for _ in range(g):
        points = get_next_curve(points)

    for x, y in points:
        board[y][x] = True

total_count = 0

for r in range(100):
    for c in range(100):
        if board[r][c] and board[r + 1][c] and board[r][c + 1] and board[r + 1][c + 1]:
            total_count += 1

print(total_count)

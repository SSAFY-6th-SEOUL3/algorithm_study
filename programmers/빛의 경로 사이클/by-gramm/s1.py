# 완전탐색 (각 좌표에서 4개 방향으로 가는 경로를 모두 탐색한다.)


# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solution(grid):
    r_len, c_len = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(c_len)] for _ in range(r_len)]
    distances = []

    for r in range(r_len):
        for c in range(c_len):
            for z in range(4):
                # (r, c)에서 z 방향으로 가는 사이클이 없었다면
                if not visited[r][c][z]:
                    # 해당 경로를 포함하는 사이클을 탐색한다.
                    nr, nc = r, c
                    visited[nr][nc][z] = True
                    distance, i = 0, z

                    while True:
                        # 위치를 업데이트한다.
                        nr, nc = (nr + dr[i]) % r_len, (nc + dc[i]) % c_len
                        # 거리와 방향을 업데이트한다.
                        distance += 1
                        if grid[nr][nc] == 'L':
                            i = (i - 1) % 4
                        elif grid[nr][nc] == 'R':
                            i = (i + 1) % 4

                        # 해당 위치와 방향에 해당하는 경로를 이미 지났다면
                        if visited[nr][nc][i]:
                            # 사이클의 길이를 저장한 뒤, 탐색을 종료한다.
                            distances.append(distance)
                            break

                        visited[nr][nc][i] = True

    # 거리를 오름차순한 결과를 리턴한다.
    return sorted(distances)

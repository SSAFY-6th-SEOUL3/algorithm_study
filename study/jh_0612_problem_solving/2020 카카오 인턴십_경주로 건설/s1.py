from heapq import heappush, heappop

# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solution(board):
    N = len(board)
    min_distance = 12345679

    # distances[r][c][i]: i 방향으로 (r, c)에 진입하는 최소 거리
    distances = [[[12345679] * 4 for _ in range(N)] for _ in range(N)]

    # heap에 (거리, 열, 행, 방향)을 저장한다.
    # 방향의 경우, 상/우/하/좌가 각각 0/1/2/3이다.
    heap = []

    if board[0][1] == 0:  # 시작점에서 오른쪽으로 이동 가능한 경우
        heap.append((100, 0, 1, 1))
    if board[1][0] == 0:  # 시작점에서 아래쪽으로 이동 가능한 경우
        heap.append((100, 1, 0, 2))

    while heap:
        distance, cnt_r, cnt_c, direction = heappop(heap)

        if min_distance <= distance:  # min_distance보다 짧은 경로가 존재하지 않는 경우 => 탐색 종료
            break

        for i in range(4):
            if (direction + 2) % 4 == i:  # 왔던 방향으로 되돌아가는 경우
                continue
            elif direction == i:  # 왔던 방향으로 계속 가는 경우
                new_distance = distance + 100
            else:  # 방향을 90도로 꺾는 경우
                new_distance = distance + 600

            nr, nc = cnt_r + dr[i], cnt_c + dc[i]

            if nr == N - 1 and nc == N - 1:  # 도착점에 도달한 경우
                min_distance = min(min_distance, new_distance)
            elif 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                if new_distance < distances[nr][nc][i]:
                    distances[nr][nc][i] = new_distance
                    heappush(heap, (new_distance, nr, nc, i))

    return min_distance

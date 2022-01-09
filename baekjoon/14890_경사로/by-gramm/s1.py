from sys import stdin


def check_route(arr):
    """
    주어진 경로에 경사로를 놓아 길을 만들 수 있는지 확인한다.
    """
    global N, L
    visited = [False] * N  # 경사로를 놓은 위치를 저장한다.

    for c in range(1, N):
        diff = arr[c - 1] - arr[c]

        # 높이 차이가 2 이상 => 탐색 중단
        if abs(diff) >= 2:
            return False

        # 오른쪽이 1만큼 높은 경우 => 왼쪽에 경사로를 놓을 수 있는지 확인
        if diff == -1:
            if c < L:
                return False

            for i in range(c - L, c):
                if visited[i] or arr[i] != arr[c - 1]:
                    return False
                visited[i] = True

        # 왼쪽이 1만큼 높은 경우 => 오른쪽에 경사로를 놓을 수 있는지 확인
        if diff == 1:
            if c + L > N:
                return False

            for i in range(c, c + L):
                if visited[i] or arr[i] != arr[c]:
                    return False
                visited[i] = True

    return True


N, L = map(int, stdin.readline().split())
board = []

for _ in range(N):
    board.append([int(x) for x in stdin.readline().split()])

total_count = 0

for idx in range(N):
    # 가로로 가는 경로 탐색
    if check_route(board[idx]):
        total_count += 1

    # 세로로 가는 경로 탐색
    if check_route([arr[idx] for arr in board]):
        total_count += 1

print(total_count)

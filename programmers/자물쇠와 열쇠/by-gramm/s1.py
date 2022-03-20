def rotate_key(key, M):
    """
    열쇠를 시계 방향으로 90도 회전시킨다.
    """
    temp = []
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                temp.append((i, j))

    new_arr = [[0] * M for _ in range(M)]

    for r, c in temp:
        new_arr[c][M - 1 - r] = 1

    return new_arr


def check_key(key, lock, start_r, start_c, M, N):
    """
    열쇠가 (start_r, start_c) 위치에서 자물쇠에 들어가는지의 여부를 확인한다.
    """
    for i in range(M):
        for j in range(M):
            if 0 <= start_r + i < N and 0 <= start_c + j < N:
                if key[i][j] + lock[start_r + i][start_c + j] != 1:
                    return False

    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    min_r, max_r = N - 1, 0
    min_c, max_c = N - 1, 0

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                min_r, max_r = min(min_r, i), max(max_r, i)
                min_c, max_c = min(min_c, j), max(max_c, j)

    r_length = max_r - min_r + 1  # 열쇠가 차지하는 영역의 세로 길이
    c_length = max_c - min_c + 1  # 열쇠가 차지하는 영역의 가로 길이

    # 열쇠를 90도 방향으로 돌려가며 자물쇠에 들어가는지 여부를 확인한다.
    for i in range(4):
        if i > 0:
            key = rotate_key(key, M)

        for start_r in range(min_r - (M - r_length), min_r + 1):
            for start_c in range(min_c - (M - c_length), min_c + 1):
                if check_key(key, lock, start_r, start_c, M, N):
                    return True

    return False

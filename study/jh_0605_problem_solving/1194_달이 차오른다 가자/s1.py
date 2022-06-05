from sys import stdin
from collections import deque
from itertools import combinations
from copy import deepcopy


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def keys_to_num(keys):
    """
    ex. 열쇠 'a' ~ 'f'의 소유 여부가 각각 [1, 0, 1, 1, 0, 1]인 경우 => 45 리턴
    """
    return sum([keys[i] * (2 ** i) for i in range(6)])


def get_key_subset(keys):
    """
    ex. keys가 [0, 0, 1, 0, 1, 0] => [0, 4, 16, 20] 리턴
    """
    nums = []
    sub_sums = [0]

    for i in range(6):
        if keys[i]:
            nums.append(2 ** i)

    for i in range(1, len(nums) + 1):
        for sub_sum in combinations(nums, i):
            sub_sums.append(sum([int(x) for x in sub_sum]))

    return sub_sums


def find_min_distance(board, N, M):
    """
    Args:
        board: 미로
        N: 미로의 세로 길이
        M: 미로의 가로 길이

    Returns:
        미로를 탈출하는 이동 횟수의 최솟값
    """

    # distances[r][c][x]: x의 열쇠 조합을 가지고 board[r][c]에 방문하는 최소 거리
    # ex. x가 11 => 11 = 001011(2)이므로, (c, e, f)의 열쇠를 가지고 있는 경우
    distances = [[[1234567] * 64 for _ in range(M)] for _ in range(N)]

    # 현재 위치를 위치를 저장한다.
    for r in range(N):
        for c in range(M):
            if board[r][c] == '0':
                start_r, start_c = r, c
                board[r][c] = '.'

    queue = deque([[start_r, start_c, 0, [0, 0, 0, 0, 0, 0]]])
    distances[start_r][start_c][0] = 0

    while queue:
        cnt_r, cnt_c, distance, keys = queue.popleft()

        for i in range(4):
            nr, nc = cnt_r + dr[i], cnt_c + dc[i]

            if not (0 <= nr < N and 0 <= nc < M):      # 미로의 범위를 벗어난 경우 => 탐색 중단
                continue
            elif board[nr][nc] == '#':                 # 이동할 위치가 벽인 경우 => 탐색 중단
                continue
            elif board[nr][nc] in 'ABCDEF':            # 이동할 위치가 문인데 맞는 열쇠가 없는 경우 => 탐색 중단
                if not keys[ord(board[nr][nc]) - 65]:
                    continue
            elif board[nr][nc] == '1':                 # 출구를 찾은 경우
                return distance + 1

            new_keys = deepcopy(keys)

            if board[nr][nc] in 'abcdef':              # 이동할 위치에 열쇠가 있는 경우
                new_keys[ord(board[nr][nc]) - 97] = 1

            key_num = keys_to_num(new_keys)

            if distances[nr][nc][key_num] <= distance + 1:
                continue
            else:
                key_num_list = get_key_subset(new_keys)

                for idx in key_num_list:
                    distances[nr][nc][idx] = min(distances[nr][nc][idx], distance + 1)

                queue.append([nr, nc, distance + 1, new_keys])

    return -1


N, M = map(int, stdin.readline().split())
board = []

for _ in range(N):
    board.append([x for x in stdin.readline().rstrip()])

print(find_min_distance(board, N, M))

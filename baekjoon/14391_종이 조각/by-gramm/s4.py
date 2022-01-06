"""
s3.py 리팩토링
"""

def get_max_sum(current, start_r, end_r, start_c, end_c):
    global board, inversed_board, max_value

    # 더 이상 남은 종이 조각이 없는 경우 => max_value를 업데이트한다.
    if start_r > end_r or start_c > end_c:
        max_value = max(max_value, current)
        return

    # 1) 위쪽 면을 자르는 경우
    up = int(board[start_r][start_c:end_c + 1])
    get_max_sum(current + up, start_r + 1, end_r, start_c, end_c)

    # 2) 아래쪽 면을 자르는 경우
    if end_r > start_r:  # 세로 길이가 2 이상일 때만 탐색한다. (길이가 1이면 위쪽 면과 같으므로)
        down = int(board[end_r][start_c:end_c + 1])
        get_max_sum(current + down, start_r, end_r - 1, start_c, end_c)

    # 3) 왼쪽 면을 자르는 경우
    left = int(inversed_board[start_c][start_r:end_r + 1])
    get_max_sum(current + left, start_r, end_r, start_c + 1, end_c)

    # 4) 오른쪽 면을 자르는 경우
    if end_c > start_c:  # 가로 길이가 2 이상일 때만 탐색한다.
        right = int(inversed_board[end_c][start_r:end_r + 1])
        get_max_sum(current + right, start_r, end_r, start_c, end_c - 1)


N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(input())

inversed_board = []

for c in range(M):
    inversed_board.append("".join([arr[c] for arr in board]))

max_value = 0
get_max_sum(0, 0, N - 1, 0, M - 1)
print(max_value)

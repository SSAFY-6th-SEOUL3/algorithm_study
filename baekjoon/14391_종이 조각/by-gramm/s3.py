"""
규칙 : 점수가 최댓값이 되려면, 합칠 수 있는 종이 조각이 더 이상 없어야 한다.
증명 : 두 숫자 A와 B를 합칠 때, (AB) = 10A + B이므로, 이는 반드시 A + B보다 크거나 같다.

s2.py가 실패한 이유 : 아래나 오른쪽에서부터 채우는 경우를 고려하지 못한다.
새로운 접근 : 매번 남은 직사각형에서 한쪽 면 전체를 조각으로 자른다.

성공!
"""

def get_max_sum(current_value, start_r, end_r, start_c, end_c):
    global board, max_value

    # 더 이상 남은 종이 조각이 없는 경우 => max_value를 업데이트한다.
    if start_r > end_r or start_c > end_c:
        max_value = max(max_value, current_value)
        return

    # 1) 위쪽 면을 자르는 경우
    str_num = ""
    for nc in range(start_c, end_c + 1):
        str_num += board[start_r][nc]
    get_max_sum(current_value + int(str_num), start_r + 1, end_r, start_c, end_c)

    # 2) 아래쪽 면을 자르는 경우
    if end_r > start_r:  # 세로 길이가 2 이상일 때만 탐색한다. (길이가 1이면 위쪽 면과 같으므로)
        str_num = ""
        for nc in range(start_c, end_c + 1):
            str_num += board[end_r][nc]
        get_max_sum(current_value + int(str_num), start_r, end_r - 1, start_c, end_c)

    # 3) 왼쪽 면을 자르는 경우
    str_num = ""
    for nr in range(start_r, end_r + 1):
        str_num += board[nr][start_c]
    get_max_sum(current_value + int(str_num), start_r, end_r, start_c + 1, end_c)

    # 4) 오른쪽 면을 자르는 경우
    if end_c > start_c:  # 가로 길이가 2 이상일 때만 탐색한다.
        str_num = ""
        for nr in range(start_r, end_r + 1):
            str_num += board[nr][end_c]
        get_max_sum(current_value + int(str_num), start_r, end_r, start_c, end_c - 1)


N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([x for x in list(input())])

max_value = 0

get_max_sum(0, 0, N - 1, 0, M - 1)
print(max_value)

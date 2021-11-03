
"""
아래와 같은 형태로 2차원 배열에 수를 저장한다.
1  0  0  0  0
2  12 0  0  0
3  13 11 0  0
4  14 15 10 0
5  6  7  8  9
"""

def solution(n):
    # 왼쪽 아래 / 오른쪽 / 왼쪽 위로
    dr = [1, 0, -1]
    dc = [0, 1, -1]

    board = [[0] * n for _ in range(n)]
    board[0][0] = 1

    r, c = 0, 0
    i = 0

    # 1부터 (n^2 + n) // 2까지 모든 수를 다 채울 때까지 반복한다.
    for num in range(2, n * (n + 1) // 2 + 1):
        r, c = r + dr[i], c + dc[i]

        # 유효 범위를 벗어나거나 이미 수가 채워진 공간이라면
        if not (0 <= r < n and 0 <= c < n) or board[r][c]:
            r, c = r - dr[i], c - dc[i]  # 원래 좌표로 되돌린 후에
            i = (i + 1) % 3  # 방향을 틀고
            r, c = r + dr[i], c + dc[i]  # 다시 새로운 좌표로 이동한다.

        board[r][c] = num

    answer = []

    # 2차원 배열의 각 열의 0이 아닌 수들을 answer에 더한다.
    for idx, sub_board in enumerate(board):
        answer += sub_board[:idx + 1]

    return answer

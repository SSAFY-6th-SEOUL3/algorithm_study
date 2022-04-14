"""
이전 풀이 => 테스트케이스 실행 시간 약 3.37s
현재 풀이 => 테스트케이스 실행 시간 약 0.38s
"""


for _ in range(10):
    tc = int(input().readline())
    max_length = 1
    board = []

    for _ in range(100):
        board.append([x for x in input().rstrip()])

    # 1. 길이가 홀수인 회문의 최대 길이를 구한다.
    for r in range(100):
        for c in range(100):
            # 1-1. board[r][c]를 중심으로 하는 가로 회문의 최대 길이를 구한다.
            width = 1
            left, right = c - 1, c + 1

            while 0 <= left and right < 100 and board[r][left] == board[r][right]:
                width += 2
                left, right = left - 1, right + 1

            # 1-2. board[r][c]를 중심으로 하는 세로 회문의 최대 길이를 구한다.
            height = 1
            up, down = r - 1, r + 1

            while 0 <= up and down < 100 and board[up][c] == board[down][c]:
                height += 2
                up, down = up - 1, down + 1

            max_length = max(max_length, width, height)

    # 2. 길이가 홀수인 세로 회문의 최대 길이를 구한다.
    for r in range(100):
        for c in range(100):
            # 2-1. board[r][c], board[r][c + 1]을 중심으로 하는 가로 회문의 최대 길이를 구한다.
            width = 0
            left, right = c, c + 1

            while 0 <= left and right < 100 and board[r][left] == board[r][right]:
                width += 2
                left, right = left - 1, right + 1

            # 2-2. board[r][c], board[r + 1][c]을 중심으로 하는 세로 회문의 최대 길이를 구한다.
            height = 0
            up, down = r, r + 1

            while 0 <= up and down < 100 and board[up][c] == board[down][c]:
                height += 2
                up, down = up - 1, down + 1

            max_length = max(max_length, width, height)

    print(f"{tc} {max_length}")

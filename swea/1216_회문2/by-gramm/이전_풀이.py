def is_palindrome(word):
    """
    주어진 문자열이 회문인지 검사한다.
    Returns:
        주어진 문자열이 회문이면 True, 회문이 아니면 False
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def get_longest_palindrome_length(board, N):
    """
    문자열로 이루어진 배열에서 가장 긴 회문의 길이를 구한다.
    Args:
        board: 문자열 배열
        N: 문자열 하나의 길이 및 문자열의 개수
    Returns:
        l: 문자열 배열 내의 가장 긴 회문의 길이
    """
    for l in range(N, 1, -1):
        # 1. 가로 회문 탐색
        for r in range(N):
            for c in range(N - l + 1):
                # current: board[r][c]에서 시작하는 길이 M의 가로 부분 문자열
                current = board[r][c:c + l]

                if is_palindrome(current):
                    return l

        # 2. 세로 회문 탐색
        for c in range(N):
            for r in range(N - l + 1):
                # current: board[r][c]에서 시작하는 길이 M의 세로 부분 문자열
                current = ''
                for cnt_r in range(r, r + l):
                    current += board[cnt_r][c]

                if is_palindrome(current):
                    return l

    # 길이가 2 이상인 회문이 없는 경우
    return 1


T, N = 10, 100

for _ in range(T):
    tc = int(input())
    board = []

    for _ in range(N):
        board.append(input())

    count = get_longest_palindrome_length(board, N)
    print("#{} {}".format(tc, count))

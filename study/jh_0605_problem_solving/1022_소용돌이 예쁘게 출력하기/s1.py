"""
r, c의 절대값 중 큰 값이
0 => 1
1 => 2~9 (8개)
2 => 10~25 (16개)
3 => 26~49 (24개)
"""

def get_value(r, c):
    level = max(abs(r), abs(c))           # 중앙의 1을 몇번째로 감싸는 정사각형인지
    start = 4 * level * (level - 1) + 1   # level번째 정사각형의 시작 번호

    # 번호가 오른쪽에 속하는 경우
    if c == level and r != level:
        return start + (level - r)
    # 번호가 위쪽에 속하는 경우
    elif r == -level:
        return start + level * 2 + (level - c)
    # 번호가 왼쪽에 속하는 경우
    elif c == -level:
        return start + level * 4 + (level + r)
    # 번호가 아래쪽에 하는 경우
    else:
        return start + level * 6 + (level + c)


r1, c1, r2, c2 = map(int, input().split())

r_count = r2 - r1 + 1
c_count = c2 - c1 + 1

board = [[0] * c_count for _ in range(r_count)]

for r in range(r_count):
    for c in range(c_count):
        board[r][c] = get_value(r1 + r, c1 + c)

max_value = max(board[0][0],
                board[0][c_count - 1],
                board[r_count - 1][0],
                board[r_count - 1][c_count - 1])
max_len = len(str(max_value))

for numbers in board:
    print(" ".join([" " * (max_len - len(str(num))) + str(num) for num in numbers]))

# s1.py에서 주사위를 굴리는 부분을 numbers_after_roll로 단순화함.

# 1 : 동 / 2 : 서 / 3 : 북 / 4 : 남
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

numbers_after_roll = [
    [],
    [2, 3, 1, 0, 4, 5],  # 주사위를 동쪽으로 굴리는 경우
    [3, 2, 0, 1, 4, 5],  # 주사위를 서쪽으로 굴리는 경우
    [5, 4, 2, 3, 0, 1],  # 주사위를 북쪽으로 굴리는 경우
    [4, 5, 2, 3, 1, 0]   # 주사위를 남쪽으로 굴리는 경우
]


def roll_dice(dice, i):
    global r, c

    if not (0 <= r + dr[i] < N and 0 <= c + dc[i] < M):
        return

    r, c = r + dr[i], c + dc[i]

    nums = numbers_after_roll[i]
    """
    s1.py에서 바뀐 부분
    """
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] \
        = dice[nums[0]], dice[nums[1]], dice[nums[2]], dice[nums[3]], dice[nums[4]], dice[nums[5]]

    if not board[r][c]:
        board[r][c] = dice[1]
    else:
        dice[1] = board[r][c]
        board[r][c] = 0

    print(dice[0])


N, M, r, c, K = map(int, input().split())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

dice = [0, 0, 0, 0, 0, 0]

commands = [int(x) for x in input().split()]

for command in commands:
    roll_dice(dice, command)

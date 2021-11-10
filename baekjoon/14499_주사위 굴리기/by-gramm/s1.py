
# 1 : 동 / 2 : 서 / 3 : 북 / 4 : 남
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def roll_dice(dice, i):
    """
    Args:
        dice: 주사위의 숫자 정보를 담은 배열
              (위 / 아래 / 왼쪽 / 오른쪽 / 앞쪽 / 뒤쪽의 숫자)
        in: 주사위를 굴리는 방향
    """
    global r, c

    # 주사위를 지도 내에서 이동시킬 수 없다면 => 명령을 무시한다.
    if not (0 <= r + dr[i] < N and 0 <= c + dc[i] < M):
        return

    # 주사위의 위치를 업데이트한다.
    r, c = r + dr[i], c + dc[i]

    # 주사위를 동쪽으로 굴리는 경우
    if i == 1:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    # 주사위를 서쪽으로 굴리는 경우
    elif i == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    # 주사위를 북쪽으로 굴리는 경우
    elif i == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    # 주사위를 남쪽으로 굴리는 경우
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]

    if not board[r][c]:         # 주사위가 놓인 칸에 쓰여 있는 수가 0이면
        board[r][c] = dice[1]   # 주사위 바닥면의 수가 칸에 복사된다.
    else:                       # 0이 아닌 경우에는
        dice[1] = board[r][c]   # 칸에 쓰여 있는 수가 바닥면에 복사되며
        board[r][c] = 0         # 칸에 쓰여 있는 수는 0이 된다.

    print(dice[0])              # 이동할 때마다 주사위 윗면의 수를 출력한다.


# 문제에서는 주사위의 좌표를 x, y로 받았지만 임의로 r, c로 받음.
N, M, r, c, K = map(int, input().split())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

# 각각 위 / 아래 / 왼쪽 / 오른쪽 / 앞쪽 / 뒤쪽의 숫자
dice = [0, 0, 0, 0, 0, 0]

commands = [int(x) for x in input().split()]

for command in commands:
    roll_dice(dice, command)

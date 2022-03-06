import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def run_cleaner(board, position_list):

    # new_board 이차원 배열에 확산된 미세먼지 새로 저장
    new_board = [[0] * C for _ in range(R)]

    for r, c in position_list:
        next_pos = []   # next_pos: r, c 기준으로 상하좌우 확산 가능한 좌표 리스트
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C or (nr, nc) in set(cleaner_pos):
                continue
            next_pos.append((nr, nc))

        if len(next_pos) == 0:
            continue

        # next_dust: 상하좌우로 뿌려줄 미세먼지 양
        next_dust = board[r][c] // 5

        # r, c 좌표에서 상하좌우로 미세먼지 확산
        new_board[r][c] += board[r][c] - next_dust * len(next_pos)
        for y, x in next_pos:
            new_board[y][x] += next_dust

    # 공기청정기 돌리기(윗부분, 반시계 방향)
    cr1, cc1 = cleaner_pos[0]
    cc1 += 1
    prev_dust1 = 0

    while (cr1, cc1) != cleaner_pos[0]:

        cur_dust1 = new_board[cr1][cc1]
        new_board[cr1][cc1] = prev_dust1
        prev_dust1 = cur_dust1

        if cr1 == cleaner_pos[0][0] and cc1 + 1 < C:
            cc1 += 1
        elif cc1 == C - 1 and cr1 - 1 >= 0:
            cr1 -= 1
        elif cr1 == 0 and cc1 - 1 >= 0:
            cc1 -= 1
        elif cc1 == 0:
            cr1 += 1

    # 공기청정기 돌리기(아랫부분, 시계 방향)
    cr2, cc2 = cleaner_pos[1]
    cc2 += 1
    prev_dust2 = 0

    while (cr2, cc2) != cleaner_pos[1]:

        cur_dust2 = new_board[cr2][cc2]
        new_board[cr2][cc2] = prev_dust2
        prev_dust2 = cur_dust2

        if cr2 == cleaner_pos[1][0] and cc2 + 1 < C:
            cc2 += 1
        elif cc2 == C - 1 and cr2 + 1 < R:
            cr2 += 1
        elif cr2 == R - 1 and cc2 - 1 >= 0:
            cc2 -= 1
        elif cc2 == 0:
            cr2 -= 1

    # position_list: 새로운 미세먼지 좌표 저장
    position_list = []
    for r in range(R):
        for c in range(C):
            if new_board[r][c]:
                position_list.append((r, c))

    return new_board, position_list


R, C, T = map(int, input().split())
dust_board = []     # 미세먼지 포함한 이차원 배열
dust_pos = []       # 미세먼지 좌표 리스트
cleaner_pos = []    # 공기청정기 좌표 리스트
for i in range(R):
    tmp = list(map(int, input().split()))
    dust_board.append(tmp)
    for j in range(C):
        if tmp[j] != 0 and tmp[j] != -1:
            dust_pos.append((i, j))
        if tmp[j] == -1:
            cleaner_pos.append((i, j))

for _ in range(T):
    dust_board, dust_pos = run_cleaner(dust_board, dust_pos)

total = 0
for db in dust_board:
    total += sum(db)

print(total)


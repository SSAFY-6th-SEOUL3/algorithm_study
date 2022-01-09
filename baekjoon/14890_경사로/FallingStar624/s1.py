import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board_T = list(map(list, zip(*board)))


def slope(line):
    before = 1
    now = 0
    while now < N-1:
        # 높이 차이가 2 이상이면 탐색 종료
        if abs(line[now] - line[now+1]) > 1:
            return 0
        # 높이가 같으면 계속 진행
        if line[now] == line[now+1]:
            now += 1
            before += 1
            continue
        # 높이가 다르면
        else:
            # 높아지는 경우
            if line[now] < line[now+1]:
                if before >= L:
                    now += 1
                    before = 1
                else:
                    return 0
            # 낮아지는 경우
            else:
                if now+L <= N-1 and len(set(line[now+1:now+(L+1)])) == 1:
                    now += L
                    before = 0
                else:
                    return 0
    else:
        return 1


cnt = 0
for col in board:
    cnt += slope(col)
for col in board_T:
    cnt += slope(col)
print(cnt)
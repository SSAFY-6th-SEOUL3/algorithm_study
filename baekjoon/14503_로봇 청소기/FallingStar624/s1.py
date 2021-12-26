import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
room = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    room.append(tmp)

cleaned = 0


def cleaning(row, col, direction):
    global cleaned, room
    # 1. 현재 위치 청소
    if room[row][col] == 0:
        room[row][col] = 2
        cleaned += 1

    # 2. 왼쪽 방향 탐색
    for i in range(1, 5):
        next_r, next_c = row + dr[(direction-i) % 4], col + dc[(direction-i) % 4]
        # 청소가 안됐으면 그 방향으로 회전한 다음 한 칸 전진 + 1번으로
        if room[next_r][next_c] == 0:
            return cleaning(next_r, next_c, (direction-i) % 4)
        else:
            continue
    else:
        # 후진하고 2번 실행
        next_r, next_c = row + dr[(direction - 2) % 4], col + dc[(direction - 2) % 4]
        if room[next_r][next_c] != 1:
            return cleaning(next_r, next_c, direction)
        # 뒤쪽방향이 벽이면 stop
        else:
            return


cleaning(r, c, d)
print(cleaned)










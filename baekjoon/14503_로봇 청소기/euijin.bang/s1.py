# 디버깅중............

import sys
sys.stdin = open("14503.txt")

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

s = (r, c)

stack = [s]
visited = []

def direction(d, now):
    if d == 3:
        return (now[0], now[1]-1)
    elif d == 2:
        return (now[0]+1, now[1])
    elif d == 1:
        return (now[0], now[1]+1)
    else:
        return (now[0]-1, now[1])

def rear(d, now):
    if d == 3:
        return (now[0], now[1] + 1)
    elif d == 2:
        return (now[0] - 1, now[1])
    elif d == 1:
        return (now[0], now[1] - 1)
    else:
        return (now[0] + 1, now[1])

while stack:
    now = stack.pop()
    if now not in visited:
        visited.append(now)  # 현재 위치를 청소한다.

    # 현재 방향을 기준으로 왼쪽 방향부터 인접칸을 탐색한다.
    for _ in range(4):
        if d == 3:
            next = direction(d-1, now)

            # 다음 칸이 청소가 되어있지 않고 벽이 아니라면
            if next not in visited and board[next[0]][next[1]] == 0:
                now = next
                stack.append(now)
                visited.append(now)

            # 다음 칸이 청소는 되어있고 벽이 아니라면
            elif next in visited and board[next[0]][next[1]] == 0:
                # 그 방향으로 회전하고 왼쪽 방향부터 다시 탐색한다.
                d = d-1
                if d == -1:
                    d = 3

            # 다음 칸이 벽이라면 왼쪽으로 돌아서 탐색한다.
            else:
                d = d-1
                if d == -1:
                    d = 3

        elif d == 2:
            next = direction(d-1, now)

            # 다음 칸이 청소가 되어있지 않고 벽이 아니라면
            if next not in visited and board[next[0]][next[1]] == 0:
                now = next
                stack.append(now)
                visited.append(now)

            # 다음 칸이 청소는 되어있고 벽이 아니라면
            elif next in visited and board[next[0]][next[1]] == 0:
                # 그 방향으로 회전하고 왼쪽 방향부터 다시 탐색한다.
                d = d-1
                if d == -1:
                    d = 3

            # 다음 칸이 벽이라면 왼쪽으로 돌아서 탐색한다.
            else:
                d = d-1
                if d == -1:
                    d = 3

        elif d == 1:
            next = direction(d-1, now)

            # 다음 칸이 청소가 되어있지 않고 벽이 아니라면
            if next not in visited and board[next[0]][next[1]] == 0:
                now = next
                stack.append(now)
                visited.append(now)

            # 다음 칸이 청소는 되어있고 벽이 아니라면
            elif next in visited and board[next[0]][next[1]] == 0:
                # 그 방향으로 회전하고 왼쪽 방향부터 다시 탐색한다.
                d = d-1
                if d == -1:
                    d = 3

            # 다음 칸이 벽이라면 왼쪽으로 돌아서 탐색한다.
            else:
                d = d-1
                if d == -1:
                    d = 3

        else:  # d == 0
            next = direction(d-1, now)

            # 다음 칸이 청소가 되어있지 않고 벽이 아니라면
            if next not in visited and board[next[0]][next[1]] == 0:
                now = next
                stack.append(now)
                visited.append(now)

            # 다음 칸이 청소는 되어있고 벽이 아니라면
            elif next in visited and board[next[0]][next[1]] == 0:
                # 그 방향으로 회전하고 왼쪽 방향부터 다시 탐색한다.
                d = d-1
                if d == -1:
                    d = 3

            # 다음 칸이 벽이라면 왼쪽으로 돌아서 탐색한다.
            else:
                d = d-1
                if d == -1:
                    d = 3

    # 네 방향 모두 청소가 되어있거나 벽인 경우 후진하고 다시 왼쪽 방향부터 인접칸 탐색
    if board[rear(d, now)[0]][rear(d,now)[1]] == 1:
        pass

# 네 방향 모두 청소가 되어있거나 벽인 경우 + 뒤쪽 방향이 벽인 경우
result = len(visited)
print(result)









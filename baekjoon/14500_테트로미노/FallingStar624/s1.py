# 오답?
import sys
sys.stdin = open('input.txt', 'r')


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def find_next(current_list):
    next_list = []
    for block in current_list:
        row, col = block
        for d in range(4):
            n_row = row + dr[d]
            n_col = col + dc[d]
            if -1 < n_row < N and -1 < n_col < M:
                if (n_row, n_col) not in current_list:
                    if (n_row, n_col) not in next_list:
                        next_list.append((n_row, n_col))
    return next_list


def calc(final_list):
    result = 0
    for block in final_list:
        row, col = block
        result += board[row][col]
    return result


def dfs(cnt, status):
    global best
    if calc(status) + max_val*(4-cnt) <= best:
        return
    if cnt == 4:
        tmp = calc(status)
        if tmp > best:
            best = tmp
        return

    next_list = find_next(status)
    for block in next_list:
        dfs(cnt+1, status + [block])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    max_val = max(max(*board))
    best = 0
    for row in range(N):
        for col in range(M):
            dfs(1, [(row, col)])

    print(tc, best)



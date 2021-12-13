import sys
sys.stdin = open('input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(c_row, c_col):
    global visited, field
    if field[c_row][c_col] == 0:
        return
    else:
        if visited[c_row][c_col] == 0:
            visited[c_row][c_col] = 1
            for d in range(4):
                n_row = c_row + dr[d]
                n_col = c_col + dc[d]
                if -1 < n_row < N and -1 < n_col < M and visited[n_row][n_col] == 0:
                    dfs(n_row, n_col)
        else:
            return


T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    cabbages = []
    for _ in range(K):
        col, row = map(int, input().split())
        cabbages.append((row, col))

    field = [[0]*M for _ in range(N)]
    for cabbage in cabbages:
        row, col = cabbage
        field[row][col] = 1

    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for cabbage in cabbages:
        start_row, start_col = cabbage
        if visited[start_row][start_col] == 0:
            cnt += 1
            dfs(start_row, start_col)
        else:
            continue

    print(cnt)




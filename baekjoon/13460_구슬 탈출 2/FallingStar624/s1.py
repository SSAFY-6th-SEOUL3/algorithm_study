import sys
sys.stdin = open('input.txt', 'r')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(rr, rc, br, bc, cnt):
    global hall, success
    if hall == (br, bc):
        return
    elif hall == (rr, rc):
        success += 1
        return
    else:
        for d in range(4):
            nrr = rr + dr[d]
            nrc = rc + dr[d]
            nbr = rr + dr[d]
            nbc = rc + dr[d]
            if -1 < nrr < N and -1 < nrc < M and -1 < nbr < N and -1 < nbc < M:
                if board[nrr][nrc] == '#':
                    nrr = rr
                    nrc = rc
                if board[nbr][nbc] == '#':
                    nbr = br
                    nbc = bc

                dfs(nrr, nrc, nbr, nbc, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    success = 0
    hall = (0, 0)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'O':
                hall = (i, j)

    red = (0, 0)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red = (i, j)

    blue = (0, 0)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'B':
                blue = (i, j)

    dfs(red[0], red[1], blue[0], blue[1])
    print(success)

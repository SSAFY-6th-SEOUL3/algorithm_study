import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(board, start):
    visited = [[False] * N for _ in range(M)]
    stack = [start]
    cnt = 0
    while stack and cnt <= 10:
        curr = stack.pop()
        visited[curr[0]][curr[1]] = True

        for i in range(4):
            if curr[0] + dr[i] in range(1, N-1) and curr[1] + dc[i] in range(1, M-1):
                if board[curr[0] + dr[i]][curr[1] + dc[i]] == "O":
                    return True
                if board[curr[0] + dr[i]][curr[1] + dc[i]] == "." and not visited[curr[0] + dr[i]][curr[1] + dc[i]]:
                    stack.append((curr[0] + dr[i], curr[1] + dc[i]))

    return False

for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            start = (r, c)

print(solution(board, start))

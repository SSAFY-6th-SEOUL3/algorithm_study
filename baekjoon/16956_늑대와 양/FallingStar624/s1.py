import sys

sys.stdin = open('input.txt', 'r')
R, C = map(int, input().split())
ranch = [list(input()) for _ in range(R)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
possible = 1


def dfs(row, col):
    global ranch, possible
    if ranch[row][col] == 'S':
        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if ranch[nr][nc] == 'W':
                    possible *= 0
                elif ranch[nr][nc] == '.':
                    ranch[nr][nc] = 'D'
                else:
                    pass


for r in range(R):
    for c in range(C):
        dfs(r, c)

print(possible)
for line in ranch:
    print(''.join(line))

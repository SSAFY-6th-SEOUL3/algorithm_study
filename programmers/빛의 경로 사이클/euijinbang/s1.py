# def solution(grid):
#     answer = []
#     return answer

grid = ["SL", "LR"]

row, col = len(grid), len(grid[0])

# 3차원 배열 생성
visited = [[[0 for k in range(4)] for i in range(col)] for j in range(row)]

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = []
for x in range(row):
    for y in range(col):
        for z in range(4):
            if visited[x][y][z] == 0:
                nx, ny = x, y
                visited[nx][ny][z] = 1
                d = z
                distance = 0

                while True:
                    distance += 1
                    # 범위 조정
                    nx, ny = (nx + dx[d]) % row, (ny + dy[d]) % col

                    if grid[nx][ny] == 'S':
                        pass

                    if grid[nx][ny] == 'L':
                        d = (d-1) % 4

                    if grid[nx][ny] == 'R':
                        d = (d+1) % 4

                    if visited[nx][ny][d] == 1:
                        answer.append(distance)
                        break

                    visited[nx][ny][d] = 1

print(sorted(answer))
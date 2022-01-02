def solution(grid):
    arr = []
    row = len(grid)
    col = len(grid[0])
    for g in grid:
        arr.append(g)
    # [0, 0, 0, 0] => 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    left = [3, 2, 0, 1]
    right = [2, 3, 1, 0]
    visited = [[[0]*4 for _ in range(col)] for _ in range(row)]
    answer = []
    for r in range(row):
        for c in range(col):
            for d in range(4):
                if visited[r][c][d]:
                    continue
                cnt = 0
                y, x, z = r, c, d
                while True:
                    visited[y][x][z] += 1
                    cnt += 1
                    loc = arr[y][x]
                    if loc == 'L':  # 0 -> 3, 1 -> 2, 2 -> 0, 3 -> 1
                        z = left[z]
                    elif loc == 'R':  # 0 -> 2, 1 -> 3, 2 -> 1, 3 -> 0
                        z = right[z]
                    y, x = (y + dr[z]) % row, (x + dc[z]) % col
                    if y == r and x == c and z == d:
                        break
                answer.append(cnt)
    answer.sort()
    return answer


print(solution(["SL", "LR"]))
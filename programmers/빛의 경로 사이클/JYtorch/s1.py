def solution(grid):
    answer = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cycle_list = []
    # visited = []
    # visited를 3차원 배열로 만드는 것과 1차원 배열로 만드는 것은 무슨 차이? 왜 3차원 배열에서 시간이 더 적게 걸리는가?
    visited = [[[0] * len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                r, c = i, j
                cycle = []
                d = k

                # if (r, c, d) in visited: continue
                cnt = 0
                while True:
                    if visited[d][r][c]: break

                    if grid[r][c] == 'S':
                        cycle.append((r, c, d))
                        # visited.append((r, c, d))
                        visited[d][r][c] = 1
                        nr = (r + dr[d]) % len(grid)
                        nc = (c + dc[d]) % len(grid[0])

                    elif grid[r][c] == 'R':
                        cycle.append((r, c, d))
                        # visited.append((r, c, d))
                        visited[d][r][c] = 1
                        d = (d + 1) % 4
                        nr = (r + dr[d]) % len(grid)
                        nc = (c + dc[d]) % len(grid[0])

                    elif grid[r][c] == 'L':
                        cycle.append((r, c, d))
                        # visited.append((r, c, d))
                        visited[d][r][c] = 1
                        d = (d - 1) % 4
                        nr = (r + dr[d]) % len(grid)
                        nc = (c + dc[d]) % len(grid[0])

                    r, c = nr, nc

                    cnt += 1
                    if r == i and c == j and d == k:
                        answer.append(cnt)
                        break

    return sorted(answer)

print(solution(["R","R"]))

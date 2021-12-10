
from sys import stdin


# 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(stdin.readline())

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    board = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0

    # 배추가 있는 위치를 1로 표시한다.
    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        board[Y][X] = 1

    # 배추밭의 각 위치를 탐색한다.
    for r in range(N):
        for c in range(M):
            # 배추를 찾으면, DFS로 해당 배추에서 갈 수 있는 모든 배추를 탐색한다.
            if not visited[r][c] and board[r][c]:
                count += 1
                visited[r][c] = True
                stack = [(r, c)]

                while stack:
                    cnt_r, cnt_c = stack.pop()

                    # 현재 탐색중인 위치와 사방으로 인접한 위치가
                    for i in range(4):
                        nr, nc = cnt_r + dr[i], cnt_c + dc[i]
                        """
                        1) 유효한 좌표이고 / 2) 아직 방문하지 않았고 / 3) 해당 위치에 배추가 있다면
                        방문 처리를 한 뒤, 스택에 넣는다.
                        """
                        if (0 <= nr < N and 0 <= nc < M
                                and not visited[nr][nc]
                                and board[nr][nc]):
                            visited[nr][nc] = True
                            stack.append((nr, nc))

    print(count)

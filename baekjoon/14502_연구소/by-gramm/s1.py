from collections import deque


def count_visit(board, N, M):
    """
    방문 여부를 표시하는 2차원 배열 board에서 방문한 공간의 개수를 구한다.
    """
    count = 0

    for r in range(N):
        for c in range(M):
            if board[r][c]:
                count += 1

    return count


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

least_visit_count = N * M   # 벽을 설치한 뒤, 바이러스가 새로 옮겨지는 공간의 최솟값

virus = []
empty = []

# 빈 공간과 바이러스의 위치를 저장한다.
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            empty.append((r, c))
        elif board[r][c] == 2:
            virus.append((r, c))

# 빈 공간 중 3곳에 벽을 설치하는 모든 경우의 수를 완전탐색한다.
for x in range(len(empty) - 2):
    r1, c1 = empty[x]
    board[r1][c1] = 1

    for y in range(x + 1, len(empty) - 1):
        r2, c2 = empty[y]
        board[r2][c2] = 1

        for z in range(y + 1, len(empty)):
            r3, c3 = empty[z]
            board[r3][c3] = 1

            stack = deque()
            for v in virus:
                stack.append(v)

            visited = [[False] * M for _ in range(N)]

            while stack:
                cnt_r, cnt_c = stack.popleft()

                for i in range(4):
                    r, c = cnt_r + dr[i], cnt_c + dc[i]
                    if 0 <= r < N and 0 <= c < M and not visited[r][c] and board[r][c] == 0:
                        visited[r][c] = True
                        stack.append((r, c))

            least_visit_count = min(least_visit_count, count_visit(visited, N, M))

            board[r3][c3] = 0
        board[r2][c2] = 0
    board[r1][c1] = 0

# 원래 빈 공간 - 벽을 세운 공간(3) - 바이러스가 옮겨지는 최소 공간
print(len(empty) - 3 - least_visit_count)

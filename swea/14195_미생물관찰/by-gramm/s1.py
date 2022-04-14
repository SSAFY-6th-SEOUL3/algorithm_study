from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = []

    for _ in range(N):
        board.append([x for x in input()])

    stack = deque()
    current_type = ''
    a_count, b_count, max_size = 0, 0, 0

    for r in range(N):
        for c in range(M):
            if board[r][c] != '_':            # 새로운 개체를 발견한 경우
                current_type = board[r][c]    # 현재 개체의 타입
                current_size = 1              # 현재 개체의 크기

                if current_type == 'A':
                    a_count += 1
                else:
                    b_count += 1

                stack.append((r, c))
                board[r][c] = '_'             # 방문한 구역은 '_'로 표시함

                while stack:
                    cnt_r, cnt_c = stack.pop()

                    for i in range(4):
                        nr, nc = cnt_r + dr[i], cnt_c + dc[i]

                        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == current_type:
                            stack.append((nr, nc))
                            board[nr][nc] = '_'
                            current_size += 1

                max_size = max(max_size, current_size)

    print(f"#{tc} {a_count} {b_count} {max_size}")

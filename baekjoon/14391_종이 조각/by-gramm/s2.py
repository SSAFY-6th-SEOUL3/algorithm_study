"""
규칙 : 점수가 최댓값이 되려면, 합칠 수 있는 종이 조각이 더 이상 없어야 한다.
증명 : 두 숫자 A와 B를 합칠 때, (AB) = 10A + B이므로, 이는 반드시 A + B보다 크거나 같다.

실패!
"""


def get_max_sum(current_value):
    global N, M, board, visited, max_value

    for r in range(N):
        for c in range(M):
            # 방문하지 않은 칸을 찾은 경우,
            # 가로로 끝까지 채우는 경우와 세로로 끝까지 채우는 경우를 각각 탐색한다.
            if not visited[r][c]:
                # 1) 가로로 끝까지 채우는 경우
                str_num = ""

                for nc in range(c, M):
                    visited[r][nc] = True
                    str_num += board[r][nc]

                get_max_sum(current_value + int(str_num))

                for nc in range(c, M):
                    visited[r][nc] = False

                # 2) 세로로 끝까지 채우는 경우
                str_num = ""

                for nr in range(r, N):
                    visited[nr][c] = True
                    str_num += board[nr][c]

                get_max_sum(current_value + int(str_num))

                for nr in range(r, N):
                    visited[nr][c] = False

                return

    # 모든 칸을 다 방문했다면 => max_value를 업데이트한다.
    max_value = max(max_value, current_value)


N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append([x for x in list(input())])

visited = [[False] * M for _ in range(N)]
max_value = 0

get_max_sum(0)
print(max_value)

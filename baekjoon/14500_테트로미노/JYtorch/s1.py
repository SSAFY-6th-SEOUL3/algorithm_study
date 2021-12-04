import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# r, c: 현재 행, 현재 열
# level: 깊이
# cursum: 현재까지의 합
# directions: 현재까지 이동한 방향을 담는 리스트(ㅗ, ㅓ, ㅏ, ㅜ 모양을 만들 때 사용)
def solution(r, c, level, cursum, directions):
    global ans

    # 정사각형을 계속 만들어봤자 ans보다 클 가망이 없으면 종료(가지치기)
    if ans >= cursum + max_v * (3 - level):
        return

    # level이 3이 되면 정사각형 4개가 다 완성되었으므로 종료
    if level == 3:
        if ans < cursum:
            ans = cursum
        return

    else:
        # ㅡ 모양에서 가운데에 정사각형 하나를 더 붙여서 ㅗ, ㅜ 모양을 만드는 코드
        if len(directions) == 2 and directions[0] == directions[1] and (directions[0] == 0 or directions[0] == 2):
            for nd in [(1, 0), (-1, 0)]:
                nr = r - dr[directions[0]] + nd[0]
                nc = c - dc[directions[0]] + nd[1]

                if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
                solution(nr, nc, level + 1, cursum + arr[nr][nc], directions)

        # ㅣ 모양에서 가운데에 정사각형 하나를 더 붙여서 ㅓ, ㅏ 모양을 만드는 코드
        elif len(directions) == 2 and directions[0] == directions[1] and (directions[0] == 1 or directions[0] == 3):
            for nd in [(0, 1), (0, -1)]:
                nr = r - dr[directions[0]] + nd[0]
                nc = c - dc[directions[0]] + nd[1]

                if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
                solution(nr, nc, level + 1, cursum + arr[nr][nc], directions)

        # 현재 위치 r, c에서 정사각형을 하나씩 이어붙이는 코드
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]: continue
            visited[nr][nc] = 1

            solution(nr, nc, level + 1, cursum + arr[nr][nc], directions + [d])

            visited[nr][nc] = 0

# N: 세로 크기, M: 가로 크기, arr: 2차원 배열
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# max_v: arr에 써진 숫자 중 최대값(가지치기할 때 사용)
max_v = max(map(max, arr))
ans = 0

visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        solution(i, j, 0, arr[i][j], [])    # 2차원 배열 arr을 모두 돌면서 각각을 시작점으로 두고 dfs 함수 실행
        visited[i][j] = 0

print(ans)
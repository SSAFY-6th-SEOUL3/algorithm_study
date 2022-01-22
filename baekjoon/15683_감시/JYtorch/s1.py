import sys
sys.stdin = open('input.txt')

def solution(n, cnt):
    global ans

    # 모든 CCTV(n개) 전부 다 돌면 사각지대 개수 계산
    if n == len(C_pos):
        if area - cnt < ans:
            ans = area - cnt
        return

    # n번째 CCTV 정보
    r, c, num = C_pos[n]

    # 1번 감시카메라
    if num == 1:
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            visited = set()
            nr, nc = r + d[0], c + d[1]
            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[0]
                    nc += d[1]
                    continue
                arr[nr][nc] = '#'   # 감시한 곳은 #으로 바꿔주기
                cnt += 1
                visited.add((nr, nc))
                nr += d[0]
                nc += d[1]

            solution(n + 1, cnt)

            # 재귀에서 빠져나왔으면 0으로 되돌려주기
            for pos in visited:
                arr[pos[0]][pos[1]] = 0
                cnt -= 1

    # 2번 감시카메라
    elif num == 2:
        for d in [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]]:
            visited = set()
            nr = r + d[0][0]
            nc = c + d[0][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[0][0]
                    nc += d[0][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[0][0]
                nc += d[0][1]

            nr = r + d[1][0]
            nc = c + d[1][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[1][0]
                    nc += d[1][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[1][0]
                nc += d[1][1]

            solution(n + 1, cnt)

            for pos in visited:
                arr[pos[0]][pos[1]] = 0
                cnt -= 1

    # 3번 감시카메라
    elif num == 3:
        for d in [[[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]]]:
            visited = set()
            nr = r + d[0][0]
            nc = c + d[0][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[0][0]
                    nc += d[0][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[0][0]
                nc += d[0][1]

            nr = r + d[1][0]
            nc = c + d[1][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[1][0]
                    nc += d[1][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[1][0]
                nc += d[1][1]

            solution(n + 1, cnt)

            for pos in visited:
                arr[pos[0]][pos[1]] = 0
                cnt -= 1

    # 4번 감시카메라
    elif num == 4:
        for d in [[[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]], [[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]]]:
            visited = set()
            nr = r + d[0][0]
            nc = c + d[0][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[0][0]
                    nc += d[0][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[0][0]
                nc += d[0][1]

            nr = r + d[1][0]
            nc = c + d[1][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[1][0]
                    nc += d[1][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[1][0]
                nc += d[1][1]

            nr = r + d[2][0]
            nc = c + d[2][1]

            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[2][0]
                    nc += d[2][1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[2][0]
                nc += d[2][1]

            solution(n + 1, cnt)

            for pos in visited:
                arr[pos[0]][pos[1]] = 0
                cnt -= 1

    # 5번 감시카메라
    elif num == 5:
        visited = set()
        for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = r + d[0], c + d[1]
            while 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 6: break
                if arr[nr][nc] in set((1, 2, 3, 4, 5, '#')):
                    nr += d[0]
                    nc += d[1]
                    continue
                arr[nr][nc] = '#'
                cnt += 1
                visited.add((nr, nc))
                nr += d[0]
                nc += d[1]

        solution(n + 1, cnt)

        for pos in visited:
            arr[pos[0]][pos[1]] = 0
            cnt -= 1


N, M = map(int, input().split())
arr = []
ans = 987654321
area = 0       # 모든 사각지대 개수 (이차원 배열에서 0의 개수)

C_pos = []     # 모든 CCTV 좌표
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] and tmp[j] != 6:
            C_pos.append((i, j, tmp[j]))
    area += tmp.count(0)
    arr.append(tmp)

used = [0] * len(C_pos)
solution(0, 0)
print(ans)
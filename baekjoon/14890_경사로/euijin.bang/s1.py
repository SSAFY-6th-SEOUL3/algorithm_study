import sys
# sys.stdin = open('input.txt')

N, L = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r_arr = list(map(list, zip(*arr)))

def count(arr):
    cnt = 0
    for i in range(N):
        route = True
        visited = [False] * N
        for j in range(N-1):
            p = arr[i][j]
            n = arr[i][j+1]

            # 경사가 2 이상인 경우
            if abs(p - n) > 1:
                route = False
                break

            # 평지인 경우
            if p == n:
                continue

            # 내리막길
            if p - n > 0:
                if arr[i][j+1:j+1+L].count(arr[i][j+1]) >= L and True not in visited[j+1:j+1+L]:
                    for k in range(j+1, j+1+L):
                        visited[k] = True
                        continue
                else:
                    route = False
                    break
            # 오르막길
            else:
                if arr[i][j-L+1:j+1].count(arr[i][j]) >= L and True not in visited[j-L+1:j+1]:
                    for k in range(j-L+1, j+1):
                        visited[k] = True
                        continue
                else:
                    route = False
                    break
        if route:
            cnt += 1

    return cnt

ans = count(arr) + count(r_arr)
print(ans)

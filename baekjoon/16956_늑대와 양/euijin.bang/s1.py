# [해결] error

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]


def solution():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "W":
                for k in range(4):
                    if (0 <= i + dx[k] < r) and (0 <= j + dy[k] < c):
                        if arr[i+dx[k]][j+dy[k]] == "S":
                            return 0
                for k in range(4):
                    if (0 <= i + dx[k] < r) and (0 <= j + dy[k] < c):
                        # . 일때만 D로 바꾼다. (늑대일 수 있으므로)
                        if arr[i+dx[k]][j+dy[k]] == ".":
                            arr[i + dx[k]][j + dy[k]] = "D"


answer = solution()
if answer == 0:
    print(0)
else:
    print(1)
    for row in arr:
        print("".join(row))

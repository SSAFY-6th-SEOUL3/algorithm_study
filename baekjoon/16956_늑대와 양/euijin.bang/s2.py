import sys
sys.stdin = open("input.txt")

# anti_clockwise
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

ch = False

for i in range(r):
    for j in range(c):
        if arr[i][j] == "W":
            for k in range(4):
                if (0 <= i + dx[k] < r) and (0 <= j + dy[k] < c):
                    if arr[i+dx[k]][j+dy[k]] == "S":
                        ch = True

if ch:
    print(0)
else:
    for i in range(r):
        for j in range(c):
            if arr[i][j] not in "SW":
                arr[i][j] = "D"
    print(1)
    for row in arr:
        print("".join(row))


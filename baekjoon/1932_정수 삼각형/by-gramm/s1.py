from sys import stdin

n = int(stdin.readline())
triangle = []

for _ in range(n):
    triangle.append([int(x) for x in stdin.readline().split()])

for r in range(1, n):
    #
    triangle[r][0] += triangle[r - 1][0]
    triangle[r][r] += triangle[r - 1][r - 1]

    for c in range(1, r):
        triangle[r][c] += max(triangle[r - 1][c - 1], triangle[r - 1][c])

print(max(triangle[n - 1]))

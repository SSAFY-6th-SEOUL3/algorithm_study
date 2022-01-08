import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N):
    for j in range(i+1):
        left, right = j-1, j
        if left < 0:
            triangle[i][j] += triangle[i-1][right]
        elif right > i-1:
            triangle[i][j] += triangle[i-1][left]
        else:
            triangle[i][j] += max(triangle[i-1][left], triangle[i-1][right])

print(max(triangle[-1]))

import sys
sys.stdin = open('input.txt')


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i - 1][0]
        elif j == len(arr[i]) - 1:
            arr[i][j] += arr[i - 1][len(arr[i - 1]) - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[len(arr) - 1]))
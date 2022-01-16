import sys
sys.stdin = open("input.txt")

n = int(input())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# DP[i][j] : arr(i,j)에 도착했을 때 최댓값


def solution(n):
    for i in range(1, n+1):
        tmp = list(map(int, input().split(' ')))
        for j in range(1, i+1):
            arr[i][j] = tmp[j-1]

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

    return max(dp[-1])


print(solution(n))

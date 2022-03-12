import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

"""
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15  
5           1 2 3 4 5  2  3  4  5  6  3    
12                           1  2  3  4

"""
MAX_VALUE = 987654321
dp = [MAX_VALUE] * (k + 1)
dp[0] = 0
for i in range(n):
    for j in range(coins[i], k + 1):
        dp[j] = min(dp[j - coins[i]] + 1, dp[j])

if dp[k] == MAX_VALUE:
    print(-1)
else:
    print(dp[k])

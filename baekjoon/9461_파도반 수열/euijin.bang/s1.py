"""
DP
"""

N = int(input())
# 1 <= N <= 100


def dp(n):
    cache = [0] * 101
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    cache[4] = 2
    cache[5] = 2

    for i in range(6, 101):
        cache[i] = cache[i - 1] + cache[i - 5]

    return cache[n]


for i in range(N):
    n = int(input())
    print(dp(n))

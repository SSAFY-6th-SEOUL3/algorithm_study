"""
replace : 11726_타일링 (DP)
"""

n = int(input())


def dp(n):
    cache = [0] * 1001
    cache[1] = 1
    cache[2] = 2

    for i in range(3, 1001):
        cache[i] = cache[i - 2] + cache[i - 1]
    return cache[n] % 10007


print(dp(n))
"""
DP
replace : 1463_1로 만들기
"""

N = int(input())


def dp(N):
    memo = [0] * (N + 1)

    for i in range(2, N + 1):

        memo[i] = memo[i - 1] + 1

        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3] + 1)

        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2] + 1)

    return memo[N]


print(dp(N))

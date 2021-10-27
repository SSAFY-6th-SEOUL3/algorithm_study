import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
stuffs = []
print(N, K)
for _ in range(N):
    w, v = (map(int, input().split()))
    stuffs.append((w, v))
dp = [[0]*(K+1) for _ in range(N)]
for i in range(0, N):
    tmp_w, tmp_v = stuffs[i][0], stuffs[i][1]
    for j in range(0, K+1):
        if j < tmp_w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-tmp_w]+tmp_v, dp[i-1][j])

print(dp[-1][-1])
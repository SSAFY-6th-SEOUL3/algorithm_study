# 시간 초과
# DP로 접근필요
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
stuffs = []
for _ in range(N):
    w, v = (map(int, input().split()))
    stuffs.append((w, v))

maximum = 0
for i in range(1 << N):
    weight = 0
    value = 0
    for j in range(N):
        if i & 1 << j:
            weight += stuffs[j][0]
            value += stuffs[j][1]
        if weight > K:
            break
    else:
        if maximum < value:
            maximum = value

print(maximum)
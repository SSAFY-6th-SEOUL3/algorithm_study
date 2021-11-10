from sys import stdin
from collections import Counter


N, M = map(int, stdin.readline().split())
"""
prefix_sums[i]: (맨 앞의 수부터 i번째 수까지의 합)을 M으로 나눈 나머지
a번째 수부터 b번째 수까지의 합 = prefix_sums[b] - prefix_sums[a - 1]
첫 수부터 시작하는 경우를 처리하기 위해, prefix_sums 앞에 0을 추가함.
"""
prefix_sums = [0] + [int(x) for x in stdin.readline().split()]

for i in range(1, N + 1):
    prefix_sums[i] = (prefix_sums[i] + prefix_sums[i - 1]) % M

"""
counters: prefix_sums에서 각 수의 개수를 모은 배열
          (ex. 3이 2개, 5가 4개 있으면 [2, 4])
"""
counters = list(Counter(prefix_sums).values())
total = 0

"""
각 count에 대하여 count개 중 2개를 고르는 경우의 수를 total에 더한다.
(n개 중 2개를 고르는 경우의 수 = n(n - 1) / 2)
"""
for count in counters:
    total += ((count) * (count - 1)) // 2

print(total)

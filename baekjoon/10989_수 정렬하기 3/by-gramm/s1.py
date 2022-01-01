"""
수는 최대 10,000,000개이지만 모든 수가 1 ~ 10,000 중 하나이므로, 계수 정렬을 이용한다.
"""

from sys import stdin


N = int(stdin.readline())
num_counts = [0] * 10001

for _ in range(N):
    num_counts[int(stdin.readline())] += 1

for num in range(1, 10001):
    for _ in range(num_counts[num]):
        print(num)

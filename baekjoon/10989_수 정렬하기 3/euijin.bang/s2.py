# 시간 초과 문제 => sys.stdin.readline() 로 변경
# 메모리 초과 문제 => for 문 생략

import sys

n = int(sys.stdin.readline())

# 수의 범위 1 ~ 10000
counts = [0] * 100001

for i in range(n):
    counts[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(counts[i]):
        print(i)
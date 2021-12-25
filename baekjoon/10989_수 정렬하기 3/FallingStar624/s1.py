# 메모리 초과
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = [0]*10000001
for i in range(N):
    numbers[int(input())] += 1
idx = 1
while N > 0:
    if numbers[idx] > 0:
        for _ in range(numbers[idx]):
            print(idx)
            N -= 1
        idx += 1
    else:
        idx += 1


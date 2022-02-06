import sys
sys.stdin = open('input.txt')

K = int(input())
numbers = [0] * 100000
idx = 0
for _ in range(K):
    n = int(input())
    if n == 0:
        idx -= 1
        numbers[idx] = 0
    else:
        numbers[idx] = n
        idx += 1

print(sum(numbers))

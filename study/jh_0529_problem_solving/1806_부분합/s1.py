from sys import stdin


N, S = map(int, stdin.readline().split())
numbers = [int(x) for x in stdin.readline().split()]

start, end = 0, 0
min_length = N + 1
total = 0

while end < N and total + numbers[end] < S:
    total += numbers[end]
    end += 1

while end < N:
    total += numbers[end]
    end += 1

    while total - numbers[start] >= S:
        total -= numbers[start]
        start += 1

    min_length = min(min_length, end - start)

if min_length == (N + 1):
    print(0)
else:
    print(min_length)

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

for i in range(N-1, 0, -1):
    for j in range(0, i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for num in numbers:
    print(num)


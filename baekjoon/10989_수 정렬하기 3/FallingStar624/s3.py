# sys.stdin.readline...빠르다...
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
numbers = [0]*10001
for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numbers[i]:
        for _ in range(numbers[i]):
            print(i)
import sys
sys.stdin = open('input.txt')

N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in A:
        print(1)
    else:
        print(0)

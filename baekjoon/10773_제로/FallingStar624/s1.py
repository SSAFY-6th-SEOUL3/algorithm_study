import sys
sys.stdin = open('input.txt')

K = int(input())
money = []

for _ in range(K):
    tmp = int(input())
    if tmp:
        money.append(tmp)
    else:
        money.pop()

print(sum(money))

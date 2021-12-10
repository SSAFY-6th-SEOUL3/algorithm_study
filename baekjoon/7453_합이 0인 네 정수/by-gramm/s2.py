
from sys import stdin


N = int(stdin.readline())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A.sort()
B.sort()
C.sort()
D.sort()

# 풀이중

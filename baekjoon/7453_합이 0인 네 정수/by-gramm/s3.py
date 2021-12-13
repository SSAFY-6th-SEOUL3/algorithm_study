# s1과 s2를 잘 섞고 효율성을 최대한 높인 결과
# pypy3에서만 10.9초로 통과함. (python3으로는 통과한 사람 자체가 없음)

from sys import stdin
from collections import Counter


N = int(stdin.readline())
A, B, C, D = [], [], [], []
a_plus_b = []   # a와 b의 합의 음수값의 개수를 저장하는 딕셔너리
c_plus_d = []   # c와 d의 합의 개수를 저장하는 딕셔너리

for _ in range(N):
    a, b, c, d = map(int, stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A:
    for b in B:
        a_plus_b.append(a + b)

for c in C:
    for d in D:
        c_plus_d.append(c + d)

total = 0
ab_counter = Counter(a_plus_b)

for x in c_plus_d:
    total += ab_counter[-x]

print(total)

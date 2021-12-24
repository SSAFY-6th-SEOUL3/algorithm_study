# 시간 초과 (s1과 거의 똑같은 풀이)

from sys import stdin


N = int(stdin.readline())
A, B, C, D = [], [], [], []
a_plus_b = dict()   # a와 b의 합의 음수값의 개수를 저장하는 딕셔너리
c_plus_d = dict()   # c와 d의 합의 개수를 저장하는 딕셔너리

for _ in range(N):
    a, b, c, d = map(int, stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(N):
    for j in range(N):
        # A와 B의 두 요소의 합의 음수값의 개수를 업데이트한다.
        a_plus_b[A[i] + B[j]] = a_plus_b.get(A[i] + B[j], 0) + 1
        # C와 D의 두 요소의 합의 개수를 업데이트한다.
        c_plus_d[C[i] + D[j]] = c_plus_d.get(C[i] + D[j], 0) + 1

total = 0

for key, value in a_plus_b.items():
    total += value * c_plus_d.get(-key, 0)

print(total)

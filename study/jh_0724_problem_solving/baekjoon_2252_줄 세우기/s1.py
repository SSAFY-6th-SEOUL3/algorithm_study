from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().split())

adj_list = [set() for _ in range(N + 1)]
in_degrees = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, stdin.readline().split())

    adj_list[A].add(B)
    in_degrees[B] += 1

queue = deque()
orders = []

# 시작 지점을 선택한다.
for i in range(1, N + 1):
    if not in_degrees[i]:
        queue.append(i)

# 위상 정렬 알고리즘을 통해 학생들을 줄 세운 결과를 저장한다.
for _ in range(N):
    current = queue.popleft()
    orders.append(current)

    for node in adj_list[current]:
        in_degrees[node] -= 1

        if not in_degrees[node]:
            queue.append(node)

for node in orders:
    print(node, end=" ")

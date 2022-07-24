from sys import stdin
from heapq import heappush, heappop


N, M = map(int, stdin.readline().split())

adj_list = [set() for _ in range(N + 1)]
in_degrees = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    adj_list[A].add(B)
    in_degrees[B] += 1

heap = []
result = []

for num in range(1, N + 1):
    if not in_degrees[num]:
        heappush(heap, num)

while heap:
    current = heappop(heap)
    result.append(current)

    for num in adj_list[current]:
        in_degrees[num] -= 1

        if not in_degrees[num]:
            heappush(heap, num)

for num in result:
    print(num, end=" ")

from sys import stdin
from heapq import heappush, heappop


T = int(stdin.readline())

for _ in range(T):
    N, K = map(int, stdin.readline().split())
    construct_times = [0] + [int(x) for x in stdin.readline().split()]
    children = [set() for _ in range(N + 1)]
    parents = [set() for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, stdin.readline().split())
        children[X].add(Y)
        parents[Y].add(X)

    W = int(stdin.readline())
    heap = []

    # 선행 건물이 없는 건물들을 힙에 저장한다.
    for i in range(1, N + 1):
        if not parents[i]:
            heappush(heap, (construct_times[i], i))

    while heap:
        time, index = heappop(heap)

        if index == W:
            print(time)
            break

        for node in children[index]:
            parents[node].remove(index)

            if not parents[node]:
                heappush(heap, (time + construct_times[node], node))

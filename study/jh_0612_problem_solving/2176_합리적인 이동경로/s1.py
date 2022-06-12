# 시간 초과

from sys import stdin
from heapq import heappush, heappop


START, END = 1, 2
N, M = map(int, stdin.readline().split())
distances = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    distances[A].append((B, C))
    distances[B].append((A, C))

# 각 정점의 2번 정점까지의 거리를 구한다.
distance_from_two = [12345679] * (N + 1)
distance_from_two[END] = 0
heap = [(0, END)]

while heap:
    cnt_distance, cnt_node = heappop(heap)

    for node, distance in distances[cnt_node]:
        new_distance = cnt_distance + distance

        if new_distance <= distance_from_two[node]:
            distance_from_two[node] = new_distance
            heappush(heap, (new_distance, node))

# 1번 정점에서 2번 정점으로 이동하는 합리적인 이동경로의 개수를 구한다.
counts = [0] * (N + 1)
counts[START] = 1
visited = [False] * (N + 1)
visited[START] = True

heap = [(distance_from_two[START], START)]

while heap:
    cnt_distance, cnt_node = heappop(heap)

    for node, distance in distances[cnt_node]:
        if node == END:
            counts[END] += counts[cnt_node]
            continue

        if distance_from_two[node] <= cnt_distance:
            counts[node] += counts[cnt_node]

            if not visited[node]:
                visited[node] = True
                heappush(heap, (distance_from_two[node], node))

print(counts[END])

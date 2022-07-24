from sys import stdin
from heapq import heappush, heappop


N = int(stdin.readline())

adj_list = [set() for _ in range(N + 1)]
build_times = [[] for _ in range(N + 1)]
min_times = [0 for _ in range(N + 1)]
in_degrees = [0] * (N + 1)

for i in range(1, N + 1):
    time, *pre_buildings = map(int, stdin.readline().split())
    build_times[i] = time

    pre_buildings.pop()  # -1 제거
    in_degrees[i] = len(pre_buildings)

    for num in pre_buildings:
        adj_list[num].add(i)

# 진입 차수가 0인 건물들을 (종료시간, 건물 번호)의 형태로 heap에 저장한다.
heap = []

for num in range(1, N + 1):
    if not in_degrees[num]:
        min_times[num] = build_times[num]
        heappush(heap, [build_times[num], num])

# 위상 정렬 알고리즘을 통해 각 건물이 완성되는 최소 시간을 구한다.
while heap:
    time, cnt_building = heappop(heap)

    for num in adj_list[cnt_building]:
        in_degrees[num] -= 1

        if not in_degrees[num]:
            min_times[num] = time + build_times[num]
            heappush(heap, [min_times[num], num])

for i in range(1, N + 1):
    print(min_times[i])

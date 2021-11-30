# 성공
import heapq


def solution(jobs):
    total, time, i = 0, 0, 0
    n = len(jobs)
    start = -1
    heap = []

    while i < n:
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            tmp = heapq.heappop(heap)
            start = time
            time += tmp[0]
            total += time - tmp[1]
            i += 1
        else:
            time += 1
    return total // n


print(solution([[0, 3], [1, 9], [2, 6]]))

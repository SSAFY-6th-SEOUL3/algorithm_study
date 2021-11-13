import heapq
from collections import deque


def solution(jobs):
    N = len(jobs)
    jobs = sorted(deque(jobs), key=lambda x: (x[0], x[1]))
    heap = [jobs[0]]
    jobs = jobs[1:]
    total = 0
    current_time = 0
    while jobs:
        # 현재시간까지 들어온 요청을 heappush
        for job in jobs:
            if job[0] <= current_time:
                heapq.heappush(heap, job)
                jobs.remove(job)
            else:
                break
        print(heap)
        current_work = heapq.heappop(heap)
        current_time += current_work[1]
        total += current_time - current_work[0]


    answer = total // N
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))
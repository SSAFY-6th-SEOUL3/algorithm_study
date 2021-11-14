import heapq


# (요청시간, 작업시간) -> (작업시간, 요청시간)
def solution(jobs):
    n = len(jobs)
    heap = []
    for job in jobs:
        heap.append((job[1], job[0]))
    heapq.heapify(heap)
    total = 0
    time = 0
    while heap:
        # 현재 시작 가능한 요청 중 작업시간이 가장 작은 요청으로 선택
        next_request = heapq.heappop(heap)
        min_time = next_request[0]
        # heap 비었을 경우
        if not heap:
            time += next_request[0]
            total += time - next_request[1]
            return total // n

        if time >= next_request[1]:
            for _ in range(n):
                tmp = heapq.heappop(heap)
                # 현재 시간보다 요청 시간이 빠르고 / 현재 최단 작업시간보다 작업시간이 작으면
                if tmp[1] <= time and min_time > tmp[0]:
                    heapq.heappush(heap, next_request)
                    next_request = tmp
                    min_time = next_request[0]
                else:
                    heapq.heappush(heap, tmp)
            time += next_request[0]
            total += time - next_request[1]
        else:
            heapq.heappush(heap, next_request)
            time += 1

    answer = total//n
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))
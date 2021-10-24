# 시간초과
import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(scoville)

    while heap and min(heap) <= K:
        least = heapq.heappop(heap)
        sec_least = heapq.heappop(heap)
        heapq.heappush(heap, least+sec_least*2)
        answer += 1
        if len(heap) == 1 and max(heap) < K:
            return -1
    return answer



print(solution([1, 2, 3, 9, 10, 12], 7))


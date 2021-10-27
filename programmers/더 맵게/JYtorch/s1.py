scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) > 1:
            f1 = heapq.heappop(scoville)
            f2 = heapq.heappop(scoville)
            heapq.heappush(scoville, f1 + f2 * 2)
            answer += 1
        else:
            return -1

    return answer

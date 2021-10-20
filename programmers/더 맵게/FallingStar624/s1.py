import heapq

arr = [1, 2, 3, 9, 10, 12]
k = 7


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] > K:
            return cnt
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first + 2*second
            heapq.heappush(scoville, new)
            cnt += 1
    else:
        if scoville[0] > K:
            return cnt
        else:
            return -1

print(solution(arr, k))




from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    # 방법 1 heapq.heapify(x)
    # 리스트 x를 선형 시간으로 제자리에서 힙으로 변환합니다.
    heapify(scoville)

    # 방법2
    h = []
    for food in scoville:
        heappush(h, food)

    # scoville의 길이는 2 이상이다.
    while len(scoville) >= 2:
            f1 = heappop(scoville)
            f2 = heappop(scoville)
            heappush(scoville, f1 + f2 * 2)
            answer += 1

            # 스코빌 최소값이 K 이상이면
            if scoville[0] >= K:
                return answer

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
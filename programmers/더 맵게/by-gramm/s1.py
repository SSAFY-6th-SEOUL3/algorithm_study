from heapq import heappush, heappop


def solution(scoville, K):
    """
    모든 음식의 스코빌 지수가 K 이상이 되기 위해 음식을 섞는 최소 횟수를 구한다.
    Args:
        scoville: 각 음식의 스코빌 지수 (배열)
    """
    heap = []
    count = 0  # 음식을 섞는 횟수

    # 각 음식의 스코빌 지수를 힙에 저장한다. (덜 매운 것부터 순서대로 저장된다.)
    for food in scoville:
        heappush(heap, food)

    # 음식이 2개 미만이 될 때까지 반복한다.
    while len(heap) >= 2:
        # 가장 안 매운 음식의 스코빌 지수가 K 이상이라면
        # 즉, 모든 음식의 스코빌 지수가 K 이상이라면 => count 리턴
        if heap[0] >= K:
            return count

        least_spicy = heappop(heap)
        second_least_spicy = heappop(heap)
        heappush(heap, least_spicy + second_least_spicy * 2)
        count += 1

    # 더 이상 섞을 음식이 없는데 스코빌 지수가 K 미만인 음식이 있다면 => -1 리턴
    if heap[0] < K:
        return -1

    return count

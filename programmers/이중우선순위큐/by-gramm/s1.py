# 프로그래머스에서는 통과함, but 백준에 있는 같은 문제에서는 시간 초과가 뜸.
# 시간 초과 이유 : remove 연산의 시간 복잡도가 O(N)

from heapq import heappush, heappop


def solution(operations):
    min_heap = []
    max_heap = []
    count = 0       # 힙에 남아있는 수의 개수

    for operation in operations:
        # 1. 최댓값 삭제
        if operation == "D 1":
            if count:
                max_value = heappop(max_heap)  # 최대 힙에서 최댓값을 꺼낸다.
                min_heap.remove(-max_value)    # 최소 힙에서 최댓값의 음수를 없앤다.
                count -= 1
        # 2. 최소값 삭제
        elif operation == "D -1":
            if count:
                min_value = heappop(min_heap)  # 최소 힙에서 최솟값을 꺼낸다.
                max_heap.remove(-min_value)    # 최대 힙에서 최솟값의 음수를 없앤다.
                count -= 1
        # 3. 숫자 삽입
        else:
            num = int(operation[2:])
            heappush(min_heap, num)            # 최소 힙에 num을 삽입한다.
            heappush(max_heap, -num)           # 최대 힙에 -num을 삽입한다. (최대 힙이 되도록)
            count += 1

    if not count:
        return [0, 0]
    else:
        max_value, min_value = -heappop(max_heap), heappop(min_heap)
        return [max_value, min_value]

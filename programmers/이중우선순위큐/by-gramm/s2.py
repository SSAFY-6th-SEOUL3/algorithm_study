# 백준 시간 초과를 해결한 풀이

from heapq import heappush, heappop


def solution(operations):
    min_heap = []
    max_heap = []
    min_counter = dict()   # min_heap에 들어있는 수의 개수를 저장하는 딕셔너리
    max_counter = dict()   # max_heap에 들어있는 수의 개수를 저장하는 딕셔너리
    count = 0

    for operation in operations:
        # 1. 최댓값 삭제
        if operation == "D 1":
            if count:
                count -= 1
                while True:
                    max_value = -heappop(max_heap)
                    max_counter[max_value] -= 1     # max_counter에 최댓값의 개수를 업데이트한다.
                    """
                    1) max_counter[max_value] >= min_counter[max_value]
                       => 지금 꺼낸 max_value는 min_heap에서 이미 꺼냈다
                       => 다음 최댓값을 꺼낸다
                    2) max_counter[max_value] < min_counter[max_value]
                       => 지금 꺼낸 max_value는 min_heap에서 꺼내지 않은 값이다
                    """
                    if max_counter[max_value] < min_counter[max_value]:
                        break
        # 2. 최소값 삭제
        elif operation == "D -1":
            if count:
                count -= 1
                while True:
                    min_value = heappop(min_heap)
                    min_counter[min_value] -= 1     # min_counter에 최솟값의 개수를 업데이트한다.
                    if min_counter[min_value] < max_counter[min_value]:
                        break
        # 3. 숫자 삽입
        else:
            num = int(operation[2:])
            heappush(min_heap, num)
            heappush(max_heap, -num)
            min_counter[num] = min_counter.get(num, 0) + 1   # num의 개수를 min_counter에 업데이트한다.
            max_counter[num] = max_counter.get(num, 0) + 1   # num의 개수를 max_counter에 업데이트한다.
            count += 1

    if not count:
        return [0, 0]
    else:
        # min_heap에서 꺼내지 않은 최댓값을 찾는다.
        while True:
            max_value = -heappop(max_heap)
            max_counter[max_value] -= 1
            if max_counter[max_value] < min_counter[max_value]:
                max_counter[max_value] += 1  # min_value를 찾기 위해 max_counter를 기존 상태로 돌려놓는다.
                break
        # max_heap에서 꺼내지 않은 최솟값을 찾는다.
        while True:
            min_value = heappop(min_heap)
            min_counter[min_value] -= 1
            if min_counter[min_value] < max_counter[min_value]:
                break

        return [max_value, min_value]

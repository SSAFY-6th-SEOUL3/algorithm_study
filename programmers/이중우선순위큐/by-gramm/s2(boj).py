# s2.py의 백준용 풀이 (BOJ 7662)

from sys import stdin
from heapq import heappush, heappop


T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    min_heap = []
    max_heap = []
    min_counter = dict()
    max_counter = dict()
    count = 0

    for _ in range(k):
        operation = stdin.readline().rstrip()

        # 1. 최댓값 삭제
        if operation == "D 1":
            if count:
                count -= 1
                while True:
                    max_value = -heappop(max_heap)
                    max_counter[max_value] -= 1
                    if max_counter[max_value] < min_counter[max_value]:
                        break
        # 2. 최소값 삭제
        elif operation == "D -1":
            if count:
                count -= 1
                while True:
                    min_value = heappop(min_heap)
                    min_counter[min_value] -= 1
                    if min_counter[min_value] < max_counter[min_value]:
                        break
        # 3. 숫자 삽입
        else:
            num = int(operation[2:])
            heappush(min_heap, num)
            heappush(max_heap, -num)
            min_counter[num] = min_counter.get(num, 0) + 1
            max_counter[num] = max_counter.get(num, 0) + 1
            count += 1

    if not count:
        print("EMPTY")
    else:
        while True:
            max_value = -heappop(max_heap)
            max_counter[max_value] -= 1
            if max_counter[max_value] < min_counter[max_value]:
                max_counter[max_value] += 1
                break
        while True:
            min_value = heappop(min_heap)
            min_counter[min_value] -= 1
            if min_counter[min_value] < max_counter[min_value]:
                break

        print(max_value, min_value)

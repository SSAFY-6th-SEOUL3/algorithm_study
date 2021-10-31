import sys
sys.stdin = open('input.txt')

import heapq

N = int(input())

heap = []
for _ in range(N):
    nums = list(map(int, input().split()))
    # 만약 heap 이 비어있다면 item을 heap으로 푸시한다.
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    # heap 이 비어있지 않다면
    else:
        for num in nums:
            # 만약 가장 작은 항목보다 큰 수가 나오면 해당 수를 푸시하고, 새로운 힙에서 가장 작은 수를 pop 한다.
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

# 반복을 마치면 가장 큰 수 다섯개가 힙에 담겨 있으므로, 그 중 가장 작은 수를 반환한다.
print(heap[0])
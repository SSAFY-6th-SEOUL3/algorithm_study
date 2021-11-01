import heapq

N = int(input())
heap = []
for num in map(int, input().split()):
    heapq.heappush(heap, num)
for _ in range(1, N):
    for num in map(int, input().split()):
        heapq.heappush(heap, num)
        heapq.heappop(heap)
print(heapq.heappop(heap))
import heapq

nums = [5, 4, 3, 2, 1]
heap = []

if not heap:
    for num in nums:
        heapq.heappush(heap, num)

print(heap) # [1, 2, 4, 5, 3]


nums = [5, 4, 3, 2, 1]
heapq.heapify(nums)

print(nums) # [1, 2, 3, 5, 4]

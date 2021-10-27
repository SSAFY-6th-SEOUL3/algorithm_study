# 메모리 초과를 막기 위해, N x N의 표를 2차원 배열에 저장하는 대신
# 그때그때 숫자를 힙에 저장하는 방식으로 구현함. => 정답!

from heapq import heappush, heappop, heapify


N = int(input())

# 0열의 숫자들을 힙에 저장한다.
heap = [int(x) for x in input().split()]
heapify(heap)

# 1열부터 N-1열까지의 숫자들을 하나씩 힙에 저장하고,
# 그때마다 힙에서 숫자 하나를 빼서 힙의 수를 N개로 유지시킨다.
for _ in range(N - 1):
    for num in [int(x) for x in input().split()]:
        heappush(heap, num)
        heappop(heap)

# N개의 수가 저장된 힙에서 수 하나를 꺼낸다. 그 수가 전체 수중 N번째 큰 수다.
nth_number = heappop(heap)
print(nth_number)

# 결과 : 메모리 초과

from heapq import heappush, heappop


N = int(input())
board = []

for _ in range(N):
    board.append([int(x) for x in input().split()])

# cnt_rows: 각 행에 대하여 현재 탐색중인 열을 저장한 배열
cnt_rows = [N - 1] * N
heap = []

"""
마지막 열의 각 수에 대하여, (수의 음수값, 행)을 힙에 저장한다.
python의 heapq 모듈은 작은 수부터 리턴하는 min heap을 만들기 때문에
가장 큰 수부터 리턴하도록 수의 음수값을 저장함. 
"""
for i, num in enumerate(board[-1]):
    heappush(heap, (-num, i))

# 가장 큰 수부터 N - 1개를 꺼낸다.
for _ in range(N - 1):
    value, idx = heappop(heap)
    cnt_rows[idx] -= 1
    # 꺼낸 수의 바로 위에 있는 수를 힙에 저장한다.
    heappush(heap, (-board[cnt_rows[idx]][idx], idx))

# N번째로 큰 수를 꺼낸 뒤, 해당 값의 음수값(원래 수)를 출력한다.
value, idx = heappop(heap)
print(-value)

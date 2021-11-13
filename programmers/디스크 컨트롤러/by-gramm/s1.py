from heapq import heapify, heappush, heappop


def solution(jobs):
    N = len(jobs)      # N: 작업의 개수
    heapify(jobs)
    heap = []
    cnt, total = 0, 0  # cnt: 현재 시간 / total: 총 소요 시간

    while jobs:
        # 힙이 비었는데 시작할 작업이 없다면 => 새 작업이 시작될 때까지 기다린다.
        if not heap and cnt < jobs[0][0]:
            cnt = jobs[0][0]

        # 작업이 남아 있고 가장 빨리 시작하는 작업이 현재 시간보다 일찍 시작한다면
        # heap에 (소요 시간, 요청 시간)의 형태로 저장한다.
        while jobs and jobs[0][0] <= cnt:
            start, time = heappop(jobs)
            heappush(heap, (time, start))

        # 작업 하나를 꺼낸 뒤, 현재 시간과 총 소요 시간을 업데이트한다.
        time, start = heappop(heap)
        cnt += time
        total += (cnt - start)

    # 힙에 남아 있는 작업들을 하나씩 꺼낸 뒤, 현재 시간과 총 소요 시간을 업데이트한다.
    while heap:
        time, start = heappop(heap)
        cnt += time
        total += (cnt - start)

    # 평균 소요 시간을 리턴한다.
    return total // N


print(solution([[0, 3], [1, 9], [2, 6]]))    # 9
print(solution([[0, 3], [1, 9], [500, 6]]))  # 6

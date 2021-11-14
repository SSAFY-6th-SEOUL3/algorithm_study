def solution(jobs):
    from heapq import heappush, heappop
    import operator

    current = 0
    answer = 0

    l = len(jobs)
    # 작업이 요청되는 시점과 소요시간을 기준으로 정렬한다.
    jobs = sorted(jobs, key=operator.itemgetter(0, 1))
    waitings = []
    heappush(waitings, (0, jobs.pop(0)))
    while waitings:

        processing = heappop(waitings)[1]

        # 요청 시점이 현재 시점보다 나중이라면(작업 미수행) 요청시점과 소요시간을 더한다.
        if processing[0] > current:
            current = processing[0] + processing[1]
        # 요청 시점이 현재 시점보다 먼저라면 현재 시점에 소요시간을 더한다.
        else:
            current += processing[1]

        # 작업의 요청부터 종료까지 걸린 시간을 정답에 더한다.
        answer += (current - processing[0])
        while True:
            # 수행할 작업이 남아있고 작업 요청시간이 작업위치보다 앞이라면
            if jobs and jobs[0][0] < current:
                print(jobs)
                # 소요시간이 적은 일부터 대기 리스트에 추가한다. => jobs[0][1] 기준으로 힙푸시
                heappush(waitings, (jobs[0][1], jobs[0]))
                print(f'waitings{waitings}')
                jobs.pop(0)
            else:
                # 수행할 작업이 남아있고 대기 리스트가 비어있다면.. 먼저 요청 들어온 작업부터 처리한다.
                if jobs and len(waitings) == 0:

                    # 새로운 작업요청을 만날때 까지 돌린다.
                    prev = jobs[0][0]
                    while jobs:
                        job = jobs[0]

                        if job[0] != prev:
                            break

                        heappush(waitings, (job[1], job))
                        prev = job[0]
                        jobs.pop(0)

                break
    answer //= l

    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))
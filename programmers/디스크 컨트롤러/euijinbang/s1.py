# tc x
def solution(jobs):

    jobs.sort(key=lambda arr: arr[1])

    work_time = 0
    for job in jobs:
        work_time += job[1]

    wait_time = 0
    if jobs[0][0] > wait_time:
        wait_time += jobs[0][0]
    end_time = jobs[0][0] + jobs[0][1]
    for i in range(len(jobs)-1):

        if jobs[i+1][0] <= end_time:
            wait_time += end_time - jobs[i+1][0]
            end_time += jobs[i+1][1]

        if jobs[i+1][0] > end_time:
            end_time += jobs[i+1][1]

    return (work_time + wait_time) // len(jobs)


#현재 태스크의 종료 범위 안에 요청된 태스크중, 길이가 짧은 태스크 부터 수행한다
#요청 시간이 같다면, 길이가 짧은 태스크부터 수행한다
# [작업이 요청되는 시점, 작업의 소요시간]
jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)
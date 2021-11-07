import math


def solution(progresses, speeds):
    answer = []
    N = len(progresses)

    # 각 기능별 배포 가능 일수
    data = []  # ex. [7, 3, 9] : 1번 기능 7일 후 배포 가능, 2번 기능 3일 후 배포 가능, 3번 기능 9일 후 배포 가능
    for i in range(N):
        data.append(math.ceil((100 - progresses[i]) / speeds[i]))


    front = 0  # 가장 먼저 배포되어야 하는 기능의 인덱스
    for idx in range(len(data)):

        # 가장 먼저 배포되어야 하는 기능의 배포 가능 일수 < 나중에 배포되어야 하는 기능의 배포 가능 일수
        if data[front] < data[idx]:
            answer.append(idx - front)  # 그 때까지의 배포 가능한 기능의 개수 append
            front = idx  # 가장 먼저 배포되어야 하는 기능의 인덱스 갱신

    answer.append(len(data) - front)  # 마지막에 배포되는 기능의 개수 append

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
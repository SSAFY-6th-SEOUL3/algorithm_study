import math
from collections import deque


def solution(progresses, speeds):
    durations = deque()  # 작업별 남은 기간 정보를 저장하는 deque
    progresses = list(map(lambda x: 100 - x, progresses))
    for idx, speed in enumerate(speeds):
        durations.append(math.ceil(progresses[idx]/speed))
    answer = []
    prerequisite = durations.popleft()
    num = 1
    #  deque를 사용하여 선행작업과 뒷 작업의 기간 비교
    while durations:
        current = durations.popleft()
        if prerequisite >= current:
            num += 1
            continue
        else:
            answer.append(num)
            num = 1
            prerequisite = current
    else:
        answer.append(num)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
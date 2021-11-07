from collections import Counter
from math import ceil


def solution(progresses, speeds):
    # 각 기능별 완성까지 남은 날짜를 저장하는 배열
    rest_days = []

    for p, s in zip(progresses, speeds):
        # 각 기능에 대하여, 남은 진도를 속도로 나눈 값을 소수 첫째 자리에서 올린 값을 저장한다.
        rest_days.append(ceil((100 - p) / s))

    # 뒤에 있는 기능의 남은 날짜가 더 적은 경우,
    # 앞에 있는 기능의 완성까지 기다려야 하므로 해당 값으로 업데이트한다.
    for i in range(1, len(rest_days)):
        rest_days[i] = max(rest_days[i], rest_days[i - 1])

    # 남은 날짜별로 완성되는 기능의 개수를 담은 배열을 반환한다.
    # (위 for문에서 정렬되었으므로 따로 정렬할 필요 X)
    return list(Counter(rest_days).values())

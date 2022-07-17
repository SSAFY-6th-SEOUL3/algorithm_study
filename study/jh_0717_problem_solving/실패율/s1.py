def solution(N, stages):
    # counts[i]: i번째 스테이지에 도전 중인 사용자의 수
    counts = [0] * (N + 2)

    for stage in stages:
        counts[stage] += 1

    # accumulates[i]: i번째 스테이지에 도달한 사용자의 수
    accumulates = [0] * (N + 2)
    accumulates[N + 1] = counts[N + 1]

    for i in range(N, 0, -1):
        accumulates[i] = accumulates[i + 1] + counts[i]

    result = []

    for num in range(1, N + 1):
        if accumulates[num]:
            result.append([num, counts[num] / accumulates[num]])
        else:
            # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0
            result.append([num, 0])

    result.sort(key=lambda x: x[1], reverse=True)

    return [x[0] for x in result]

from collections import Counter

def solution(progresses, speeds):
    days = []

    while progresses:
        day = 0

        while progresses[0] < 100:
            progresses[0] += speeds[0]
            day += 1

        if days and day < days[-1]:
            day = days[-1]
            days.append(day)
            progresses.pop(0)
            speeds.pop(0)

        else:
            days.append(day)
            progresses.pop(0)
            speeds.pop(0)

    cnt = Counter()
    for day in days:
        cnt[day] += 1


    return list(cnt.values())

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


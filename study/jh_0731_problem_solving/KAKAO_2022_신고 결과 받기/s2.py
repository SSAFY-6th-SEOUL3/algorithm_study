def solution(id_list, report, k):
    reported_by = {name: set() for name in id_list}
    counts = {name: 0 for name in id_list}

    for info in report:
        a, b = info.split(' ')
        reported_by[b].add(a)

    for name, reporters in reported_by.items():
        if len(reporters) >= k:
            for reporter in reporters:
                counts[reporter] += 1

    return [count for count in counts.values()]

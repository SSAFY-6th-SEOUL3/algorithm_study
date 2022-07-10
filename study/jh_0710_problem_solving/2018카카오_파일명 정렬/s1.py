def solution(files):
    result = []

    for file in files:
        idx = 0

        # HEAD 구하기
        while file[idx] not in '0123456789':
            idx += 1

        head = file[:idx]
        num_start = idx

        # NUMBER 구하기
        count = 0

        while count < 5 and idx < len(file) and file[idx] in '0123456789':
            idx += 1
            count += 1

        number = file[num_start:idx]

        # TAIL 구하기
        if idx >= len(file) - 1:
            result.append([head, number])
        else:
            result.append([head, number, file[idx:]])

    result.sort(key=lambda x: int(x[1]))
    result.sort(key=lambda x: x[0].lower())

    print(result)

    return ["".join(name) for name in result]

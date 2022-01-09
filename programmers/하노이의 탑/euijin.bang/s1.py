def hanoi(n, start, end):
    if n == 0:
        return
    else:
        other = 6 - start - end

        hanoi(n-1, start, other)

        result.append([start, end])

        hanoi(n-1, other, end)

def solution(n):
    global result
    result = []
    hanoi(n, 1, 3)
    return result


# print(solution(2))
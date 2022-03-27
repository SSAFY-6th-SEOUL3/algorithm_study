def solution(brown, yellow):
    answer = []

    s = brown + yellow
    for i in range(s, 0, -1):
        if s % i == 0:
            a = s // i
            if (a - 2) * (i - 2) == yellow:
                return [i, a]
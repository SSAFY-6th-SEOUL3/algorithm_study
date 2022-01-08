"""
A에서 B로 N개를 옮기는 방법

1. A에서 C로 N - 1개를 옮긴다.
2. A에서 B로 1개를 옮긴다.
3. C에서 B로 N - 1개를 옮긴다.
"""
def move_plates(n, start, end):
    if n == 1:
        return [[start, end]]

    mid = 6 - start - end
    return move_plates(n - 1, start, mid) + [[start, end]] + move_plates(n - 1, mid, end)


def solution(n):
    return move_plates(n, 1, 3)

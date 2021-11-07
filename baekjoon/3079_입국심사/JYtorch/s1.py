import sys
sys.stdin = open('input.txt')

def solution():

    left = 1
    right = max(time) * M

    while left <= right:
        mid = (left + right) // 2

        people = 0
        for t in time:
            people += mid // t

        if people >= M:
            answer = mid
            right = mid - 1
        elif people < M:
            left = mid + 1

    return answer

N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]
print(solution())

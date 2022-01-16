import sys
sys.stdin = open('input.txt')

def solution(curv, numbers, cnt):
    global min_v, nums

    if cnt > min_v:
        return

    if curv == 1:
        if cnt < min_v:
            min_v = cnt
            nums = numbers
        return

    else:
        if curv % 2 == 0:
            solution(curv // 2, numbers + [curv // 2], cnt + 1)

        if curv % 3 == 0:
            solution(curv // 3, numbers + [curv // 3], cnt + 1)

        solution(curv - 1, numbers + [curv - 1], cnt + 1)

N = int(input())
min_v = 987654321
nums = []

solution(N, [N], 0)
print(min_v)
print(*nums)
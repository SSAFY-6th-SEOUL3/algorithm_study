import sys
sys.stdin = open('input.txt')

from itertools import combinations
# 팀별 능력치 계산
def calc(arr1, arr2):
    start_data = 0
    link_data = 0

    # start 팀 능력치 합
    for n1, n2 in combinations(arr1, 2):
        start_data += arr[n1][n2] + arr[n2][n1]

    # link 팀 능력치 합
    for m1, m2 in combinations(arr2, 2):
        link_data += arr[m1][m2] + arr[m2][m1]

    return abs(start_data - link_data)

def solution(lev, k):
    global ans
    # 두 팀으로 나누기(팀당 N // 2 명)
    if lev == N // 2:
        start = []  # start 팀원 번호
        link = []   # link 팀원 번호

        for j in range(N):
            if used[j]: start.append(j)
            else: link.append(j)
        ans = min(calc(start, link), ans)
        return

    else:
        for i in range(k, N):
            if used[i]: continue
            used[i] = 1
            solution(lev + 1, i + 1)
            used[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [0] * N
ans = 10000
lst = []
solution(0, 0)
# solution2()
print(ans)

# def solution2():
#     global ans
#     for i in range(1 << N):
#         if bin(i).count('1') == N // 2:
#             data1, data2 = [], []
#             for j in range(N):
#                 if list(format(i, 'b').zfill(N))[j] == '1': data1.append(j)
#                 else: data2.append(j)
#             total1, total2 = 0, 0
#             for n1, n2 in combinations(data1, 2):
#                 total1 += arr[n1][n2] + arr[n2][n1]
#             for m1, m2 in combinations(data2, 2):
#                 total2 += arr[m1][m2] + arr[m2][m1]
#             ans = min(ans, abs(total1 - total2))






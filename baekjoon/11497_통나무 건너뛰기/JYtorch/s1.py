import sys
sys.stdin = open('input.txt')

def solution2():
    heights = sorted(L)
    diff = 0
    for i in range(2, N):
        diff = max(diff, abs(heights[i] - heights[i - 2]))
    return diff

T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    # used = [0] * N
    # ans = 987654321
    # solution(0, [])
    print(solution2())


# 순열로는 풀 수 없는 문제인가요? 중복된 통나무 배열을 걸러주는 방법이 있을까요? 시간초과가 뜹니다...
# def solution(k, heights):
#     global ans
#     if len(heights) >= 2:
#         if abs(heights[k - 1] - heights[k - 2]) > ans:
#             return
#     if k == N:
#         max_diff = 0
#         print(heights)
#         for j in range(N):
#             if j == N - 1:
#                 diff = abs(heights[0] - heights[N - 1])
#             else:
#                 diff = abs(heights[j] - heights[j + 1])
#             max_diff = max(max_diff, diff)
#         ans = min(max_diff, ans)
#         return
#     else:
#         for i in range(N):
#             if used[i]: continue
#             used[i] = 1
#             solution(k + 1, heights + [L[i]])
#             used[i] = 0

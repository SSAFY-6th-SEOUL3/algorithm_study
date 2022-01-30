import sys
sys.stdin = open('input.txt')

"""
PyPy3
"""

# 사다리 출발점과 도착점의 열이 같은지 확인
def play():
    for i in range(1, N + 1):
        r = 0
        c = i
        while r != H:
            if board[r][c]:
                c += 1
            elif board[r][c-1]:
                c -= 1
            r += 1
        if i != c:
            return False
    return True

# def solution(start, cnt):
#     global ans
#
#     if cnt >= ans:
#         return
#
#     if play():
#         if ans > cnt:
#             ans = cnt
#         return
#
#     if cnt == 3:
#         return
#
#     for i in range(start, N * H):
#         r = i // N
#         c = i % N
#
#         if c < N - 1 and board[r][c] == 0:
#
#             if (c == 0 and board[r][c + 1] == 0)\
#                 or (c == N - 2 and board[r][c - 1] == 0)\
#                 or (0 < c < N - 2 and board[r][c - 1] == board[r][c + 1] == 0):
#                 board[r][c] = 1
#                 solution(N * r + c + 1, cnt + 1)
#                 board[r][c] = 0
#     return
# board에 가로선 채우기(최대 3개까지)
def solution2(start, cnt):
    global ans

    # 가지치기
    if cnt >= ans:
        return

    # 조건에 만족하는 사다리면 cnt 갱신
    if play():
        ans = cnt
        return

    # 가로선 3개 다 그으면 종료
    if cnt == 3:
        return

    # start부터 N * H 까지 돌면서 board에 가로선 긋기
    for i in range(start, N * H):
        r = i // N
        c = i % N

        if c < N - 1:
            if board[r][c] == board[r][c + 1] == 0:
                board[r][c] = 1
                board[r][c + 1] = -1

                solution2(r * N + c + 1, cnt + 1)

                board[r][c] = 0
                board[r][c + 1] = 0

N, M, H = map(int, input().split())
rows_info = [list(map(int, input().split())) for _ in range(M)]

board = [[0] * (N + 1) for _ in range(H + 1)]
ans = 4

# 1을 만나면 오른쪽으로, -1을 만나면 왼쪽으로 가도록 표시
for y, x in rows_info:
    board[y-1][x-1] = 1
    board[y-1][x] = -1

solution2(0, 0)
if ans == 4:
    ans = -1
print(ans)


#################################################

# # 사다리 확인
# def play():
#     for i in range(N):
#         r = 0
#         c = i
#         while r != H:
#             if board[r][c] == 1:
#                 c += 1
#             elif board[r][c] == -1:
#                 c -= 1
#             r += 1
#         if c != i: return False
#     return True
#
#
# # board에 가로선 최대 3개씩 채워가면서 체크하기
# def solution(start, cnt):
#     global ans
#
#     if cnt == 3 or start >= N * H:
#         if play():
#             return cnt
#         return 4
#
#     r = start // N
#     c = start % N
#
#     if c + 1 < N:
#         if board[r][c] == board[r][c + 1] == 0:
#             board[r][c] = 1
#             board[r][c + 1] = -1
#
#             ans = min(ans, solution(start + 2, cnt + 1))
#
#             board[r][c] = 0
#             board[r][c + 1] = 0
#
#     ans = min(ans, solution(start + 1, cnt))
#     return ans
#
# N, M, H = map(int, input().split())
# rows_info = [list(map(int, input().split())) for _ in range(M)]
#
# board = [[0] * N for _ in range(H)]
# ans = 4
#
# # 1: 오른쪽, -1: 왼쪽
# for y, x in rows_info:
#     board[y-1][x-1] = 1
#     board[y-1][x] = -1
#
# ans = solution(0, 0)
#
# if ans == 4:
#     print(-1)
# else:
#     print(ans)
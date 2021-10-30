import sys
sys.stdin = open('input.txt')

# 메모리 초과

N = int(input())
board = [list(map(int, input().split())) for x in range(N)]


maxnum = 0
for i in range(N):
    for j in range(N):
        maxnum = max(board[i][j], maxnum)

arr = []
for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        arr.append(maxnum - board[i][j])
        arr.sort()

print(maxnum - arr[N-1])


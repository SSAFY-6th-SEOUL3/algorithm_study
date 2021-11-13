import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
board = [[0]*N for _ in range(N)]

for i in range(N):
    board[i][i] = numbers[i] % M

for i in range(N):
    for j in range(i+1, N):
        board[i][j] = (board[i][j-1] + numbers[j]) % M

print(board)

result = 0
for i in range(N):
    for j in range(i, N):
        if board[i][j] == 0:
            result += 1

print(result)

import sys
sys.stdin = open('input.txt')
N = int(input())

board = [[0]*101 for _ in range(101)]
dc = (1, 0, -1, 0)
dr = (0, -1, 0, 1)
directions = [0]
answer = 0

for i in range(1, 11):
    k = 1<<(i-1)  # 비트마스킹
    for j in range(k):
        # 0 -(+1)-> 1 -(+1)-> 2  1 -(+1)-> 2, 3, 2, 1
        directions.append((directions[k-j-1]+1) % 4)

for _ in range(N):
    col, row, d, g = map(int, input().split())
    board[row][col] = 1
    for i in range(1<<g):
        row, col = row + dr[(directions[i]+d) % 4], col+dc[(directions[i]+d) % 4]
        board[row][col] = 1

for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            answer += 1

print(answer)
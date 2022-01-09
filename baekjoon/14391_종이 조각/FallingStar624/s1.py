# 비트마스킹
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, list(input()))))


max_num = 0
for i in range(1 << N*M):
    total = 0
    num = format(i, 'b')
    current = '0'*(N*M-len(num)) + str(num)

    for row in range(N):
        row_sum = 0
        for col in range(M):
            idx = row * M + col
            if current[idx] == '0':
                row_sum = row_sum*10 + paper[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for col in range(M):
        col_sum = 0
        for row in range(N):
            idx = row*M + col
            if current[idx] == '1':
                col_sum = col_sum*10 + paper[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    max_num = max(total, max_num)

print(max_num)

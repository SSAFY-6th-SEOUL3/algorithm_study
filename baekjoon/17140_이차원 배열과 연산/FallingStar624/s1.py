import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')

r, c, k = map(int, sys.stdin.readline().split())
r -= 1
c -= 1
arr = []
for _ in range(3):
    arr.append(list(map(int, sys.stdin.readline().split())))
row_max = 3
col_max = 3
cnt = 0

while True:
    if arr[r][c] == k:
        print(cnt)
        break
    if cnt > 100:
        print(-1)
        break
    calculated_arr = []
    rotated = False
    max_length = 0
    # R 연산
    if row_max >= col_max:
        new_arr = arr
    else:
        new_arr = list(map(list, zip(*arr)))
        rotated = True

    for row in new_arr:
        new_row = []
        tmp = list((Counter(row)).items())
        tmp.sort(key=lambda x: (x[1], x[0]))
        for result in tmp:
            if result[0] == 0:
                pass
            else:
                new_row.append(result[0])
                new_row.append(result[1])
            if len(new_row) > max_length:
                max_length = len(new_row)
        calculated_arr.append(new_row)

    for row in calculated_arr:
        if len(row) < max_length:
            row += [0]*(max_length-len(row))

    if rotated:
        arr = list(map(list, zip(*calculated_arr)))
    else:
        arr = calculated_arr
    row_max = len(arr)
    col_max = len(arr[0])
    cnt += 1


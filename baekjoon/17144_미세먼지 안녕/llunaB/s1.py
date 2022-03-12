"""
replace : 1018_체스판 다시 칠하기
"""

N, M = map(int, input().split())

arr = []
count_list = []

for _ in range(N):
    arr.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        index1 = 0  # 'W'로 시작할 경우 바뀐 체스 판의 개수
        index2 = 0  # 'B'로 시작할 경우 바뀐 체스 판의 개수

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if arr[a][b] != 'W':
                        index1 += 1
                    if arr[a][b] != 'B':
                        index2 += 1
                else:
                    if arr[a][b] != 'B':
                        index1 += 1
                    if arr[a][b] != 'W':
                        index2 += 1

        count_list.append(min(index1, index2))

print(min(count_list))

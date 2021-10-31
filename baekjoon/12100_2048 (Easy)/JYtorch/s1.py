import sys
sys.stdin = open('input.txt')
import copy
from itertools import product
from collections import deque

"""

swea 벽돌 깨기 문제와 비슷하게 접근했습니다.

"""

def solution(arr, directions):
    global ans

    for d in directions:
        # 오른쪽으로 보내는 경우   (한쪽 방향만 이해하면 나머지는 거의 똑같습니다.)
        if d == 0:

            for r in range(N):
                row_list = []
                temp_list = deque()

                for c in range(N-1, -1, -1):  # 블록을 오른쪽으로 보낼 경우에는, 맨 오른쪽에 가까운 숫자부터 합쳐짐
                                              # 따라서 맨 오른쪽에서 왼쪽 방향으로 탐색(<=)

                    if arr[r][c]:                       # 숫자가 있으면 temp_list에 담는다.
                        temp_list.append(arr[r][c])

                    if len(temp_list) == 2:             # temp_list에 숫자 두개가 모이면 pop으로 하나씩 빼서 같은 숫자인지 비교한다.
                        v1 = temp_list.popleft()
                        v2 = temp_list.popleft()
                        if v1 == v2:                    # 두개의 숫자가 같으면, row_list에 합친 숫자를 넣는다.
                            row_list.append(v1*2)
                        else:
                            row_list.append(v1)         # 두개의 숫자가 다르면, 먼저 뺏던 숫자(v1)는 더 이상 합쳐질리 없으니 row_list에 넣고
                            temp_list.append(v2)        # 나중에 뺏던 숫자(v2)는 다시 temp_list에 넣어준다.
                                                        # 이 과정이 끝까지 이루어지면 합쳐질 숫자는 다 합쳐진 상태로 row_list가 채워진다.


                if temp_list:                           # temp_list에 남은 숫자가 있으면 마지막으로 넣어준다.
                    row_list.append(temp_list[0])

                for i in range(N-1, -1, -1):            # 이제 다 합쳐진 숫자를 게임보드에 다시 배치해야할 차례다.
                    if N-1-i < len(row_list):           # row_list에 있는 숫자를 게임보드의 맨 오른쪽에서부터 순서대로 다 채운다.
                        arr[r][i] = row_list[N-1-i]
                    else:
                        arr[r][i] = 0                   # row_list에 있는 숫자를 다 채워서 더 이상 채울 숫자가 없으면
                                                        # 나머지 게임보드 공간을 0으로 채운다.(빈 공간이므로)


        # 아래로 보내는 경우
        if d == 1:

            for c in range(N):
                col_list = []
                temp_list = deque()

                for r in range(N - 1, -1, -1):

                    if arr[r][c]:
                        temp_list.append(arr[r][c])

                    if len(temp_list) == 2:
                        v1 = temp_list.popleft()
                        v2 = temp_list.popleft()
                        if v1 == v2:
                            col_list.append(v1 * 2)
                        else:
                            col_list.append(v1)
                            temp_list.append(v2)

                if temp_list:
                    col_list.append(temp_list[0])

                for i in range(N - 1, -1, -1):
                    if N - 1 - i < len(col_list):
                        arr[i][c] = col_list[N - 1 - i]
                    else:
                        arr[i][c] = 0
        # 왼쪽으로 보내는 경우
        if d == 2:

            for r in range(N):
                row_list = []
                temp_list = deque()

                for c in range(N):

                    if arr[r][c]:
                        temp_list.append(arr[r][c])

                    if len(temp_list) == 2:
                        v1 = temp_list.popleft()
                        v2 = temp_list.popleft()
                        if v1 == v2:
                            row_list.append(v1 * 2)
                        else:
                            row_list.append(v1)
                            temp_list.append(v2)

                if temp_list:
                    row_list.append(temp_list[0])

                for i in range(N):
                    if i < len(row_list):
                        arr[r][i] = row_list[i]
                    else:
                        arr[r][i] = 0
        # 위로 보내는 경우
        if d == 3:

            for c in range(N):
                col_list = []
                temp_list = deque()

                for r in range(N):

                    if arr[r][c]:
                        temp_list.append(arr[r][c])

                    if len(temp_list) == 2:
                        v1 = temp_list.popleft()
                        v2 = temp_list.popleft()
                        if v1 == v2:
                            col_list.append(v1 * 2)
                        else:
                            col_list.append(v1)
                            temp_list.append(v2)

                if temp_list:
                    col_list.append(temp_list[0])

                for i in range(N):
                    if i < len(col_list):
                        arr[i][c] = col_list[i]
                    else:
                        arr[i][c] = 0

    # 최종적으로 구해진 블록의 최대값과 ans를 비교한 뒤 더 큰 값을 갱신
    for a in arr:
        if ans < max(a):
            ans = max(a)


N = int(input())

temp_mat = [list(map(int, input().split())) for _ in range(N)]

# mat : 게임보드
mat = copy.deepcopy(temp_mat)

# 0: 우, 1: 하, 2: 좌, 3: 상
# 우, 하, 좌, 상 방향을 각각 0, 1, 2, 3으로 놓고 5개씩 선택
# `우우우우우`부터 `상상상상상`까지 전부 다 플레이해보는 전략
# d_list : [(0, 0, 0, 0, 0), (0, 0, 0, 0, 1) ... (3, 3, 3, 3, 2), (3, 3, 3, 3, 3)]
d_list = list(product(range(4), repeat=5))

ans = 0
for direction in d_list:            # ex. direction에 (0, 0, 0, 0, 0) 형태의 튜플이 들어오면 총 5번 우측으로 보낸다는 뜻
    solution(mat, direction)
    mat = copy.deepcopy(temp_mat)   # solution 함수를 다 돌고 나올 때마다 mat을 처음 제공된 게임보드로 갱신

print(ans)
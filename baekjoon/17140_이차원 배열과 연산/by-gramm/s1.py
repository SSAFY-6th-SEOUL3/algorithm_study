
def count_and_sort(arr):
    """
    배열의 각 수와 등장 횟수를, i) 등장 횟수가 적은 순으로 / ii) 수가 작은 순으로 정렬한다.
    ex. [3, 1, 1, 2] => [2, 1, 3, 1, 1, 2]
    """
    count_dict = dict()

    for x in arr:
        count_dict[x] = count_dict.get(x, 0) + 1

    if 0 in count_dict:     # 0의 개수는 count에 포함시키지 않는다.
        del count_dict[0]

    temp = []
    result = []

    for value, count in count_dict.items():
        temp.append((value, count))

    temp.sort(key=lambda x: x[0])  # ii) 수가 작은 순으로 정렬
    temp.sort(key=lambda x: x[1])  # i) 등장 횟수가 적은 순으로 정렬

    for a, b in temp[:50]:  # 100개를 넘어가는 경우, 100개 이후로는 버린다.
        result.append(a)
        result.append(b)

    return result


def inverse_matrix(board, c_length):
    """
    2차원 배열의 행과 열을 반전시킨다.
    ex. 1 2 3    1 4 7
        4 5 6 => 2 5 8
        7 8 9    3 6 9
    """
    new_board = []

    for c in range(c_length):
        new_board.append([arr[c] for arr in board])

    return new_board


def fill_zero(board, c_length):
    """
    주어진 2차원 배열에서 가장 큰 행의 크기만큼 0을 채워준다.
    ex. 1 2        1 2 0 0
        3 4 5 6 => 3 4 5 6
        7          7 0 0 0
    """
    for sub_arr in board:
        sub_arr += [0] * (c_length - len(sub_arr))


r, c, k = map(int, input().split())
r, c = r - 1, c - 1  # 행과 열을 1부터 세므로 1씩 빼준다.
board = []

for _ in range(3):
    board.append([int(x) for x in input().split()])

r_length, c_length = 3, 3

for time in range(101):
    # board[r][c]가 있는지 확인한 뒤, 있다면 k인지 확인한다.
    if r < r_length and c < c_length:
        if board[r][c] == k:
            print(time)
            break

    # 행의 개수 >= 열의 개수인 경우 : R연산
    if r_length >= c_length:
        for i, sub_arr in enumerate(board):
            board[i] = count_and_sort(sub_arr)

        c_length = max([len(sub_arr) for sub_arr in board])
        fill_zero(board, c_length)
    # 열의 개수 < 행의 개수인 경우 : C연산 (행렬 반전 => R 연산 => 행렬 반전)
    else:
        board = inverse_matrix(board, c_length)
        r_length, c_length = c_length, r_length

        for i, sub_arr in enumerate(board):
            board[i] = count_and_sort(sub_arr)
        c_length = max([len(sub_arr) for sub_arr in board])
        fill_zero(board, c_length)

        board = inverse_matrix(board, c_length)
        r_length, c_length = c_length, r_length
else:
    print(-1)

from collections import deque


def solution(board, moves):
    cnt = 0
    N = len(board)
    moves = deque(moves)
    basket = []
    while moves:
        lane = moves.popleft() - 1
        for col in range(N):
            if board[col][lane] > 0:
                basket.append(board[col][lane])
                board[col][lane] = 0
                break
        if len(basket) > 1 and basket[-1] == basket[-2]:
            cnt += 2
            basket = basket[:-2]

    return cnt



arr1 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
arr2 = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(arr1, arr2))
def solution(n):
    directions = [0, 1, 2] # 하, 우, 좌상
    board = [[0]*n for _ in range(n)]
    row, col = 0, 0
    num = 0
    direction = directions[0]
    while num < n*(n+1)/2:
        num += 1
        board[row][col] = num
        if direction == 0:
            if -1 < row+1 < n and board[row+1][col] == 0:
                row += 1
            else:
                direction = 1
                col += 1
        elif direction == 1:
            if -1 < col+1 < n and board[row][col+1] == 0:
                col += 1
            else:
                direction = 2
                row -= 1
                col -= 1
        else:  # direction == 2 (왼쪽 위 대각선 방향)
            if -1 < row-1 < n and -1 < col-1 < n and board[row-1][col-1] == 0:
                row -= 1
                col -= 1
            else:
                direction = 0
                row += 1

    answer = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                answer.append(board[i][j])
    return answer


print(solution(4))
print(solution(5))
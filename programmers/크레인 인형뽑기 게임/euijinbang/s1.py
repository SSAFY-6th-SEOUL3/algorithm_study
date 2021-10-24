def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)

    for i in range(N):
        board[i].insert(0, 0)
    board = [[0] * (N+1)] + board

    print(board)

    for col in moves:
        for row in range(1, N+1):
            if board[row][col]:
                if len(stack) != 0 and stack[-1] == board[row][col]:
                    stack.pop()
                    answer += 2
                    board[row][col] = 0
                    break
                else:
                    stack.append(board[row][col])
                    board[row][col] = 0
                    break

    return answer



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
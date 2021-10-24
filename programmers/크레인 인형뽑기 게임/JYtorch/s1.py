board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    N = len(board)
    bags = []

    for move in moves:
        for i in range(N):
            if board[i][move-1]:
                bags.append(board[i][move-1])
                if len(bags) >= 2 and bags[len(bags)-1] == bags[len(bags)-2]:
                    bags.pop()
                    bags.pop()
                    answer += 2
                board[i][move-1] = 0
                break
    return answer

print(solution(board, moves))
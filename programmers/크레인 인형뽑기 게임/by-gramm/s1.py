
def solution(board, moves):
    N = len(board)  # 격자의 가로, 세로 길이
    basket = []     # 인형 바구니 (일종의 스택)
    count = 0       # 터트려져 사라진 인형의 개수

    for move in moves:
        c = move - 1
        # 위에서부터 인형이 있는지 검사한다.
        for r in range(N):
            # 인형을 발견했다면
            if board[r][c]:
                # 1) 바구니 맨 위에 있는 인형과 같은 경우 => 바구니의 인형 제거 및 count 업데이트
                if basket and board[r][c] == basket[-1]:
                    basket.pop()
                    count += 2
                # 2) 바구니 맨 위에 있는 인형과 다른 경우 => 바구니에 새 인형 추가
                else:
                    basket.append(board[r][c])

                # 인형을 꺼낸 칸을 빈 공간으로 만들고, 반복문을 빠져 나온다.
                board[r][c] = 0
                break

    return count

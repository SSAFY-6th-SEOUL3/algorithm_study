def get_min_price(count, cnt_price):
    """
    Params:
        count: 현재까지 선택한 제품의 개수
        cnt_price: 현재까지 선택한 제품의 총 생산비용
    """
    global N, board, factory_selected, min_price

    # 모든 제품을 다 선택한 경우
    if count == N:
        min_price = min(min_price, cnt_price)
        return

    for c in range(N):
        if not factory_selected[c] and cnt_price + board[count][c] < min_price:  # backtracking
            factory_selected[c] = True
            get_min_price(count + 1, cnt_price + board[count][c])
            factory_selected[c] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = []

    factory_selected = [False] * N
    min_price = 123456789

    for _ in range(N):
        board.append([int(x) for x in input().split()])

    get_min_price(0, 0)

    print(f"#{tc} {min_price}")

from heapq import heappush, heappop


def solution(n, s, a, b, fares):
    MAX_INF = 123456789
    # prices[n1][n2]: n1에서 n2 혹은 n2에서 n1로 이동하는 택시 요금
    prices = [[MAX_INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        prices[i][i] = 0

    for n1, n2, fare in fares:
        prices[n1][n2] = fare
        prices[n2][n1] = fare

    # 출발지점, A의 도착지점, B의 도착지점에서 각 지점까지의 최소 금액을 구한다.
    s_min_prices = [MAX_INF] * (n + 1)
    a_min_prices = [MAX_INF] * (n + 1)
    b_min_prices = [MAX_INF] * (n + 1)

    for std_node, min_prices in zip([s, a, b], [s_min_prices, a_min_prices, b_min_prices]):
        heap = []
        heappush(heap, [0, std_node])
        min_prices[std_node] = 0

        while heap:
            price, node = heappop(heap)

            for idx in range(1, n + 1):
                new_price = price + prices[node][idx]

                if new_price < min_prices[idx]:
                    min_prices[idx] = new_price
                    heappush(heap, [new_price, idx])

    min_fare = MAX_INF

    # 각 지점을 합승 도착 지점으로 할 때의 최소 요금을 탐색하여
    # A와 B가 각자의 목적지로 도착하는 최소 요금을 구한다.
    for mid in range(1, n + 1):
        current = s_min_prices[mid] + a_min_prices[mid] + b_min_prices[mid]
        min_fare = min(min_fare, current)

    return min_fare

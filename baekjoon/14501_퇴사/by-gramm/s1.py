
N = int(input())
max_prices = [0] * (N + 1)  # max_prices[i]: i일째까지 상담으로 받을 수 있는 최대 금액
schedules = []

for _ in range(N):
    T, P = map(int, input().split())
    schedules.append((T, P))

for i, schedule in enumerate(schedules, 1):
    time, price = schedule  # i일에 시작하는 상담의 기간 / 가격

    # i일에 시작하는 상담이 끝나는 시점부터 마지막 날까지의 최대 금액을 업데이트한다.
    # i일에 시작한 상담을 끝낼 수 없는 경우 => i + time - 1이 N보다 크므로 변화 X
    for j in range(i + time - 1, N + 1):
        if max_prices[j] < max_prices[i - 1] + price:
            max_prices[j] = max_prices[i - 1] + price
        else:
            break

print(max_prices[-1])

n, k = map(int, input().split())
coins = set()

for _ in range(n):
    current = int(input())

    if current <= k:
        coins.add(current)

# 중복 제거 후 오름차순 정렬
coins = sorted(list(coins))

# DP: 1원부터 k원까지 해당 금액을 만드는 동전의 최소 개수를 구한다.
min_counts = [12345] * (k + 1)

for price in range(1, k + 1):
    if price in coins:
        min_counts[price] = 1
    else:
        for coin in coins:
            # coins는 오름차순 정렬되어 있으므로 price - coin이 0보다 작다면
            # 나머지 동전도 모두 (price - coin < 0)이므로 탐색 종료
            if price - coin < 0:
                break
            min_counts[price] = min(min_counts[price], min_counts[price - coin] + 1)

if min_counts[k] == 12345:
    print(-1)
else:
    print(min_counts[k])

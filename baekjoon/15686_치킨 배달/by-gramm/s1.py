"""
완전 탐색: M개의 치킨집을 고르는 모든 조합에 대하여, 도시의 치킨 거리를 탐색한다.
"""
from itertools import combinations


def get_chicken_distance(loc1, loc2):
    r1, c1 = loc1
    r2, c2 = loc2

    return abs(r1 - r2) + abs(c1 - c2)


N, M = map(int, input().split())
board = []
houses = set()            # 모든 집의 set
chicken_stores = set()    # 모든 치킨집의 set

for _ in range(N):
    board.append([int(x) for x in input().split()])

# 집, 치킨집의 위치를 각각 houses, chicken_stores에 저장한다.
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            houses.add((r, c))
        if board[r][c] == 2:
            chicken_stores.add((r, c))

min_city_distance = 123456   # 도시의 치킨 거리의 최소값

for store_sets in combinations(chicken_stores, M):
    min_distance = 0   # 현재 store_sets을 채택한 경우의 도시의 치킨 거리

    # 각 가정집의 치킨 거리를 구하여, min_distance에 더한다.
    for house in houses:
        min_distance += min([get_chicken_distance(house, store) for store in store_sets])

    min_city_distance = min(min_city_distance, min_distance)

print(min_city_distance)

# DFS + 백트래킹 => 시간초과

from sys import stdin


def get_max_value(idx, weight, value):
    """
    배낭에 넣을 수 있는 물건들의 최대 가치를 구한다.
    Args:
        idx: 현재 탐색중인 가방의 인덱스
        weight: 현재까지 찾은 무게의 합
        value: 현재까지 찾은 가치의 합
    """
    global visited, N, K, max_value, infos

    # 모든 물건을 다 탐색한 경우 => max_value를 업데이트하고 리턴한다.
    if idx == N:
        max_value = max(max_value, value)
        return

    # 더 이상 넣을 수 있는 물건이 없는 경우 => max_value를 업데이트하고 리턴한다.
    # (무게가 가벼운 것이 앞에 오도록 정렬했으므로
    # 현재 물건을 넣을 수 없다면, 그 뒤에 있는 물건들도 넣을 수 없음.)
    if weight + infos[idx][0] > K:
        max_value = max(max_value, value)
        return

    # 현재 물건을 넣는 경우와 넣지 않는 경우로 나누어 DFS 탐색
    # 1) 현재 물건을 넣는 경우
    get_max_value(idx + 1, weight + infos[idx][0], value + infos[idx][1])
    # 2) 현재 물건을 넣지 않는 경우
    get_max_value(idx + 1, weight, value)


N, K = map(int, stdin.readline().split())
visited = [False] * N
max_value = 0

# infos: 각 물건의 정보를 (무게, 가치)의 형태로 저장한 배열
infos = []

for _ in range(N):
    W, V = map(int, stdin.readline().split())
    infos.append((W, V))

# 1. 무게가 무거운 것부터 / 2. 가치가 높은 것부터 정렬
infos.sort(key=lambda x: x[1], reverse=True)
infos.sort(key=lambda x: x[0], reverse=True)

get_max_value(0, 0, 0)
print(max_value)

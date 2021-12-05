
from heapq import heappush, heappop


def get_item_count(start):
    """
    start번 지역에서 출발하여 얻을 수 있는 아이템의 개수를 구한다. (다익스트라 활용)
    """
    global n, m, r, items

    distances = [1000000] * (n + 1)
    visited = [False] * (n + 1)
    heap = [(0, start)]

    while heap:
        # 매번 힙에서 시작점으로부터의 거리가 가장 가까운 노드의 (거리, 노드)를 꺼낸다.
        dist, node = heappop(heap)
        # 시작점에서 노드까지의 거리가 m보다 크다면 => 탐색 종료
        if dist > m:
            break
        # 이미 방문한 노드라면 => 현재 노드 탐색 종료 후 계속 진행
        if visited[node]:
            continue

        distances[node] = dist
        visited[node] = True

        for i in range(1, n + 1):
            # 아직 방문하지 않았고, 현재 노드와 연결된 모든 노드에 대하여
            if not visited[i] and adj_matrix[node][i] < 1000000:
                # 현재 노드를 통해 갈 수 있는 경로의 (거리, 노드)를 heap에 넣는다.
                heappush(heap, (dist + adj_matrix[node][i], i))

    count = 0

    for idx, distance in enumerate(distances):
        # 시작점으로부터의 거리가 m 이하인 모든 지역에 대하여
        if distance <= m:
            # 해당 지역의 아이템의 개수를 더한다.
            count += items[idx]

    return count


n, m, r = map(int, input().split())
# items[i] = i번 지역에 있는 아이템의 수
items = [0] + [int(x) for x in input().split()]
# adj_matrix[i][j] = i번 지역과 j번 지역 사이의 거리
adj_matrix = [[1000000] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    adj_matrix[a][b] = l
    adj_matrix[b][a] = l


max_count = 0

for i in range(1, n + 1):
    max_count = max(max_count, get_item_count(i))

print(max_count)

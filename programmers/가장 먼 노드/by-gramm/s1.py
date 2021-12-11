from collections import deque


def solution(n, edge):
    """"
    Args:
        n: 노드의 개수
        edge: 간선 정보 (배열의 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있음을 의미함.)

    Returns:
        1번 노드로부터 가장 멀리 떨어진 노드의 개수
    """
    adj_graph = [[] for _ in range(n + 1)]  # n이 최대 20,000이므로 인접 행렬 대신 인접 그래프로 구현함.
    distances = [1234567] * (n + 1)

    for x, y in edge:
        adj_graph[x].append(y)
        adj_graph[y].append(x)

    distances[1] = 0
    queue = deque()
    queue.append((1, 0))

    # BFS로 탐색하며 1번 노드로부터 각 노드로의 거리를 구한다.
    while queue:
        node, distance = queue.popleft()

        for i in adj_graph[node]:
            if distances[i] == 1234567:
                distances[i] = distance + 1
                queue.append((i, distance + 1))

    max_dist, count = 0, 0

    for i in range(1, n + 1):
        if distances[i] > max_dist:     # 1번 노드에서 i번 노드까지의 거리가 max_dist보다 큰 경우
            max_dist = distances[i]     # max_dist를 업데이트하고
            count = 1                   # count를 1로 초기화한다.
        elif distances[i] == max_dist:  # 1번 노드에서 i번 노드까지의 거리가 max_dist와 같은 경우
            count += 1                  # count에 1을 더한다.

    return count


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

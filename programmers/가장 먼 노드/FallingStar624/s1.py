# BFS 시간초과 -> 연결 리스트 + 탐색 범위 축소
from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for way in edge:
        graph[way[0]].append(way[1])
        graph[way[1]].append(way[0])

    visited = [0] * (n+1)
    visited[1] = 0.5
    Q = deque([1])
    while Q:
        current_node = Q.popleft()
        for next_node in graph[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[current_node] + 1
                Q.append(next_node)

    answer = 0
    maximum = max(visited)
    for v in visited:
        if v == maximum:
            answer += 1
    return answer


vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6, vertex))

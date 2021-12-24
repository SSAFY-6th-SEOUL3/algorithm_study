from collections import deque

def solution(n, edge):
    visited = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in range(len(edge)):
        x, y = edge[i][0], edge[i][1]
        adj[x].append(y)
        adj[y].append(x)

    q = deque([1])
    visited[1] = 1

    while q:
        v = q.popleft()
        for w in adj[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)

    # visited = [0, 1, 2, 2, 3, 3, 3]
    counter = [0] * (max(visited)+1)
    for i in range(n+1):
        counter[visited[i]] += 1
    # counter = [1, 1, 2, 3]
    return counter[max(visited)]

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6, vertex))
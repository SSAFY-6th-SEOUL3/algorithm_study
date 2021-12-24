from collections import deque


def solution(n, edge):
    adj_list = [[] for _ in range(n + 1)]
    for i in range(len(edge)):
        n1, n2 = edge[i]
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # q = deque([1])
    q = [0] * 50000
    q_len = len(q)
    front, rear = 0, 0
    rear = (rear + 1) % q_len
    q[rear] = 1
    visited = [0] * (n + 1)
    visited[1] = 1
    max_v = 0

    # while q:
    while (rear + 1) % q_len != front:

        # i = q.popleft()
        front = (front + 1) % q_len
        i = q[front]


        for j in adj_list[i]:
            if not visited[j]:
                visited[j] = visited[i] + 1
                # q.append(j)
                rear = (rear + 1) % q_len
                q[rear] = j
                if max_v < visited[j]:
                    max_v = visited[j]

    return visited.count(max_v)

print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
import sys
sys.stdin = open('input.txt', 'r')

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
route = [[987654321]*(n+1) for _ in range(n+1)]
for _ in range(r):
    start, end, length = map(int, input().split())
    route[start][end] = length
    route[end][start] = length

for i in range(1, n+1):
    route[i][i] = 0

result = []
for start in range(1, n+1):
    cost = [0]*(n+1)
    visited = [0]*(n+1)
    visited[start] = 1
    for end in range(n+1):
        cost[end] = route[start][end]

    for _ in range(r):
        minCost = 987654321
        w = 0

        for i in range(1, n+1):
            if visited[i] == 0 and minCost > cost[i]:
                minCost = cost[i]
                w = i

        visited[w] = 1

        for j in range(1, n+1):
            if 0 < route[w][j] < 10000:
                cost[j] = min(cost[j], cost[w]+route[w][j])
    cnt = 0
    for idx, dist in enumerate(cost):
        if dist <= m:
            cnt += items[idx]

    result.append(cnt)
print(max(result))






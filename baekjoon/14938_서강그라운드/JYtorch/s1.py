import sys
sys.stdin = open('input.txt')

def dijkstra(t):
    key = [0] + [987654321] * n
    visited = [0] * (n+1)

    key[t] = 0

    for _ in range(n):
        min_idx = -1
        min_value = 987654321
        for i in range(1, n + 1):
            if not visited[i] and min_value > key[i]:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1

        for i in range(1, n + 1):
            if not visited[i] and key[i] > key[min_idx] + adj_arr[min_idx][i]:
                key[i] = key[min_idx] + adj_arr[min_idx][i]

    return key


n, m, r = map(int, input().split())
T = [0] + list(map(int, input().split()))
adj_arr = [[987654321] * (n + 1) for _ in range(n + 1)]
max_items = 0

for i in range(r):
    a, b, l = map(int, input().split())
    adj_arr[a][b] = l
    adj_arr[b][a] = l

for i in range(1, n + 1):
    items = dijkstra(i)
    total = 0
    for j in range(1, n + 1):
        if items[j] <= m:
            total += T[j]
    max_items = max(total, max_items)

print(max_items)
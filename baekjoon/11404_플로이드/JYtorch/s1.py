import sys
sys.stdin = open('input.txt')

def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j: adj_arr[i][j] = 0
                else: adj_arr[i][j] = min(adj_arr[i][j], adj_arr[i][k] + adj_arr[k][j])


########################################################
def dijkstra(c):
    dist = [987654321] * (n + 1)
    visited = [0] * (n + 1)
    dist[c] = 0

    for _ in range(n):
        min_value = 987654321
        min_idx = -1

        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_value:
                min_value = dist[i]
                min_idx = i

        visited[min_idx] = 1

        for i in range(1, n + 1):
            if not visited[i] and dist[i] > adj_arr[min_idx][i] + dist[min_idx]:
                dist[i] = adj_arr[min_idx][i] + dist[min_idx]

    for i in range(1, n + 1):
        if dist[i] == 987654321:
            dist[i] = 0

    return ' '.join(map(str, dist[1:]))

######################################################
n = int(input())
m = int(input())

adj_arr = [[987654321] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    if adj_arr[a][b] > c:
        adj_arr[a][b] = c

for j in range(1, n+1):
    print(dijkstra(j))

# floyd()
#
# for i in range(1, n + 1):
#     print(*adj_arr[i][1:])




# def dijkstra(c):
#     dist = [987654321] * (n + 1)
#     city = [0] * (n + 1)
#     dist[c] = 0
#
#     for v in range(1, n + 1):
#         if adj_arr[c][v]:
#             dist[v] = adj_arr[c][v]
#     min_idx = c
#
#     while sum(city) < n+1:
#         now_pos = min_idx
#         city[now_pos] = 1
#         for i in range(1, n + 1):
#             if adj_arr[now_pos][i] and dist[now_pos] + adj_arr[now_pos][i] <= dist[i]:
#                 dist[i] = dist[now_pos] + adj_arr[now_pos][i]
#
#
#         min_v = 987654321
#         min_idx = 0
#         for j in range(1, n + 1):
#             if not city[j] and dist[j] < min_v:
#                 min_v = dist[j]
#                 min_idx = j
#
#
#     return ' '.join(map(str, dist[1:]))
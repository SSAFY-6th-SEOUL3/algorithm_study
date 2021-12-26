# 플로이드_와샬

INF = 100001

n = int(input())  # 노드 수
m = int(input())  # 간선 수

# 현재까지 계산된 최소비용 초기화
d = []
for x in range(n):
    d.append([INF] * n)

for _ in range(m):
    st_node, end_node, val = map(int, input().split())
    # 경로 1개이상인 경우(존재하는 경우) 더 비용적은 경로로 선택
    if val < d[st_node-1][end_node-1]:
        d[st_node - 1][end_node - 1] = val
    else:
        pass
    d[st_node-1][st_node-1] = 0

# print(d)
# k = 거쳐가는 노드, i = 출발 노드, j = 도착 노드
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 출발-도착 직선거리보다 특정 노드를 거쳐가는 비용을 비교해서 더 적은 비용으로 초기화한다.
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]

# print(d)
for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print()
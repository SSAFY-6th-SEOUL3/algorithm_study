import sys
sys.stdin = open('input.txt')

n, m, r = map(int, input().split()) # n: 지역의 개수, m: 수색 범위, r: 길의 개수
items = list(map(int, input().split())) # 각 구역의 아이템 수

# 가중치, 무방향 그래프
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split()) # a, b: 길의 양 끝 지역번호, l: 길의 길이
    arr[a][b] = l
    arr[b][a] = l
print(arr)


from collections import deque
queue = deque()

distance = [0] * (n+1) # 특정 노드까지의 최단거리 예상치
pre_node = [0] * (n+1) # 특정 노드의 직전노드
complete = [False] * (n+1) # 특정 노드까지의 최단길이 찾았는지 여부

visited = [False] * (n+1)
# 떨어지는 지역의 경우의 수
def bfs(s):
    items = [5, 7, 8, 2, 3]
    result = 0
    m = 4
    queue.append(s)
    result += items[s-1]
    while queue:
        current = queue.popleft()
        # 모든 노드 중 current 와 인접한 노드
        for k in range(1, n+1):
            total = 0
            # 처음 방문한 노드이면 방문표시 후 큐에 넣는다.
            if arr[current][k] and not visited[k]:
                visited[k] = True
                queue.append(k)
                total += arr[current][k]
                print(f"{current},{k} total : {total}")
                if total <= m:
                    result += items[k-1]
                print(f"items : {result}")
        break


bfs(1)





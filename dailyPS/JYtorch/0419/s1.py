from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def check(arr):
    pos_list = []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                pos_list.append((i, j))
    for y, x in pos_list:
        q = deque()
        q.append((y, x, 0))
        visited = [[0] * 5 for _ in range(5)]
        visited[y][x] = 1
        while q:
            r, c, dist = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr < 0 or nr >= 5 or nc < 0 or nc >= 5: continue
                if arr[nr][nc] == 'X': continue
                if visited[nr][nc]: continue
                if arr[nr][nc] == 'P':
                    if dist <= 1:
                        return False
                visited[nr][nc] = 1

                q.append((nr, nc, dist + 1))
    return True


def solution(places):
    answer = []
    for place in places:
        if not check(place):
            answer.append(0)
        else:
            answer.append(1)

    return answer
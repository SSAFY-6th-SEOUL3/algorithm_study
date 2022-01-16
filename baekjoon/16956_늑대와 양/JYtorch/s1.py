import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def solution():
    global answer
    for r, c in W_pos:
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if arr[nr][nc] == 'S': return answer
            elif arr[nr][nc] == 'W' or arr[nr][nc] == 'D': continue
            elif arr[nr][nc] == '.': arr[nr][nc] = 'D'
    answer = 1
    return answer

R, C = map(int, input().split())
arr = []
W_pos = []
for i in range(R):
    m = list(input())
    for j in range(C):
        if m[j] == 'W':
            W_pos.append((i, j))
    arr.append(m)
answer = 0
solution()
if answer:
    print(answer)
    for i in arr:
        print(''.join(i))
else:
    print(answer)
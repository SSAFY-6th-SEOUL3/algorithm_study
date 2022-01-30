import sys
sys.stdin = open('input.txt')

"""
N: 문제 개수
L: 최소 기준
R: 최대 기준
X: 난이도 차이
"""
N, L, R, X = map(int, input().split())
problems = list(map(int, input().split()))
problems.sort()
cnt = 0


def dfs(selection, k):
    global cnt
    if k == N:
        if len(selection) == 0:
            return
        left = problems[selection[0]]
        right = problems[selection[-1]]
        total = 0
        for i in selection:
            total += problems[i]
        if total < L or total > R:
            return
        if right-left < X:
            return
        cnt += 1
        return
    dfs(selection[:] + [k], k+1)
    dfs(selection[:], k+1)


dfs([], 0)
print(cnt)
import sys
sys.stdin = open('input.txt')

def solution(lev, problems):
    global ans

    if lev == N:
        # 문제 개수 >= 2
        if len(problems) >= 2:
            # 문제 난이도 최대값 - 문제 난이도 최소값 >= X
            if max(problems) - min(problems) >= X:
                # L <= 문제 난이도의 합 <= R
                if L <= sum(problems) <= R:
                    ans += 1
        return

    solution(lev + 1, problems + [arr[lev]])
    solution(lev + 1, problems)

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))
used = [0] * N
ans = 0
solution(0, [])
print(ans)








import sys
sys.stdin = open('input.txt')

def solution(day, cursum):
    global ans
    if ans < cursum:
        ans = cursum

    if day >= N + 1:
        if ans < cursum:
            ans = cursum
        return

    else:
        for i in range(day + T[day], N + 1):
            if i + T[i] <= N + 1:
                solution(i, cursum + P[i])

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
ans = 0

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for j in range(1, N + 1):
    if j + T[j] <= N + 1:
        solution(j, P[j])
print(ans)



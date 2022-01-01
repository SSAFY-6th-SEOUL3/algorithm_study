import sys
sys.stdin = open('input.txt')


N = int(input())
schedules = [(0, 0)]
for i in range(N):
    schedule = tuple(map(int, input().split()))
    schedules.append(schedule)

dp = [0]*(N+1)

for i in range(N-1, -1, -1):
    if i + schedules[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(schedules[i][1] + dp[i+schedules[i][0]], dp[i+1])

print(dp)





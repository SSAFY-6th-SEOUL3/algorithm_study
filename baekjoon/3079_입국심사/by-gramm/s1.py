"""
입력값을 input()으로 받았을 때는 시간 초과가 뜸.
입력값이 많은 경우 sys.stdin을 써야 함을 알 수 있음.
"""
from sys import stdin


N, M = map(int, stdin.readline().split())
times = []

for _ in range(N):
    times.append(int(stdin.readline()))

# end의 경우, 심사시간이 가장 짧은 심사대로 모든 사람이 들어간 경우를 초기값으로 설정한다.
start, end = 1, min(times) * M

# 이분 탐색으로 모든 사람의 심사가 끝나는 최소 시간을 구한다.
while start < end:
    mid = (start + end) // 2
    # total: mid초 동안 각 심사대에서 심사를 마친 사람의 합
    total = sum([mid // time for time in times])

    if total < M:
        start = mid + 1
    elif total >= M:
        # mid가 최소 시간일 가능성도 있으므로 mid - 1이 아니라 mid를 end에 대입한다.
        end = mid

print(end)

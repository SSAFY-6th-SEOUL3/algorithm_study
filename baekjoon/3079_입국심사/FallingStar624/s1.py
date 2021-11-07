import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())  # N: 입국 심사대 수 / M: 총 인원
immigrations = []
for _ in range(N):
    immigrations.append(int(input()))
left = 0
seconds = right = max(immigrations) * M

while left <= right:
    mid = (left+right) // 2
    people = 0
    for immigration in immigrations:
        people += mid//immigration
    if people < M:
        left = mid + 1
    else:
        right = mid - 1
        seconds = min(seconds, mid)

print(seconds)
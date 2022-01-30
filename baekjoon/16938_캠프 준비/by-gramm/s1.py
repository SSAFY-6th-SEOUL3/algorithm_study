
N, L, R, X = map(int, input().split())
levels = [int(x) for x in input().split()]
levels.sort()  # levels를 미리 정렬하여, current도 자동 정렬되도록 함.

total_count = 0

# bitmask 활용
for i in range(1, 1 << N):
    current = []

    for j in range(N):
        if i & (2 ** j):
            current.append(levels[j])

    if L <= sum(current) <= R and current[-1] - current[0] >= X:
        total_count += 1

print(total_count)

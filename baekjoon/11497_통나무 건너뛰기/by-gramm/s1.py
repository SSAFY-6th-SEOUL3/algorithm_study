from sys import stdin


T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    heights = [int(x) for x in stdin.readline().split()]
    heights.sort()
    max_value = 0

    for i in range(2, N):
        max_value = max(max_value, heights[i] - heights[i - 2])

    print(max_value)

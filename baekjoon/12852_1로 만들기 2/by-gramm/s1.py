from collections import deque

N = int(input())


next = [-1] * (N + 1)
queue = deque()
queue.append(1)

# 1에서부터 N이 나올 때까지 역으로 경로를 탐색한다.
while queue:
    num = queue.popleft()

    if num == N:
        break

    for x in [num * 3, num * 2, num + 1]:
        if x <= N and next[x] == -1:
            queue.append(x)
            next[x] = num

num = N
total_path = []

while num != 1:
    total_path.append(num)
    num = next[num]

print(len(total_path))

for x in total_path:
    print(x, end=" ")

print(1)

import sys
sys.stdin = open('input.txt', 'r')


n = int(input())
numbers = [[] for _ in range(4)]
for _ in range(6):
    nums = list(map(int, input().split()))
    for idx, num in enumerate(nums):
        numbers[idx].append(num)

for num_list in numbers:
    num_list.sort()

cnt = 0


def dfs(total, now):
    global cnt, numbers
    if now == 4:
        if total == 0:
            cnt += 1
        return
    else:
        for tmp in numbers[now]:
            dfs(total+tmp, now+1)


dfs(0, 0)
print(cnt)

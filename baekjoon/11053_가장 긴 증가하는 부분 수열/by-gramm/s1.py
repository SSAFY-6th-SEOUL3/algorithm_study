N = int(input())
numbers = [int(x) for x in input().split()]


# count[i]: 0 ~ i번 인덱스 수까지 가장 긴 증가하는 부분 수열의 길이
count = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            count[i] = max(count[i], count[j] + 1)

print(max(count))

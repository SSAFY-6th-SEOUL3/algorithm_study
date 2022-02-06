from sys import stdin


K = int(stdin.readline())
numbers = []

for _ in range(K):
    num = int(stdin.readline())

    if num:  # num이 0이 아니면
        numbers.append(num)
    else:    # num이 0이면
        numbers.pop()

print(sum(numbers))

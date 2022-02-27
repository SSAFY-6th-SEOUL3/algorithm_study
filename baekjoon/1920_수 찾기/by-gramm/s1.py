from sys import stdin


N = int(stdin.readline())
numbers = [int(x) for x in stdin.readline().split()]
numbers.sort()

M = int(stdin.readline())
targets = [int(x) for x in stdin.readline().split()]

for target in targets:
    start, end = 0, N - 1
    is_found = False

    while start <= end:
        mid = (start + end) // 2

        if target < numbers[mid]:
            end = mid - 1
        elif target > numbers[mid]:
            start = mid + 1
        else:
            is_found = True
            break

    print(int(is_found))

import sys
import collections
sys.stdin = open("input.txt")
r, c, k = map(int, input().split())

arr = [[0] * 4] + [[0]+list(map(int, input().split()))for _ in range(3)]
# print(arr)

def reorg(arr):
    counter = collections.Counter(arr)
    sorted(counter.items())
    keys = counter.keys()
    sorted_arr = []
    for i in range(len(counter)):
        sorted_arr.append(keys[i])
        sorted_arr.append(counter.get(keys[i]))

    return sorted_arr

def min_time(r, c, k):
    answer = 0

    # R 연산
    if len(arr[0]) >= len(arr):
        for i in range(1, len(arr)+1):
            reorg(arr[i])

    # C연산
    else:
        pass

    if arr[r][c] == k:
        return answer


print(min_time(r, c, k))
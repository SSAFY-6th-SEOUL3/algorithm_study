from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

while True:
    n, k = map(int, input().split())
    if (n+k) == 0:
        break
    numbers = deque(map(int, input().split()))
    numbers_copy = list(numbers)
    arr = []
    tmp_num = numbers.popleft()
    while numbers:
        Q = [tmp_num]
        while True:
            try:
                next_num = numbers.popleft()
                if next_num - Q[-1] == 1:
                    Q.append(next_num)
                else:
                    arr.append(Q)
                    tmp_num = next_num
                    break
            except IndexError:
                arr.append(Q)
                break
    indices = list(map(len, arr))
    ranks = [0]*len(indices)
    i = 0
    while i < len(indices):
        jump = indices[i]
        for j in range(i+1, len(indices)):
            ranks[j] += 1
        i += jump
    tree = []

    for x, y in zip(ranks, indices):
        for _ in range(y):
            tree.append(x)

    print(tree.count(tree[numbers_copy.index(k)])-1)

from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    forward = []
    backward = deque()
    for idx, log in enumerate(logs):
        if idx%2:
            backward.appendleft(log)
        else:
            forward.append(log)
    logs = forward + list(backward)
    max_lv = abs(logs[0]-logs[-1])
    for i in range(1, N):
        tmp = abs(logs[i]-logs[i-1])
        if tmp > max_lv:
            max_lv = tmp
    print(max_lv)


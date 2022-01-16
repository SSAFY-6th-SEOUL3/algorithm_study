# gears[0]는 deque가 아니라 잘못 풀면 AttributeError 발생
# check == 0 이 방문 안했을 때다...그렇다...그러하다...
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

gears = [[0]*8]
for _ in range(4):
    gears.append(deque(list(map(int, input()))))
K = int(input())
rotation = []
for _ in range(K):
    rotation.append(tuple(map(int, input().split())))
check = [0]*5


def rotate(idx, direction):
    global gears, check
    check[idx] = 1
    target = gears[idx]
    link_right, link_left = target[2], target[6]

    if direction == 1:
        tmp = target.pop()
        target.appendleft(tmp)
    else:
        tmp = target.popleft()
        target.append(tmp)

    if idx > 1:
        if check[idx-1] == 0 and (link_left + gears[idx-1][2]) % 2 == 1:
            rotate(idx-1, direction*(-1))
    if idx < 4:
        if check[idx+1] == 0 and (link_right + gears[idx+1][6]) % 2 == 1:
            rotate(idx+1, direction*(-1))


for opr in rotation:
    check = [0]*5
    wheel, rot_dir = opr
    rotate(wheel, rot_dir)

score = 0
for i in range(1, 5):
    if gears[i][0]:
        score += 2**(i-1)

print(score)


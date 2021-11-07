# tc1 만..

import sys
sys.stdin = open('input.txt')

def solution(N, M, t):
    member = [x for x in range(M)]
    sec = 0
    turn = 0
    while member:
        for i in range(N):
            member.pop(0)
            if len(member) == 1:
                turn += 1
                if (turn+1) * t[0] < (turn) * t[1]:
                    return ((turn+1) * t[0])
        turn += 1

    sec += (turn-1) * t[1]
    return sec

N, M = map(int, input().split())
t = []
for i in range(N):
    t.append(int(input()))
t.sort()

print(solution(N, M, t))




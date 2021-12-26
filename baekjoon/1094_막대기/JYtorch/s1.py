import sys
sys.stdin = open('input.txt')

def solution():
    stick_list = [64]

    while sum(stick_list) != X:
        stick = stick_list.pop(0)
        if stick // 2 + sum(stick_list) >= X:
            stick_list.append(stick // 2)
        else:
            stick_list.append(stick // 2)
            stick_list.append(stick // 2)
        stick_list.sort()
    return len(stick_list)

X = int(input())
print(solution())

import sys
sys.stdin = open("input.txt")

gears = [list(map(int, input())) for _ in range(4)]
print(gears)


def clockwise(gear):
    for i in range(8):
        gear[i] = gear[(i+1) % 8]

    return gear


def counter_clockwise(gear):
    for i in range(8):
        gear[i] = gear[(i-1) % 8]

    return gear


K = int(input())

for i in range(K):
    n, m = map(int, input().split())  # n : 회전시킨 톱니바퀴의 번호, m : 방향 1 시계 -1 반시계

    # n 번 톱니바퀴
    if n == 1:
        if m == 1:
            if gears[0][2] != gears[1][6]:
                gears[0] = clockwise(gears[0])
                gears[1] = counter_clockwise(gears[1])

                if gears[1][6] != gears[2][2]:
                    gears[2] = clockwise(gears[2])
                else:
                    gears[2] = counter_clockwise(gears[2])

                    if gears[2][6] != gears[3][2]:
                        gears[3] = counter_clockwise(gears[2])
                    else:
                        gears[3] = clockwise(gears[2])

        else:
            pass

    elif n == 2:
        pass

    elif n == 3:
        pass

    else:
        pass

print(gears)
import sys
sys.stdin = open('input.txt')

def solution():
    global ans
    # K번 회전

    for number, direction in rotation_list:

        # 톱니바퀴 회전 판단(queue 사용)
        rotate_possible = [0] * 4
        used = [0] * 4
        q = [(number - 1, direction)]
        rotate_possible[number - 1] = direction
        used[number - 1] = 1
        while q:
            num, d = q.pop()
            for i in [1, -1]:
                if 0 <= num + i < 4:
                    if used[num + i]: continue
                    if i == 1:
                        if arr[num][2] != arr[num + i][6]:
                            rotate_possible[num] = d
                            rotate_possible[num + i] = d * -1
                            # used[num] = 1
                            used[num + i] = 1
                            q.append((num + i, d * -1))

                    elif i == -1:
                        if arr[num][6] != arr[num + i][2]:
                            rotate_possible[num] = d
                            rotate_possible[num + i] = d * -1
                            # used[num] = 1
                            used[num + i] = 1
                            q.append((num + i, d * -1))

        for n, rotataion_direction in enumerate(rotate_possible):

            # 시계방향으로 회전
            if rotataion_direction == 1:
                tmp = arr[n].pop()
                arr[n].insert(0, tmp)

            # 반시계방향으로 회전
            elif rotataion_direction == -1:
                tmp = arr[n].pop(0)
                arr[n].append(tmp)

    for i in range(4):
        if i == 0 and arr[i][0]: ans += 1
        if i == 1 and arr[i][0]: ans += 2
        if i == 2 and arr[i][0]: ans += 4
        if i == 3 and arr[i][0]: ans += 8


arr = [list(map(int, input())) for _ in range(4)]
K = int(input())
rotation_list = [list(map(int, input().split())) for _ in range(K)]
ans = 0
solution()
print(ans)




# def findRotatingGear(target, direction):  # 회전 시킬 톱니바퀴를 찾는 함수
#     global gears
#     res = [0] * 4
#
#     res[target] = direction
#
#     # target을 기준으로 왼쪽 검사
#     for i in range(target - 1, -1, -1):
#         if gears[i][2] == gears[i + 1][6]:
#             break
#
#         res[i] = res[i + 1] * -1
#
#     # target을 기준으로 오른쪽 검사
#     for i in range(target + 1, 4):
#         if gears[i][6] == gears[i - 1][2]:
#             break
#
#         res[i] = res[i - 1] * -1
#
#     return res
#
#
# def rotate(res):  # 톱니바퀴를 회전 시키는 함수
#     global gears
#
#     for i in range(4):
#         if res[i] == 0:  # 해당 톱니바퀴는 회전시키지 않는다.
#             continue
#
#         elif res[i] == 1:  # 해당 톱니바퀴는 시계 방향으로 회전시킨다.
#             gears[i] = [gears[i][7]] + gears[i][0:7]
#
#         else:  # 해당 톱니바퀴는 시계 반대 방향으로 회전시킨다.
#             gears[i] = gears[i][1:8] + [gears[i][0]]
#
#
# if __name__ == "__main__":
#     gears = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(4)]
#
#     k = int(sys.stdin.readline().strip())
#
#     rotatingInfo = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]
#
#     for g, d in rotatingInfo:
#         res = findRotatingGear(g - 1, d)
#         print(res)
#         rotate(res)
#         for i in gears:
#             print(i)
#         print('---------------')
#     score = gears[0][0] + gears[1][0] * 2 + gears[2][0] * 4 + gears[3][0] * 8
#
#     print(score)

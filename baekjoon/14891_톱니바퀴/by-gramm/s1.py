def rotate(num, direction):
    global wheels, visited

    left, right = wheels[num][6], wheels[num][2]
    visited[num] = True

    if direction == 1:  # 시계 방향
        wheels[num] = wheels[num][7] + wheels[num][:7]
    else:  # 반시계 방향
        wheels[num] = wheels[num][1:] + wheels[num][0]

    # 왼쪽 탐색
    if num - 1 >= 1 and not visited[num - 1] and left != wheels[num - 1][2]:
        rotate(num - 1, -direction)
    # 오른쪽 탐색
    if num + 1 <= 4 and not visited[num + 1] and right != wheels[num + 1][6]:
        rotate(num + 1, -direction)


wheels = ['']  # 1번 인덱스부터 시작하기 위해 빈 문자열을 넣어둠.

for _ in range(4):
    wheels.append(input())

K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())
    visited = [False] * 5
    rotate(num, direction)

result = 0

for i in range(1, 5):
    result += int(wheels[i][0]) * (2 ** (i - 1))

print(result)

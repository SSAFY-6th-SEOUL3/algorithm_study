from sys import stdin


N, X = map(int, stdin.readline().split())
visits = [int(x) for x in stdin.readline().split()]

# 1일차부터 X일차까지의 합을 current, max_count에 저장한다.
current = sum(visits[:X])
max_count = current
max_count_days = 1

# 시작 일차를 하루씩 뒤로 옮기며 max_count 및 max_count_days의 값을 업데이트한다.
for i in range(X, N):
    current = current - visits[i - X] + visits[i]

    if current > max_count:   # i일차까지의 방문자 수가 max_count보다 큰 경우
        max_count = current
        max_count_days = 1
    elif current == max_count:  # i일차까지의 방문자 수가 max_count와 같은 경우
        max_count_days += 1

if max_count:
    print(max_count)
    print(max_count_days)
else:
    print('SAD')

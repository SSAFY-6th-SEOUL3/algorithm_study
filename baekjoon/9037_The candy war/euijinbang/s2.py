import sys
sys.stdin = open("input.txt")


# 짝수 체크
def check(n, candy_state):
    for i in range(n):
        if candy_state[i] % 2:
            candy_state[i] += 1

    return len(set(candy_state)) == 1


# 캔디 나누기
def teacher(n, candy_state):
    tmp_candy_state = [0 for _ in range(n)]

    for i in range(n):
        if candy_state[i] % 2:
            candy_state[i] += 1

        candy_state[i] //= 2
        tmp_candy_state[(i+1) % n] = candy_state[i]

    for i in range(n):
        candy_state[i] += tmp_candy_state[i]

    return candy_state


def candy_time():
    n, candy_state = int(input()), list(map(int, sys.stdin.readline().split()))
    count = 0

    # 모든 아이들이 가진 캔디 수가 같다면 0을 반환
    while not check(n, candy_state):
        teacher(n, candy_state)
        count += 1

    print(count)

for tc in range(int(input())):
    candy_time()


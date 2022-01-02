import collections
import sys

t = int(sys.stdin.readline())

def candy_time(num, candy_state):
    count = 0

    # 모든 아이들이 가진 캔디 수가 같을 때 까지 나눠주기 반복
    while True:
        # 캔디 보충
        for i in range(num):
            if candy_state[i] % 2:
                candy_state[i] += 1

        # 모든 아이들이 가진 캔디 수가 같다면 0을 반환
        if len(collections.Counter(candy_state)) == 1:
            break

        new_candy_state = [0] * num
        for i in range(num):
            new_candy_state[i] = candy_state[i] - (candy_state[i]//2) + (candy_state[(i-1) % num]//2)

        candy_state = new_candy_state

        count += 1

    return count

for tc in range(t):
    num = int(sys.stdin.readline())
    candy_state = list(map(int, sys.stdin.readline().split()))
    print(candy_time(num, candy_state))




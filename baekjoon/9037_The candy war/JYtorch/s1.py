import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    divided_list = [0] * N

    cnt = 0
    while True:
        # 사탕 개수가 홀수인 아이한테는 하나씩 더 나눠주기
        for i in range(N):
            if C[i] % 2: C[i] += 1

        # 사탕 개수가 모두 동일해지면 순환 종료
        if C.count(C[0]) == len(C):
            break

        # 사탕 절반 나누기
        for i in range(N):
            divided_list[i] = C[i] // 2
            C[i] //= 2

        # 옆사람한테 나눈 사탕 전달해주기
        for i in range(N):
            idx = (i + 1) % N
            C[idx] += divided_list[i]

        cnt += 1
    print(cnt)



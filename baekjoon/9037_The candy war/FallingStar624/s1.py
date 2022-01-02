import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())  # 인원
    C = list(map(int, sys.stdin.readline().split()))  #처음 사탕 분포
    cnt = 0
    while True:
        # 나누기 전 보충
        half = []
        for i in range(N):
            if C[i] % 2:
                C[i] += 1
            half.append(C[i] // 2)
        # 종료 조건
        if len(set(C)) == 1:
            break
        # 오른쪽 사람에게 전달
        for i in range(N):
            C[i] = half[i] + half[(i-1) % N]
        # 짝수 보충
        for i in range(N):
            if C[i] % 2:
                C[i] += 1
        cnt += 1

    print(cnt)



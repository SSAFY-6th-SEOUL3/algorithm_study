import sys
sys.stdin = open('input.txt')

N = int(input())

cnt = [[0, []] for _ in range(N+1)]  # [최솟값, 경로 리스트]
cnt[1][0] = 0  # 최솟값
cnt[1][1] = [1]  # 경로를 담을 리스트

for i in range(2, N + 1):

    # f(x-1) + 1
    cnt[i][0] = cnt[i-1][0] + 1
    cnt[i][1] = cnt[i-1][1] + [i]

    # f(x//3) + 1
    if i % 3 == 0 and cnt[i//3][0] + 1 < cnt[i][0]:
        cnt[i][0] = cnt[i//3][0] + 1
        cnt[i][1] = cnt[i//3][1] + [i]

    # f(x//2) + 1
    if i % 2 == 0 and cnt[i//2][0] + 1 < cnt[i][0]:
        cnt[i][0] = cnt[i//2][0] + 1
        cnt[i][1] = cnt[i//2][1] + [i]

print(cnt[N][0])
for i in cnt[N][1][::-1]:  # 뒤집은 뒤 출력
    print(i, end=' ')

print(cnt)
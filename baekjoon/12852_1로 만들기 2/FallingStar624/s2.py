import sys
sys.stdin = open('input.txt')

N = int(input())
min_cnt = [0]*(N+1)
route = [0]*(N+1)


def find_n():
    global N, min_cnt, route
    for i in range(2, N+1):
        """
        바로 위에 수는 +1 해주면 바로 만들 수 있으므로 
        i는 기본적 i-1보다 한 번 더 연산을 한다고 세팅
        """
        min_cnt[i] = min_cnt[i-1]+1
        route[i] = i-1
        """
        i가 2나 3으로 나누어지고 i//2 나 i//3이 min_cnt[i]보다
        2 이상 차이나게 작으면 갱신
        ex)
        N == 4:
         0  1  2  3  4
        [0, 0, 0, 0, 0] => [0, 0, 1, 2, 3]
        [0, 0, 1, 2, 3] => [0, 0, 1, 1, 2]
        """
        if i % 2 == 0 and min_cnt[i//2]+1 < min_cnt[i]:
            min_cnt[i] = min_cnt[i//2] + 1
            route[i] = i // 2

        if i % 3 == 0 and min_cnt[i//3]+1 < min_cnt[i]:
            min_cnt[i] = min_cnt[i//3] + 1
            route[i] = i // 3


find_n()
print(min_cnt[N])
while N != 0:
    print(N, end=' ')
    N = route[N]
import sys
sys.stdin = open('input.txt')

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

# 주사위 한번 굴렸을 때, 번호 위치 재배치하기
def find(status, direction):
    n1, n2, n3, n4, n5, n6 = status
    if direction == 1:
        status = [n6, n2, n5, n4, n1, n3]

    elif direction == 2:
        status = [n5, n2, n6, n4, n3, n1]

    elif direction == 3:
        status = [n4, n1, n2, n3, n5, n6]

    elif direction == 4:
        status = [n2, n3, n4, n1, n5, n6]

    return status

# N: 세로길이, M: 가로길이, r, c: 행과 열, K: 명령 횟수
N, M, r, c, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

# now_status: 현재 주사위 숫자의 배열
# 0번 인덱스: 보드 바닥에 닿아 있는 부분
# 1번 인덱스: 남쪽으로 1회 굴렸을 때 바닥에 닿는 부분
# 2번 인덱스: 남쪽으로 2회 굴렸을 때 바닥에 닿는 부분 (0번 인덱스의 정반대편)
# 3번 인덱스: 남쪽으로 3회 굴렸을 때 바닥에 닿는 부분
# 4번 인덱스: 서쪽으로 1회 굴렸을 때 바닥에 닿는 부분
# 5번 인덱스: 동쪽으로 1회 굴렸을 때 바닥에 닿는 부분
now_status = [0] * 6

i = 0
while i < K:
    nr = r + dr[orders[i]]
    nc = c + dc[orders[i]]
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
        i += 1
        continue

    now_status = find(now_status, orders[i])

    # 보드 바닥에 쓰인 숫자가 0이면 주사위 숫자를 보드에 새기기
    if mat[nr][nc] == 0:
        mat[nr][nc] = now_status[0]

    # 보드 바닥에 쓰인 숫자가 0이 아니면, 주사위 바닥에 보드 숫자 새기기
    else:
        now_status[0] = mat[nr][nc]
        mat[nr][nc] = 0
    r, c = nr, nc

    # 상단 부분 숫자 출력
    print(now_status[2])
    i += 1
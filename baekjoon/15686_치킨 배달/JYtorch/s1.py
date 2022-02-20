import sys
sys.stdin = open('input.txt')

#
def solution(k, start):
    global ans
    # M개의 치킨집을 고르면, 각각의 집에서 => 치킨집 최소 거리를 계산한다.
    if k == M:
        c_pos_list = []     # M개의 치킨집 좌표 리스트
        for j in range(len(chicken_pos)):
            if used[j]:
                c_pos_list.append(chicken_pos[j])

        total = 0   # 치킨 거리의 최솟값
        for hr, hc in house_pos:
            min_dist = 987654321
            for cr, cc in c_pos_list:
                dist = abs(hr - cr) + abs(hc - cc)

                min_dist = min(min_dist, dist)
            total += min_dist
        ans = min(total, ans)
        return

    # 치킨집 조합 계산
    for i in range(start, len(chicken_pos)):
        if used[i]: continue
        used[i] = 1
        solution(k + 1, i + 1)
        used[i] = 0


N, M = map(int, input().split())
house_pos = []      # 가정집 좌표
chicken_pos = []    # 치킨집 좌표
city_info = []      # 마을 전체 정보
for i in range(N):
    info = list(map(int, input().split()))

    for j in range(N):
        if info[j] == 1:
            house_pos.append((i, j))
        elif info[j] == 2:
            chicken_pos.append((i, j))

    city_info.append(info)

used = [0] * len(chicken_pos)

ans = 987654321

solution(0, 0)
print(ans)
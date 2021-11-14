# runtime error?

# 1. Prefix Sum 알고리즘을 통해 모든 구간 합을 구한다.
#
# 2. 구간 합들의 나머지를 나머지 배열에 넣어둔다.(해당하는 인덱스가 나머지를 의미하도록)
#
# 3. 조합론을 생각하며 를 해준다.(이 의미는 해당하는 같은 나머지 2개를 뽑아서 조합한다는 의미이다.)

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] + arr
for i in range(1, N+1):
    prefix_sum[i] = (prefix_sum[i-1] + prefix_sum[i])

prefix_sum_mod = prefix_sum
for i in range(1, N+1):
    prefix_sum_mod[i] = prefix_sum[i] % M

#print(prefix_sum_mod) # [0, 1, 0, 0, 1, 0]

cnt = [0 for x in range(100000)]
for i in range(N+1):
    cnt[prefix_sum[i]] += 1

ans = 0
for i in range(N):
    ans += (cnt[i] * (cnt[i] - 1)) // 2

print(ans)
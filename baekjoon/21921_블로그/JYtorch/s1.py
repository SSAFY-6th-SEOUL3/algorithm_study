import sys
sys.stdin = open('input.txt')

N, X = map(int, input().split())
visit_info = list(map(int, input().split()))

visit_set = {}
total = 0
start = 0
visit_sum = 0
for i in range(N):
    visit_sum += visit_info[i]
    if i >= X - 1:
        if total <= visit_sum:
            total = visit_sum
            if visit_set.get(visit_sum):
                visit_set[visit_sum] += 1
            else:
                visit_set[visit_sum] = 1
        visit_sum -= visit_info[start]
        start += 1

if total == 0:
    print('SAD')
else:
    print(total)
    print(visit_set[total])

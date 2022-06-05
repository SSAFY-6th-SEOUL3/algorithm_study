"""
감소하는 수는 감소하는 수로 나눌 수 있다.
ex. 976421이 감소하는 수 => 97, 6, 421은 모두 감소하는 수다.

n자리수의 감소하는 수의 개수 = 숫자 10개 중 n개를 고르는 조합의 개수
"""
from itertools import combinations

# N번째 감소하는 수의 자리수를 구한다.
N = int(input())
digits = [x for x in range(10)]

# 1자리 ~ 10자리의 감소하는 수를 순회하며 N번째 감소하는 수를 탐색한다.
for i in range(1, 11):
    desc_numbers = []
    num_list = combinations(digits, i)

    for x in num_list:
        desc_numbers.append("".join([str(x) for x in sorted(x, reverse=True)]))

    desc_numbers = [int(x) for x in desc_numbers]
    desc_numbers.sort()
    num_count = len(desc_numbers)

    if num_count <= N:
        N -= num_count
    else:
        print(desc_numbers[N])
        N = -1
        break

if N > -1:
    print(-1)

import math
from itertools import permutations

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:  # 2부터 시작하는 정수들로 나누어 떨어진다면 소수가 아니다
            return False
    else:
        return True  # 2부터 시작하는 정수들 모두 나누어 떨어지지 않으면 소수이다

def countIsPrime(numbers):
    cnt = 0
    visited = [0, 1]

    for i in range(1, 8):
        nums_for_num = list(permutations(numbers, i))
        perm_nums = []

        if nums_for_num:
            for tuple_num in nums_for_num:
                tt = ''
                for tn in tuple_num:
                    tt += tn
                perm_nums.append(int(tt))
            #print(perm_nums) #[1, 7] [17, 71] // [0, 1, 1] [1, 1, 10, 11, 10, 11] [11, 11, 101, 110, 101, 110]

            for perm_num in perm_nums:
                if isPrime(perm_num) and perm_num not in visited:
                    visited.append(perm_num)
                    cnt += 1

    return cnt








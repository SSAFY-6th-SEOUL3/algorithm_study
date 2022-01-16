n = 110011
k = 10

def check_prime(num):
    if num == 1: return False
    N = int(num ** (1 / 2))
    for i in range(2, N + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    cnt = 0
    my_number = ''
    while n > 0:
        num = str(n % k)
        if num != '0':
            my_number = num + my_number
        else:
            if my_number:
                if check_prime(int(my_number)): cnt += 1
                my_number = ''
        n //= k

    if my_number:
        if check_prime(int(my_number)): cnt += 1

    return cnt

print(solution(n, k))


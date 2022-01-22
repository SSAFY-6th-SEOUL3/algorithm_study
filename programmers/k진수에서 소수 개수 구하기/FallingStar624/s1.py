# TC1 왜 시간초과?...
def prime_check(number):
    number = int(number)
    if number == 1:
        return 0
    for i in range(2, int(number**(1/2))):
        if number % i == 0:
            return 0
    return 1


def solution(n, k):
    result = ""
    while n > 0:
        n, r = divmod(n, k)
        result = str(r) + result
    answer = result.split('0')
    cnt = 0
    for tmp in answer:
        if tmp and prime_check(tmp):
            cnt += 1
    return cnt


print(solution(437674, 3))
print(solution(110011, 10))

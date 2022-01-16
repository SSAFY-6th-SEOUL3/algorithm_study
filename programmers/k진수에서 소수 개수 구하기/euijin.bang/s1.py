# 테스트1 시간초과

def is_prime_num(n):
    """
    N-1 ~ 2 까지의 수 중, 어떠한 수로도 나누어지지 않는 수
    """
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def solution(n, k):
    tmp = ''

    # k진수 변환
    while n:
        tmp += str(n % k)
        n = n // k

    string = tmp + "0"

    answer = 0
    tmp2 = ''
    for s in string:
        if s != "0":
            tmp2 += s
        if s == "0":
            if tmp2 != "" and tmp2 != "1":
                tmp2 = tmp2[::-1]
                answer += is_prime_num(int(tmp2))
            tmp2 = ""

    return answer

print(solution(110011, 10))
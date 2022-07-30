def n_to_kth(n, k):
    """
    10진수 수 n을 k진수 수로 바꾼다.
    """
    result = ""

    while n > 0:
        n, rest = divmod(n, k)
        result = str(rest) + result

    return result


def is_prime(n):
    """
    주어진 숫자 n이 소수면 True, 아니면 False를 반환한다.
    """
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    kth_number = n_to_kth(n, k)
    numbers = kth_number.split('0')
    count = 0

    for num in numbers:
        if num and is_prime(int(num)):
            count += 1

    return count

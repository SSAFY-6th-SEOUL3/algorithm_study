from itertools import permutations


def is_prime(num):
    """
    주어진 수가 소수이면 True, 소수가 아니면 False를 리턴한다.
    """
    if num == 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    count = 0
    num_set = set()

    # 주어진 숫자들을 조합하여 만들 수 있는 모든 수를 num_set에 저장한다.
    for i in range(1, len(numbers) + 1):
        for number in list(permutations(list(numbers), i)):
            num_set.add(int(''.join(number)))

    # num_set에 있는 수 중 소수의 개수를 구한다.
    for num in num_set:
        if is_prime(num):
            count += 1

    return count

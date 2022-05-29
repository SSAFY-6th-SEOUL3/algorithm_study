N = int(input())
max_value = int(10 ** (N / 2))  # N자리 수의 최대 루트값

# max_value 이하의 소수를 모두 구한다.
primes = [2, 3, 5, 7]

for i in range(11, max_value + 1, 2):
    is_prime = True

    for prime in primes:
        if prime * prime > i:
            break
        if i % prime == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(i)


def is_prime(num):
    """
    num이 소수면 True, 소수가 아니면 False를 리턴한다.
    """
    max_value = num ** 0.5

    for prime in primes:
        if prime > max_value:
            return True
        if num % prime == 0:
            return False

    return True


def find_ndigit_prime(number, length):
    """
    number: 현재 탐색중인 수
    length: 현재 탐색중인 수의 자리수
    """
    if length == N:
        print(number)
        return

    for i in range(1, 10, 2):
        new_number = 10 * number + i
        if is_prime(new_number):
            find_ndigit_prime(new_number, length + 1)


for x in [2, 3, 5, 7]:
    find_ndigit_prime(x, 1)

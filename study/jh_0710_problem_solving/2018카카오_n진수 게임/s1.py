num_to_char = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def to_nth(num, n):
    """
    num을 n진수로 표현한 문자열을 구한다.
    """
    result = ""

    if num == 0:
        return '0'

    while num > 0:
        num, rest = divmod(num, n)

        if rest >= 10:
            rest = num_to_char[rest]
        result = str(rest) + result

    return result


def solution(n, t, m, p):
    result = ""

    for i in range(25000):
        result += to_nth(i, n)

    answer = ""
    p -= 1

    for _ in range(t):
        answer += result[p]
        p += m

    return answer

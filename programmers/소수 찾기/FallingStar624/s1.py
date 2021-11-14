from itertools import permutations


def solution(numbers):
    n = len(numbers)
    number_list = list(numbers)
    combinations = []
    for i in range(1, n+1):
        tmp = list(permutations(number_list, i))
        combinations.extend(tmp)
    combinations = list(map(lambda x: ''.join(x), combinations))
    combinations = list(map(lambda x: x.lstrip('0'), combinations))
    combinations = list(set(combinations))
    if '' in combinations:
        combinations.remove('')
    answer = 0
    for number in combinations:
        num = int(number)
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                answer += 1
    return answer


print(solution("011"))
print(solution('17'))
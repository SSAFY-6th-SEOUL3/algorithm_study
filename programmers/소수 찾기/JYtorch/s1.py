from itertools import permutations

def solution(numbers):
    answer = 0

    # 주어진 문자열로 조합 가능한 모든 숫자 만들기
    N = len(numbers)

    tmp = []
    for i in range(len(numbers)):
        numbers_permutations = permutations(numbers, i + 1)
        tmp += list(map(''.join, numbers_permutations))

    tmp = list(set(map(int, tmp)))

    # 소수인지 판단하는 함수 만들기 2, 3, 5, 7, 11, 13, 17, 19, 23
    for n in tmp:

        if int(n) == 0 or int(n) == 1:
            continue

        num = int(n)
        cnt = 0
        for j in range(2, num):
            if num % j == 0:
                cnt += 1
                break
        if cnt == 0:
            answer += 1

    return answer

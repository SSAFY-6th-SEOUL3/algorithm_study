from sys import stdin


N = int(stdin.readline())
numbers = [0] + [int(x) for x in stdin.readline().split()]

# odd_palindromes[n]: n번째 수를 중심으로 길이가 홀수인 가장 긴 회문의 시작 인덱스
odd_palindromes = [0]

for i in range(1, N + 1):
    left, right = i, i

    while True:
        if left < 1 or right > N or numbers[left] != numbers[right]:
            odd_palindromes.append(left + 1)
            break

        left, right = left - 1, right + 1

# even_palindromes[n]: n번째, n+1번째 수를 중심으로 길이가 짝수인 가장 긴 회문의 시작 인덱스
even_palindromes = [0]

for i in range(1, N):
    left, right = i, i + 1

    # n번째 수와 n+1번째 수가 다른 경우 => 길이가 짝수인 회문이 존재하지 않음
    if numbers[left] != numbers[right]:
        even_palindromes.append(12345)
    else:
        while True:
            if left < 1 or right > N or numbers[left] != numbers[right]:
                even_palindromes.append(left + 1)
                break

            left, right = left - 1, right + 1

M = int(stdin.readline())

for _ in range(M):
    S, E = map(int, stdin.readline().split())
    mid, rest = divmod(S + E, 2)

    # 1) 탐색하는 문자열의 길이가 홀수인 경우
    if not rest:
        print(int(odd_palindromes[mid] <= S))
    # 2) 탐색하는 문자열의 길이가 짝수인 경우
    else:
        print(int(even_palindromes[mid] <= S))

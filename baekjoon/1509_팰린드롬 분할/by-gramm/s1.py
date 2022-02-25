S = input()

s_length = len(S)
"""
palindrome_sets[i] : S[i]에서 시작하는 팰린드롬의 마지막 인덱스의 리스트
distances[i] : S의 팰린드롬 분할에서 S[i]로 끝나는 분할이 n번째 분할일 때, n의 최소값
               ex. S가 "ABACABA"인 경우, distances는 [1, 2, 1, 2, 3, 2, 1]
"""
palindrome_sets = [[x] for x in range(s_length)]
distances = [x for x in range(1, s_length + 1)]

# 1. 길이가 홀수인 팰린드롬을 모두 탐색한다.
for i in range(s_length):
    left, right = i - 1, i + 1

    while 0 <= left < s_length and 0 <= right < s_length:
        if S[left] != S[right]:
            break

        palindrome_sets[left].append(right)
        left, right = left - 1, right + 1

# 2. 길이가 짝수인 팰린드롬을 모두 탐색한다.
for i in range(s_length - 1):
    left, right = i, i + 1

    while 0 <= left < s_length and 0 <= right < s_length:
        if S[left] != S[right]:
            break

        palindrome_sets[left].append(right)
        left, right = left - 1, right + 1

# 3. distances에 각 인덱스까지의 팰린드롬 분할의 최소값을 저장한다.
for x in palindrome_sets[0]:
    distances[x] = 1

for i in range(1, s_length):
    for x in palindrome_sets[i]:
        # i에서 x로 갈 때의 거리가 현재 저장된 x로 가는 최단 거리보다 짧다면
        if distances[i - 1] + 1 < distances[x]:
            distances[x] = distances[i - 1] + 1

print(distances[-1])


def solution(s):
    min_length = s_len = len(s)                  # 압축한 문자열 중 가장 짧은 것의 길이

    for i in range(1, s_len // 2 + 1):           # 문자열을 i개 단위로 자르는 경우를 탐색한다.
        length = s_len                           # 압축한 문자열의 길이 (초기값 : s의 길이)
        before = s[:i]                           # before: 현재 문자열 앞의 문자열
        count = 1                                # 현재 문자열이 겹친 개수

        for j in range(i, s_len, i):             # i 단위로 자른 문자열 중 2번째 문자열부터 앞 문자열과 같은지 비교한다.
            current = s[j:j + i]                 # current: 현재 문자열

            if before == current:                # 1) 앞 문자열과 같은 경우
                count += 1                       # count에 1을 더한다.
                if count in (2, 10, 100, 1000):  # 1-A) count가 2거나, 자리수가 하나 늘어난 경우
                    length -= (i - 1)            # length에서 i - 1만큼 뺀다. (숫자의 길이가 1 추가되므로)
                else:                            # 1-B) 그 외의 경우
                    length -= i                  # length에서 i만큼 뺀다.
            else:                                # 2) 앞 문자열과 다른 경우
                count = 1                        # 현재 문자열이 겹친 개수를 1로 초기화한다.

            before = current                     # 다음 문자열을 탐색하기 전, 현재 문자열을 이전 문자열로 설정한다.

        min_length = min(min_length, length)     # min_length에 현재 탐색 중인 경우를 업데이트한다.

    return min_length


print(solution("aabbcddd"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

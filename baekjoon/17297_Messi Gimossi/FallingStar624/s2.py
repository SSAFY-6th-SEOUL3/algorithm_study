# s1 => maximum recursion error
import sys
sys.stdin = open('input.txt')


def solution(idx, M):
    global res, dp
    """
    :param idx: 현재 문자열에서 찾으려는 index
    :param M: 문제에서 주어진 M
    :param dp: dp를 위한 arr
    :return: M번째 글자 출력
    """
    if idx <= 1:
        return "Messi Gimossi"[M - 1]
    if M > dp[idx - 1] + 1:
        res = solution(idx - 2, M - dp[idx - 1] - 1)
    elif M < dp[idx - 1]:
        res = solution(idx - 1, M)
    else:
        return " "
    return res


M = int(input())
dp = [5, 13]
# messi(M)의 문자열 길이 구하기
while dp[-1] < M:
    dp.append(dp[-2] + 1 + dp[-1])  # (n-1) + 공백 + (n-2)
res = solution(len(dp) - 1, M)
print("Messi Messi Gimossi" if res == " " else res)
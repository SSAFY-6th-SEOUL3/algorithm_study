dic = {'A': 0,
           'B': 1,
           'C': 2,
           'D': 3,
           'E': 4,
           'F': 5,
           'G': 6,
           'H': 7,
           'I': 8,
           'J': 9,
           'K': 10,
           'L': 11,
           'M': 12,
           'N': 13,
           'O': 12,
           'P': 11,
           'Q': 10,
           'R': 9,
           'S': 8,
           'T': 7,
           'U': 6,
           'V': 5,
           'W': 4,
           'X': 3,
           'Y': 2,
           'Z': 1
          }


def solution(name):
    answer = 0
    min_move = len(name) - 1

    for i in range(len(name)):
        answer += dic[name[i]]
        cnt = i + 1
        while cnt < len(name) and name[cnt] == 'A':
            cnt += 1

        min_move = min(min_move, i * 2 + len(name) - cnt)
    answer += min_move
    return answer


###############################################################
# 같은 로직인데 테스트 11에서 시간 초과...
#
# def solution(name):
#     N = len(name)
#     answer = 0
#     min_move = N-1
#     check = False
#
#     for i in range(N):
#         answer += dic[name[i]]
#         if name[i] == 'A':
#             check = True
#         if check and name[i] != 'A':
#             min_move = min(min_move, cnt + N - i)
#             check = False
#         if name[i] != 'A':
#             cnt = i * 2
#     answer += min_move
#
#     return answer



import sys
sys.stdin = open('input.txt')


def solution():
    for i in range(100, 0, -1):
        for j in range(101 - i):
            for r in range(100):
                word = board[r][j:j + i]
                if word == word[::-1]:
                    return len(word)
                tmp = ""
                for c in range(j, j + i):
                    tmp += board[c][r]
                if tmp == tmp[::-1]:
                    return len(tmp)


for _ in range(10):
    tc = int(input())
    board = [input() for _ in range(100)]
    print('#{} {}'.format(tc, solution()))

import sys
sys.stdin = open('input.txt', 'r')

M = int(input())


def messi(num):
    if num == 1:
        return "Messi"
    elif num == 2:
        return "Messi Gimossi"
    else:
        return messi(num-1) + ' ' + messi(num-2)


print(messi(M)[M-1])
# 재귀 => 시간초과
import sys
sys.stdin = open('input.txt')

N = int(input())
minimum = N
result = []


def solution(number, process):
    global minimum, result
    if len(process) > minimum:
        return
    if number == 1:
        process.append(1)
        if minimum > len(process):
            minimum = len(process)
            result = process
    if number % 3 == 0 and number not in process:
        solution(number//3, process+[number])
    if number % 2 == 0 and number not in process:
        solution(number//2, process+[number])
    if number > 1 and number-1 not in process:
        solution(number-1, process+[number])


solution(N, [])

print(minimum-1)
print(' '.join(map(str, result)))
import sys
sys.stdin = open('input.txt')


def calc(o, n1, n2):
    if o == '+':
        return n1 + n2
    if o == '-':
        return n1 - n2
    if o == '*':
        return n1 * n2
    if o == '/':
        if n1 < 0:
            return (n1 * -1 // n2) * -1
        else:
            return n1 // n2


def perm(k, curv):
    global max_value, min_value
    if k == len(operators):
        if max_value < curv:
            max_value = curv
        if min_value > curv:
            min_value = curv
        return
    else:
        for i in range(k, len(operators)):
            operators[i], operators[k] = operators[k], operators[i]
            perm(k+1, calc(operators[k], curv, numbers[k+1]))
            operators[i], operators[k] = operators[k], operators[i]


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operators = []
used = []

max_value = -1000000000
min_value = 1000000000
operators_count = list(map(int, sys.stdin.readline().split()))

for idx, operators_val in enumerate(operators_count):
    if idx == 0:
        for i in range(operators_val):
            operators.append('+')
    if idx == 1:
        for i in range(operators_val):
            operators.append('-')
    if idx == 2:
        for i in range(operators_val):
            operators.append('*')
    if idx == 3:
        for i in range(operators_val):
            operators.append('/')
P = list(range(len(operators)))
perm(0, numbers[0])
print(max_value)
print(min_value)








import sys
sys.stdin = open('input.txt')

value_set = {}
def get_value(n):
    if n in value_set:
        return value_set[n]
    else:
        value_set[n] = 1 if n < 4 else get_value(n - 3) + get_value(n - 2)
        return value_set[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(get_value(N))

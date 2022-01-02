
def make_even():
    global candy

    for i, c in enumerate(candy):
        if c % 2 == 1:
            candy[i] += 1


def circulate():
    global candy, N

    half_candy = [c // 2 for c in candy]

    for i in range(1, N):
        candy[i] -= half_candy[i]
        candy[i] += half_candy[i - 1]

    candy[0] -= half_candy[0]
    candy[0] += half_candy[N - 1]


def check_all_same(candy, n):
    for i in range(n - 1):
        if candy[i] != candy[i + 1]:
            return False

    return True


T = int(input())

for _ in range(T):
    N = int(input())
    candy = [int(x) for x in input().split()]
    count = 0
    make_even()

    while not check_all_same(candy, N):
        circulate()
        make_even()
        count += 1

    print(count)

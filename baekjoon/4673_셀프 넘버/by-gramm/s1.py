def get_next_num(n):
    return n + sum([int(x) for x in list(str(n))])


is_self_num = [True] * 10001

for i in range(1, 10001):
    if is_self_num[i]:
        num = get_next_num(i)

        while num <= 10000 and is_self_num[num]:
            is_self_num[num] = False
            num = get_next_num(num)

for i in range(1, 10001):
    if is_self_num[i]:
        print(i)

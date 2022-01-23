created = [0]*10000
for i in range(1, 10000):
    next_num = i
    while i > 0:
        i, r = divmod(i, 10)
        next_num += r
    if next_num < 10000:
        created[next_num] = 1

for idx, check in enumerate(created):
    if not check and idx > 0:
        print(idx)





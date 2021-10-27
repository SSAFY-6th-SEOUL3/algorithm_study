import random
from itertools import permutations

members = ['광호', '의진', '정환', '재영']
num_list = [0, 1, 2, 3]
combinations = []

perms = list(permutations(num_list, 4))

for perm in perms:
    for i in range(4):
        if perm[i] == i:
            break
    else:
        combinations.append(perm)

result = random.choice(combinations)

for j in range(4):
    print(f'{members[j]} >> {members[result[j]]}의 문제')



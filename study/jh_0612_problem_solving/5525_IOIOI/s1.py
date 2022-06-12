from sys import stdin


N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().rstrip()

pn_count = dict()
idx = 0

while idx < M:
    if S[idx] == 'I':
        cnt_length = 0

        while idx < M - 2 and S[idx + 1] == 'O' and S[idx + 2] == 'I':
            cnt_length += 1
            idx += 2

        if cnt_length >= N:
            pn_count[cnt_length] = pn_count.get(cnt_length, 0) + 1

    idx += 1

total_count = 0

for length, count in pn_count.items():
    total_count += (length - N + 1) * count

print(total_count)

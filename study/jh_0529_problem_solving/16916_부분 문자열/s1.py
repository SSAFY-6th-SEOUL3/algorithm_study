from sys import stdin


S = stdin.readline().rstrip()
P = stdin.readline().rstrip()

S_LEN = len(S)
P_LEN = len(P)

target_sum = 0

for char in P:
    target_sum += ord(char)

accumulates_of_s = [0]

for i in range(S_LEN):
    accumulates_of_s.append(accumulates_of_s[-1] + ord(S[i]))

for i in range(S_LEN - P_LEN + 1):
    if accumulates_of_s[i + P_LEN] - accumulates_of_s[i] == target_sum:
        for j in range(P_LEN):
            if S[i + j] != P[j]:
                break
        else:
            print(1)
            break
else:
    print(0)

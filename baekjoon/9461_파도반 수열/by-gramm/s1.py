
padovans = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

# 규칙: padovans[n] = padovans[n - 1] + padovans[n - 5]
# padovans[11]부터 padovans[100]까지의 값을 구한다.
for _ in range(90):
    padovans.append(padovans[-1] + padovans[-5])

T = int(input())
for _ in range(T):
    print(padovans[int(input())])

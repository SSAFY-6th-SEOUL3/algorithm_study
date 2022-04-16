N = int(input())
s, g, p, d = map(int, input().split())
grades = list(input().rstrip())

max_prices = {'B': s - 1, 'S': g - 1, 'G': p - 1, 'P': d - 1}
max_price = 0

# 다이아몬드 등급인 경우 => 최대 과금액은 다이아몬드 등급 기준액
while grades and grades[-1] == 'D':
    grades.pop()
    max_price += d

# 다이아몬드 등급이 아닌 마지막 달부터 2달씩 최대 과금액을 더한다.
for i in range(len(grades) - 1, -1, -2):
    max_price += max_prices[grades[i]]

print(max_price)

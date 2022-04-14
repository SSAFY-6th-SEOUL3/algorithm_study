import sys
sys.stdin = open('input.txt')


N = int(input())
s, g, p, d = map(int, input().split())
grade_info = input()

total = 0
prev = 0
for i in range(len(grade_info)):
    grade = grade_info[i]

    if grade == "B":
        curr = (s - 1) - prev

    elif grade == "S":
        curr = (g - 1) - prev

    elif grade == "G":
        curr = (p - 1) - prev

    elif grade == "P":
        curr = (d - 1) - prev

    elif grade == "D":
        curr = d

    prev = curr
    total += curr
print(total)

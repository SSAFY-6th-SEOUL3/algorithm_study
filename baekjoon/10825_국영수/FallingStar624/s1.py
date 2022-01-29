import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
students = []
for _ in range(N):
    name, kor, eng, mat = input().split()
    students.append((name, int(kor), int(eng), int(mat)))
students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in students:
    print(student[0])
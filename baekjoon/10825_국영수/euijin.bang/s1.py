"""
정렬
"""

n = int(input())
students = []

for i in range(n):
    student = {}
    info = input().split()
    student['name'] = info[0]
    student['sub1'] = int(info[1])
    student['sub2'] = int(info[2])
    student['sub3'] = int(info[3])

    students.append(student)


sorted_students = sorted(students, key=lambda s: (-s['sub1'], s['sub2'], -s['sub3'], s['name']))
for student in sorted_students:
    print(student['name'])
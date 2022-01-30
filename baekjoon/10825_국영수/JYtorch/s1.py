import sys
sys.stdin = open('input.txt')

N = int(input())
stu_info = [list(input().split()) for _ in range(N)]
stu_info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for info in stu_info:
    print(info[0])
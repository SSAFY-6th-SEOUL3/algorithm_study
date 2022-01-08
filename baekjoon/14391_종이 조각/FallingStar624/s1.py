import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, list(input()))))

# 비트 마스킹 -> 조각 구분
# 계산하는 함수
# 최대값 도출

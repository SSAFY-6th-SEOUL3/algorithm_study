# 맞추긴 했는데... 채점 3분...ㅎ
import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
stats = [[0]*(N+1)]
for _ in range(N):
    stats.append([0] + list(map(int, sys.stdin.readline().split())))

cnt = N//2
teams = list(combinations(range(1, N+1), N//2))
least = 9876543210
for team in teams:
    opp = []
    for i in range(1, N+1):
        if i not in team:
            opp.append(i)
    synergy1 = 0
    synergy2 = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            synergy1 += stats[team[i]][team[j]] + stats[team[j]][team[i]]
    for x in range(N//2):
        for y in range(x+1, N//2):
            synergy2 += stats[opp[x]][opp[y]] + stats[opp[y]][opp[x]]

    if least > abs(synergy1 - synergy2):
        least = abs(synergy1 - synergy2)
    print(team)

print(least)

# 시간초과
import sys
sys.stdin = open("input.txt")

n = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
members = [i+1 for i in range(n)]

r = n // 2
teams = []

# N 명의 경우 N//2 명을 뽑는다
def comb(idx, list):
    if len(list) == r:
        teams.append(list)

    for i in range(idx, n):
        comb(i+1, list + [members[i]])

comb(0, [])

min_diff = 100

# 다시 팀에서 둘씩 뽑는다.
def comb2(idx, list):
    if len(list) == 2:
        twos.append(list)

    for i in range(idx, len(players)):
        comb2(i+1, list + [players[i]])

for i in range(len(teams)//2):
    power_start, power_link = 0, 0

    twos = []
    players = teams[i]
    comb2(0, [])
    for k in range(len(twos)):
        power_start += board[twos[k][0]-1][twos[k][1]-1] + board[twos[k][1]-1][twos[k][0]-1]

    twos = []
    players = teams[len(teams)-i-1]
    comb2(0, [])
    for k in range(len(twos)):
        power_link += board[twos[k][0]-1][twos[k][1]-1] + board[twos[k][1]-1][twos[k][0]-1]

    min_diff = min(min_diff, abs(power_start - power_link))

print(min_diff)
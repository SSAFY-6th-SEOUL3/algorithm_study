
from sys import stdin

# 테트로미노의 각 모양을 직접 구현하기
dr = [
    [0, 0, 0, 0], [-1, 0, 1, 2], [0, 0, 1, 1],                # | / ㅁ
    [0, 1, 1, 1], [0, 0, 0, 1], [0, 1, 1, 2], [0, 1, 1, 2],   # ㅗ
    [0, 0, 0, 1], [0, 1, 2, 2], [0, 1, 1, 1], [0, 0, 1, 2],   # 가로로 긴 ㄱ
    [0, 0, 1, 2], [0, 0, 0, -1], [0, 1, 2, 2], [0, 0, 0, 1],  # 세로로 긴 ㄱ
    [0, 1, 1, 2], [0, 1, 1, 2], [0, 0, 1, 1], [0, 0, 1, 1],   # 번개
]
dc = [
    [-1, 0, 1, 2], [0, 0, 0, 0], [0, 1, 0, 1],
    [0, -1, 0, 1], [0, 1, 2, 1], [0, 0, 1, 0], [0, -1, 0, 0],
    [0, 1, 2, 2], [0, 0, 0, -1], [0, 0, 1, 2], [0, 1, 0, 0],
    [0, 1, 1, 1], [0, 1, 2, 2], [0, 0, 0, 1], [0, 1, 2, 0],
    [0, 0, 1, 1], [0, 0, -1, -1], [0, 1, 1, 2], [0, 1, -1, 0],
]

N, M = map(int, stdin.readline().split())
board = []

# 인덱스 에러 방지를 위해 여유 공간 넣어주기 (왼쪽/위쪽 1칸, 오른쪽/아래쪽 2칸)
board.append([0] * (M + 3))

for _ in range(N):
    board.append([0] + [int(x) for x in stdin.readline().split()] + [0, 0])

for _ in range(2):
    board.append([0] * (M + 3))

max_sum = 0

for r in range(1, N + 1):
    for c in range(1, M + 1):
        for i in range(19):
            current_sum = 0
            for j in range(4):
                current_sum += board[r + dr[i][j]][c + dc[i][j]]

            max_sum = max(max_sum, current_sum)

print(max_sum)

import sys
sys.stdin = open('input.txt')

def solution(arr):
    global cnt
    for i in range(N):
        prev_h = 0                  # 직전 칸의 높이
        move_count = 1              # 연속해서 이동한 평지 칸수
        need_down_stair = False     # 내리막 경사로 설치 예약 여부

        for j in range(N):
            if not prev_h:
                prev_h = arr[i][j]
                continue

            # 직전 높이와 2 이상 차이나면 종료
            if abs(prev_h - arr[i][j]) > 1: break


            # 직전 높이에서 한칸 낮아지는 경우
            if prev_h - arr[i][j] == 1:

                # 내리막 경사로 설치가 예약되어있는 경우
                if need_down_stair:
                    if move_count < L: break        # 경사로를 설치할 공간이 없으면 종료
                    move_count = 1

                # 내리막 경사로 설치가 예약되어 있지 않은 경우
                else:
                    need_down_stair = True          # 내리막 경사로 설치 예약
                    move_count = 1



            # 직전 높이에서 한칸 높아지는 경우
            elif prev_h - arr[i][j] == -1:
                if need_down_stair:
                    if move_count < L * 2: break       # 내리막 경사로 설치 공간이 없으면 종료
                                                       # (연속해서 이동한 평지 칸수가 경사로 길이의 두배보다 크거나 같으면 경사로 설치 가능)
                    need_down_stair = False            # 내리막 경사로 설치 완료 & 예약 지우기
                    move_count = 1

                else:
                    if move_count < L: break           # 오르막 경사로 설치 공간이 없으면 종료
                    move_count = 1


            # 직전 높이와 같은 경우
            elif prev_h - arr[i][j] == 0:
                move_count += 1

                if need_down_stair and move_count >= L:
                    need_down_stair = False              # 내리막 경사로 설치 공간 확보
                    move_count -= L


            prev_h = arr[i][j]

        else:
            # 남아있는 경사로 설치 예약을 이행할 수 있거나, 남아있는 예약이 하나도 없으면 성공!
            if (need_down_stair and move_count >= L) or not need_down_stair:
                cnt += 1








N, L = map(int, input().split())
board = [list(map(int , input().split())) for _ in range(N)]
cnt = 0

solution(board)
board = list(zip(*board[::-1]))     # 90도 회전
solution(board)
print(cnt)
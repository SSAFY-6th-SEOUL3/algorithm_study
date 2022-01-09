answer = []


def hanoi(n, a, b):
    # 원판 1개일 경우
    if n == 1:
        answer.append([a, b])
        return
    # n-1개 원판을 시작 기둥(a)에서 중간 기둥(6-a-b)으로 옮기기
    hanoi(n - 1, a, 6 - a - b)
    # n개의 원판 중 맨밑 원판을 시작 기둥(a)에서 목표 기둥(b)로 옮기기
    answer.append([a, b])
    # n-1개 원판을 중간 기둥(6-a-b)에서 목표 기둥(b)으로 옮기기
    hanoi(n - 1, 6 - a - b, b)
    return


def solution(n):
    hanoi(n, 1, 3)
    """    
    n == 3 일 때,
    
        hanoi(2, 1, 2) => hanoi(1, 1, 3) 1, 3
        1, 2
        hanoi(2, 1, 2) => hanoi(1, 3, 2) 3, 2
    1, 3    
        hanoi(2, 2, 3) => hanoi(1, 2, 1) 2, 1  
        2, 3
        hanoi(2, 2, 3) => hanoi(1, 1, 3) 1, 3     
    
    """
    return answer

print(solution(3))
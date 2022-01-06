def move_disc(n, start, finish, bypass, record):
    """
    :param n: 원반 개수
    :param start: 출발 기둥
    :param finish: 도착 기둥
    :param bypass: 경유 기둥
    :param record: 이동 기록을 담을 빈 리스트
    :return: record
    """
    if n == 1:
        record.append([start, finish])
        return record
    else:
        # 제일 큰 원판을 제외하고 나머지 두 번째 기둥으로 전부 이동
        move_disc(n-1, start, bypass, finish, record)
        # 제일 큰 원판 세 번째 기둥으로 이동 (1 -> 3)
        move_disc(1, start, finish, bypass, record)
        move_disc(n-1, bypass, finish, start, record)


def solution(n):
    answer = []
    move_disc(n, 1, 3, 2, answer)
    return answer


print(solution(2))  # [[1,2], [1,3], [2,3]]
print(solution(3))  # [[1,3], [1,2], [3,1], [1,3], [2,1], [2,3], [1,3]]

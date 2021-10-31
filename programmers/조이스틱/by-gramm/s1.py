# 그리디로 풀이 => 11번 테스트케이스 틀림.

def solution(name):
    N = len(name)

    # 각 알파벳에 대하여, 조이스틱을 몇 번 조작해야 하는지 구한다.
    operations = [min(91 - ord(x), ord(x) - 65) for x in name]

    # M: A가 아닌 알파벳의 개수
    M = N - operations.count(0)
    # idx: 현재 탐색중인 인덱스
    # total: 총 조이스틱 조작 횟수
    idx, total = 0, 0

    # 시작 알파벳이 'A'가 아니면, 'A'로 만들어준다.
    if operations[0]:
        total += operations[0]
        operations[0] = 0
        M -= 1

    # 그리디: 매번 가장 가까이에 있는 위치로 이동하여, 알파벳을 완성한다. (M번 반복)
    for _ in range(M):
        i = 1
        while True:
            if operations[(idx - i) % N]:  # 왼쪽 경로 탐색
                idx = (idx - i) % N
                total += (i + operations[idx])
                operations[idx] = 0
                break
            if operations[(idx + i) % N]:  # 오른쪽 경로 탐색
                idx = (idx + i) % N
                total += (i + operations[idx])
                operations[idx] = 0
                break
            i += 1

    return total

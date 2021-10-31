# 일종의 완전탐색으로 풀이함.

def solution(name):
    N = len(name)  # 이름의 길이

    # 각 알파벳에 대하여, 조이스틱을 최소 몇 번 조작해야 하는지 구한다.
    operations = [min(91 - ord(x), ord(x) - 65) for x in name]

    M = N - operations.count(0)  # M: A가 아닌 알파벳의 개수
    min_total = 10000            # min_total: 총 조이스틱 조작 횟수의 최소값

    # 시작 알파벳이 A가 아니면, M에서 1을 뺀다. (시작점은 탐색을 하지 않으므로)
    if operations[0]:
        M -= 1

    # 1) 왼쪽으로 먼저 가는 경우 : (왼쪽에서 M개 / ... / 왼쪽에서 1개, 오른쪽에서 M - 1개)
    for i in range(1, M + 1):
        # left, right: 각각 왼쪽/오른쪽으로 가서 바꾸는 알파벳의 개수
        left, right, count = 0, 0, 0

        while count < i:
            left -= 1
            if operations[left]:
                count += 1

        while count < M:
            right += 1
            if operations[right]:
                count += 1

        # 왼쪽으로만 가서 탐색을 마친다면
        if not right:
            min_total = min(min_total, -left)
        else:
            min_total = min(min_total, -2 * left + right)

    # 2) 오른쪽으로 먼저 가는 경우: (오른쪽에서 M개 /.../ 오른쪽에서 1개, 왼쪽에서 M - 1개)
    for i in range(1, M + 1):
        left, right, count = 0, 0, 0

        while count < i:
            right += 1
            if operations[right]:
                count += 1

        while count < M:
            left -= 1
            if operations[left]:
                count += 1

        # 오른쪽으로만 가서 탐색을 마친다면
        if not left:
            min_total = min(min_total, right)
        else:
            min_total = min(min_total, 2 * right - left)

    return min_total + sum(operations)  # 최소 이동 횟수 + 각 알파벳을 A로 바꾸는 조작 횟수의 합

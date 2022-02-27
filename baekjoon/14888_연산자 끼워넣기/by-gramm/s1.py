N = int(input())
numbers = [int(x) for x in input().split()]
counts = [int(x) for x in input().split()]

max_value = -1000000000
min_value = 1000000000


def get_result(cnt_value, counts, used_count):
    """
    cnt_value: 현재까지 계산한 값
    counts: 사칙연산 연산자의 남은 개수
    used_count: 사용한 연산자의 개수
    """
    global numbers, N, max_value, min_value

    # 모든 연산자를 다 사용한 경우 => 최대값과 최소값을 업데이트하고 탐색 종료
    if used_count == (N - 1):
        max_value = max(max_value, cnt_value)
        min_value = min(min_value, cnt_value)
        return

    for i, count in enumerate(counts):
        if count:
            counts[i] -= 1

            if i == 0:
                get_result(cnt_value + numbers[used_count + 1], counts, used_count + 1)
            elif i == 1:
                get_result(cnt_value - numbers[used_count + 1], counts, used_count + 1)
            elif i == 2:
                get_result(cnt_value * numbers[used_count + 1], counts, used_count + 1)
            else:
                # 음수를 양수로 나누는 경우 처리
                if cnt_value < 0:
                    next_value = -(-cnt_value // numbers[used_count + 1])
                else:
                    next_value = cnt_value // numbers[used_count + 1]
                get_result(next_value, counts, used_count + 1)

            counts[i] += 1


get_result(numbers[0], counts, 0)

print(max_value)
print(min_value)

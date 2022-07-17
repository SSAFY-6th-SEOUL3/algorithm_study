def is_subset(a, b, length):
    """
    a가 b의 부분집합이면 True, 아니면 False를 리턴한다.
    """
    for i in range(length):
        if a[i] == '1' and b[i] == '0':
            return False

    return True


def is_unique(relation, R, C):
    """
    릴레이션의 모든 튜플이 유일하게 식별 가능하면 True, 아니면 False를 리턴한다.
    """
    for r1 in range(R - 1):
        for r2 in range(r1 + 1, R):
            is_unique = False

            for c in range(C):
                if relation[r1][c] != relation[r2][c]:
                    is_unique = True

            if not is_unique:
                return False

    return True


def solution(relation):
    R = len(relation)
    C = len(relation[0])

    every_set = []
    candidates = []
    count = 0

    for i in range(2 ** C):
        # ex. C가 8, i가 21인 경우, 0b10101 => '0b10101' => '10101' => '00010101'
        every_set.append(str(bin(i)).lstrip('0b').zfill(C))

    # 각 경우에 대하여, 유일성을 만족하는지 검사한다.
    # 유일성을 만족하면, 해당 경우를 포함하는 다른 모든 경우를 제거한다. (최소성을 만족하지 않으므로)
    for idx in range(1, 2 ** C):
        current = every_set[idx]
        is_superset = False

        # 현재 집합이 유일성을 만족하는 다른 집합의 superset인지 검사한다.
        for candidate in candidates:
            if is_subset(candidate, current, C):
                is_superset = True
                continue

        if is_superset:
            continue

        current_set = []

        for tuple in relation:
            sub_tuple = []

            for j in range(C):
                if current[j] == '1':
                    sub_tuple.append(tuple[j])

            current_set.append(sub_tuple)

        # current_set이 유일하게 식별 가능한지 검사한다.
        if is_unique(current_set, R, len(current_set[0])):
            candidates.append(current)
            count += 1

    return count

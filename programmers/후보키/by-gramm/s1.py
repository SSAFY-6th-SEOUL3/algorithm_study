# def find_candidate_key(count, cnt_key):
#     """
#     Args:
#         count: 현재까지 탐색한 컬럼의 개수
#         cnt_key: 현재까지 저장한 튜플
#     """
#     global r_length, c_length
#
#     for r in range(count, r_length):
#         new_keys = cnt_key + [r]
#         new_set = set()
#
#         for c in range(c_length):
#             new_set.add()


from itertools import combinations


def solution(relation):
    r_length = len(relation)
    c_length = len(relation[0])

    rows = [*range(r_length)]
    candidate_combinations = []
    candidate_list = []
    candidate_count = 0

    for r in range(1, r_length):
        candidate_combinations.append(list(combinations(rows, r)))

    for idx, combs in enumerate(candidate_combinations):
        for row_set in combs:
            temp_set = set()
            for c in range(c_length):
                temp = {relation[c][r] for r in row_set}
                temp_set.add(temp)

            # 후보키 발견
            if len(temp_set) == c_length:
                candidate_list.append(row_set)

    return candidate_list


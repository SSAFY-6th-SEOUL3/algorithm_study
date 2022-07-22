from itertools import combinations


def solution(orders, course):
    orders = [sorted(list(o)) for o in orders]
    result = []

    for count in course:
        count_dict = dict()

        for order in orders:
            for comb in combinations(order, count):
                count_dict[comb] = count_dict.get(comb, 0) + 1

        max_count = 0

        for count in count_dict.values():
            max_count = max(max_count, count)

        if max_count > 1:
            for key, count in count_dict.items():
                if count == max_count:
                    result.append("".join(key))

    return sorted(result)


def solution(phone_book):
    number_dict = [[] for _ in range(10)]

    for phone_num in phone_book:
        number_dict[int(phone_num[0])].append(phone_num)

    for num_set in number_dict:
        num_set.sort()

        for idx in range(1, len(num_set)):
            if num_set[idx].startswith(num_set[idx - 1]):
                return False

    return True

print(solution(['']))
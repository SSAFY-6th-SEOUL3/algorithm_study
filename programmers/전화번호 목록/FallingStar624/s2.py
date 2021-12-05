# 해시 적용
def solution(phone_book):
    answer = True
    hash_book = {}
    for number in phone_book:
        hash_book[number] = len(number)
    for numbers in hash_book.keys():
        prefix = ''
        for num in numbers[:-1]:
            prefix += num
            if prefix in hash_book:
                answer = False
                break
    return answer

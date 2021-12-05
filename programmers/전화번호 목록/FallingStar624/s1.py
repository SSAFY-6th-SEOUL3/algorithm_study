# 정확도 테스트 통과/ 효율성 테스트 실패
def solution(phone_book):
    answer = True
    cnt = 0
    n = len(phone_book)
    for phone_number in phone_book:
        m = len(phone_number)
        for compare in phone_book:
            if phone_number == compare[:m]:
                cnt += 1
    if cnt - n > 0:
        answer = False
    return answer

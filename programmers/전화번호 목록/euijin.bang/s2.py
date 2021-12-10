phone_book = ["97674223","11","12","111", "119", "1195524421"]

def solution(phone_book):
    phone_book.sort()
    answer = True

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer


print(solution(phone_book))
def solution(phoneBook):
    n = len(phoneBook)
    phoneBook.sort()
    for i in range(n-1):
        if phoneBook[i] == phoneBook[i+1][:len(phoneBook[i])]:
            return False
    return True
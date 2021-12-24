# TC 15, 19 x
# TC 3, 4 시간초과

phone_book = ["97674223", "97674223", "11","12","111","111", "119", "97674223", "1195524421"]

# hash 내장함수 : 문자열, 정수형, 불린형, 튜플 을 고유의 임의 정수값으로 변환

def solution(phone_book):
    hashes = []
    lens = []
    for num in phone_book:
        hashes.append(hash(num))
        lens.append(len(num))

    for n in lens:
        for num in phone_book:
            # n개를 앞에서부터 확인
            if (hash(num[:n]) in hashes) and n != len(num): # 자기자신 제외
                return False
        return True

print(solution(phone_book))



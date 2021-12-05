text = "x"

def solution(text):
    min_result = 999
    if len(text) == 1:
        return 1
    for n in range(1, len(text)//2+1):
        result = ""
        cnt = 1
        tmp = text[:n]
        for i in range(n, len(text), n): # n번째 인덱스부터 n씩 건너뛰며 검사
            if tmp == text[i:i+n]:       # 임시 문자열과 다음 문자열이 같으면 cnt증가
                cnt += 1
            else:       # 임시 문자열과 다음 문자열이 다르면
                # cnt 가 1 초과일 경우
                if cnt > 1:
                    result += str(cnt) + tmp
                # cnt 가 1일 경우
                else:
                    result += tmp   # 1생략
                cnt = 1
                tmp = text[i:i+n] # tmp 이동

        # tmp 결과 담기
        if cnt > 1:
            result += str(cnt) + tmp
        else:
            result += tmp

        if len(result) < min_result:
            min_result = len(result)

    return min_result

print(solution(text))

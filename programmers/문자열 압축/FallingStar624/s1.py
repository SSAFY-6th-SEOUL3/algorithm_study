def solution(s):
    n = len(s)
    if n == 1:
        return 1
    result = [s]
    for i in range(1, n//2 + 1):
        j = 0
        tmp = ''
        num = 1
        while j < n:
            if len(tmp) >= n:
                break
            if s[j:j+i] == s[j+i:j+2*i]:
                num += 1
                j += i
            else:
                if j == 0:
                    tmp += s[:i]
                    j += i
                else:
                    if num > 1:
                        tmp += str(num) + s[j:j+i]
                        j += i
                        num = 1
                    else:
                        tmp += s[j]
                        j += 1
        else:
            if num > 1:
                tmp += str(num) + s[j-i:]
            if 48 <= ord(tmp[0]) <= 57:
                result.append(tmp)
            else:
                if 48 <= ord(tmp[i]) <= 57:
                    result.append(tmp)
                else:
                    pass

    result = list(map(len, result))
    return min(result)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))
print(solution("aababa"))



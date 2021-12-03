def solution(s):
    n = len(s)
    result = [n]
    for i in range(1, n//2 + 1):
        cnt = 1
        tmp = ''
        current = s[:i]
        for j in range(i, n, i):
            if current == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += str(cnt) + current
                    cnt = 1
                else:
                    tmp += current
            current = s[j: j + i]
        else:
            if cnt > 1:
                tmp += str(cnt) + current
            else:
                tmp += current
        result.append(len(tmp))
    return min(result)


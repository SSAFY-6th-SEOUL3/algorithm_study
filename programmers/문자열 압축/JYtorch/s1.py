def solution(s):
    answer = set()
    n = len(s) // 2

    if len(s) == 1:
        return 1

    for i in range(1, n + 1):
        string = ''
        string_cnt = 1
        idx = 0
        while idx < len(s):
            if s[idx:idx+i] == s[idx+i:idx+i*2]:
                string_cnt += 1
            else:
                if string_cnt >= 2:
                    string += str(string_cnt) + s[idx:idx+i]
                    string_cnt = 1
                else:
                    string += s[idx:idx+i]
            idx += i

        answer.add(len(string))
    return min(answer)

print(solution("a"))
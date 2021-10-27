def solution(name):
    answer = 0
    for x in name:
        tmp = ord(x)
        if tmp > 78:
            tmp = 91 - tmp
        else:
            tmp -= 65
        answer += tmp

    return answer - 1


print(solution('JEROEN'))
print(solution('JAN'))

# print('---'*4)
# for i in range(65, 91):
#     print(i-64, chr(i))


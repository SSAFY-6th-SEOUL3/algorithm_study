# error

def solution(n):
    total = []
    for i in range(n):
        total.append([0] * (i + 1))


    start = 1
    end = 0
    for i in range(n):
        end += i + 1

    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                total[i][j] = start + i
                continue
            if n % 2:
                if i == j:
                    total[i][j] = end
                    continue
            else:
                if i == j:
                    total[i][j] = end - i
                    continue
            if n % 2:
                pass
            else:
                if i == n // 2:
                    total[i][i // 2] = end
                    continue
            if i == (n - 1):
                for j in range(n):
                    total[-1][j] = n
                    n += 1
                break

    result = []
    for i in range(len(total)):
        result.extend(total[i])
    return result

print(solution(4))
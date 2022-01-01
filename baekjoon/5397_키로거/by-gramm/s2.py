# 시간 초과

T = int(input())

for _ in range(T):
    current, length = 0, 0   # 현재 커서의 위치 / 현재 단어의 길이
    password = []
    total_input = input().strip('<>')
    i = 0
    L = len(total_input)

    while i < L:
        key_input = total_input[i]
        i += 1

        if key_input == '<':
            current = max(0, current - 1)
        elif key_input == '>':
            current = min(length, current + 1)
        elif key_input == '-':
            if 0 < current:
                password.pop(current - 1)
                current -= 1
                length -= 1
        else:
            temp = [key_input]

            while i < L:
                new_input = total_input[i]
                if new_input in '<>-':
                    break
                temp.append(new_input)
                i += 1

            password = password[:current] + temp + password[current:]
            current += len(temp)
            length += len(temp)

    print("".join(password))

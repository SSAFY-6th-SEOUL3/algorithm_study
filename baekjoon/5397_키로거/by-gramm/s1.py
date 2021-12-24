# 시간 초과

T = int(input())

for _ in range(T):
    current, length = 0, 0   # 현재 커서의 위치 / 현재 단어의 길이
    password = []

    for key_input in input():
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
            password.insert(current, key_input)
            current += 1
            length += 1

    print("".join(password))

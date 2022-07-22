def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    result = []

    for char in new_id:
        if char in '-_.' or char.isalnum():
            result.append(char)

    # 3단계
    idx = 0

    while idx < len(result):
        if result[idx] == '.':
            idx += 1

            while idx < len(result) and result[idx] == '.':
                result[idx] = ''
                idx += 1
        else:
            idx += 1

    result = "".join(result)

    # 4단계
    result = result.strip('.')

    # 5단계
    if not result:
        result = "a"

    # 6단계 + 7단계
    if len(result) > 15:
        result = result[:15].rstrip('.')
    elif len(result) < 3:
        while len(result) < 3:
            result += result[-1]

    return result

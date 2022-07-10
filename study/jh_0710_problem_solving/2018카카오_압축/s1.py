def solution(msg):
    msg_dict = dict()

    for i in range(1, 27):
        msg_dict[chr(i + 64)] = i

    idx = 0
    dict_count = 26
    M_LEN = len(msg)
    result = []

    while idx < M_LEN:
        length = 1

        while idx + length <= M_LEN and msg[idx: idx + length] in msg_dict:
            length += 1

        current = msg[idx: idx + length]

        if current in msg_dict:
            result.append(msg_dict[current])
        else:
            dict_count += 1
            msg_dict[current] = dict_count
            result.append(msg_dict[msg[idx: idx + length - 1]])

        idx += (length - 1)

    return result

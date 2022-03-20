def solution(record):
    id_and_nickname = dict()
    messages = []

    for line in record:
        command, id, *nickname = line.split()

        if command == 'Leave':
            messages.append([id, 'L'])
        else:
            id_and_nickname[id] = nickname[0]

            if command == 'Enter':
                messages.append([id, 'E'])

    result = []

    for message in messages:
        nickname = id_and_nickname[message[0]]

        if message[1] == 'E':
            result.append(f"{nickname}님이 들어왔습니다.")
        else:
            result.append(f"{nickname}님이 나갔습니다.")

    return result

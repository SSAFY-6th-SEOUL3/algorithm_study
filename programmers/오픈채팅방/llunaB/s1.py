def solution(record):
    room = []  # id, 들어오고 나간 정보
    info = {}  # 키는 아이디, 밸류는 최종 닉네임

    for rc in record:
        r = rc.split()  # r[0] = 행동, r[1] = id, r[2] = 닉네임

        if r[0] == "Enter":
            room.append([r[1], "님이 들어왔습니다."])
            info[r[1]] = r[2]  # 닉네임 업데이트

        elif r[0] == "Leave":
            room.append([r[1], "님이 나갔습니다."])

        elif r[0] == "Change":
            info[r[1]] = r[2]

    # 아이디에 닉네임을 매칭
    result = list(map(lambda x: info[x[0]] + x[1], room))

    return result

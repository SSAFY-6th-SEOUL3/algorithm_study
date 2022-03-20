def solution(record):
    uid_set = {}
    for data in record:
        res = data.split()
        if len(res) == 3:
            command, uid, nickname = res
            uid_set[uid] = nickname
        else:
            command, uid = res
    answer = []
    for data in record:
        res = data.split()
        if res[0] == 'Enter':
            answer.append(f'{uid_set[res[1]]}님이 들어왔습니다.')
        elif res[0] == 'Leave':
            answer.append(f'{uid_set[res[1]]}님이 나갔습니다.')
    return answer

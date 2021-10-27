def solution(participant, completion):
    players = {}

    # 완성한 선수들의 이름을 key, 선수의 수를 value로 저장한다.
    for c in completion:
        players[c] = players.get(c, 0) + 1

    for p in participant:
        # players에 선수가 없거나, 남은 선수의 수가 0이라면 => 해당 선수를 리턴한다.
        if not players.get(p, 0):
            return p
        # 현재 탐색한 선수의 수를 1 감소시킨다.
        players[p] -= 1

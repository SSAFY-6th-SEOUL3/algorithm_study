# 해시맵(딕셔너리)

def solution(participant, completion):
    # 해쉬 넣을 딕셔너리 만든다.
    hashDict = {}
    sumHash = 0

    # participant 의 해시를 구하고, 해시맵(딕셔너리)에 더한다.
    for part in participant:
        hashDict[hash(part)] = part
        # 해시의 합을 더한다.
        sumHash += hash(part)

    # completion 을 돌면서 해시값을 뺀다.
    for comp in completion:
        sumHash -= hash(comp)

    # 남은 값이 곧 완주하지 못한 선수의 hash 값이므로 딕셔너리에서 찾아 반환한다.
    answer = hashDict[sumHash]
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))


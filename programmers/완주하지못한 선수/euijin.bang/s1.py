def solution(participant, completion):
    # 인덱스 비교 위해 정렬
    participant.sort()
    completion.sort()

    # 완주자 수(참가자 수-1) 만큼 돌면서 인덱스 비교, 다르면 미완주
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    # 다 돌았으면 마지막 참가자가 미완주
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
from collections import Counter

def solution(participant, completion):
    print(Counter(participant))
    print(Counter(completion))
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

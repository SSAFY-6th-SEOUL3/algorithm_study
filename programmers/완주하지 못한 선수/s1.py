def solution(participant, completion):
    people = {part: 0 for part in participant}
    for part in participant:
        people[part] += 1
    for comp in completion:
        if people.get(comp) == 1:
            people.pop(comp)
        elif people.get(comp) > 1:
            people[comp] -= 1
        else:
            pass
    answer = list(people.keys())[0]
    return answer

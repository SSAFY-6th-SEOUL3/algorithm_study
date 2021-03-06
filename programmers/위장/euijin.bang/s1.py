# hash 활용

def solution(clothes):
    counter = {}
    for cloth in clothes:
        counter[cloth[1]] = counter.get(cloth[1], 0) + 1
        # key가 있으면 해당 value를, 없으면 0을 반환 {'headgear': 2, 'eyewear': 1}

    # 옷을 입는 경우의 수 = (종류1 + 1) * (종류2 + 1) * ...  - 1 (모두 안입는 경우는 뺀다)
    total = 1
    for v in counter.values():
        total *= v+1

    total -= 1

    return total

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))


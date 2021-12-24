def solution(clothes):
    #     다른 방법!
    #     1. clothes를 인덱스로 다루기 위한 인덱스 리스트 생성
    #         [0, 0, 0]
    #     2. 하나씩 꺼낸 clothe를 빈 리스트에 넣어주자!

    #     3. [['yellowhat', 'green_tunban'], ['bluesunglasses']]
    #     [['crowmask', 'bluesunglasses', 'smoky_makeup']]
    #     """

    dic = {}
    for clothe in clothes:
        if dic.get(clothe[1], 0):
            dic[clothe[1]] += 1
        else:
            dic[clothe[1]] = 1

    answer = 1
    for value in dic.values():
        answer *= value + 1
    answer -= 1

    return answer
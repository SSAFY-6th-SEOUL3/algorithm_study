
def solution(clothes):
    cl_count = dict()

    for name, cl_type in clothes:
        cl_count[cl_type] = cl_count.get(cl_type, 0) + 1    # ex. {'eyewear': 2, 'headgear': 3}

    total_count = 1

    """
    [의상을 조합하는 경우의 수]
    ex. 상의가 3개 | 하의가 2개 | 겉옷이 4개 있는 경우
        => 상의는 3개 중 하나를 입거나 안 입을 수 있으므로 총 4가지 경우의 수
        => 마찬가지로 하의는 2+1=3가지, 겉옷은 4+1=5가지 경우의 수를 가진다.
        => 따라서 전체 경우의 수는 의상 종류별 개수에 1을 더한 것을 모두 곱한 것과 같다.
    """
    for count in cl_count.values():
        total_count *= (count + 1)

    return total_count - 1   # 아무것도 입지 않을 수는 없으므로 1을 뺀다.

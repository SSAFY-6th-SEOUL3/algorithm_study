import sys
sys.setrecursionlimit(100000)


def pre_traverse(node, traverse_list, left, right):
    """
    주어진 이진 트리를 전위 순회한 결과를 리턴한다.
    """
    # 1. 현재 노드 탐색
    traverse_list[0].append(node)
    # 2. 왼쪽 자식 트리 탐색
    if left[node] != -1:
        pre_traverse(left[node], traverse_list, left, right)
    # 3. 오른쪽 자식 트리 탐색
    if right[node] != -1:
        pre_traverse(right[node], traverse_list, left, right)


def post_traverse(node, traverse_list, left, right):
    """
    주어진 이진 트리를 후위 순회한 결과를 리턴한다.
    """
    # 1. 왼쪽 자식 트리 탐색
    if left[node] != -1:
        post_traverse(left[node], traverse_list, left, right)
    # 2. 오른쪽 자식 트리 탐색
    if right[node] != -1:
        post_traverse(right[node], traverse_list, left, right)
    # 3. 현재 노드 탐색
    traverse_list[1].append(node)


def solution(nodeinfo):
    N = len(nodeinfo)

    if N == 1:
        return [[1], [1]]

    left_range = [-1] * (N + 1)        # left_range[i]: 값이 N이면, i번 노드의 번호는 N보다 크다.
    right_range = [100001] * (N + 1)   # right_range[i]: 값이 N이면, i번 노드의 번호는 N보다 작다.

    x_coordinates = [-1] * (N + 1)     # x_coordinates[i]: i번 노드의 x좌표
    left = [-1] * (N + 1)              # left[i]: i번 노드의 왼쪽 자식 노드의 번호
    right = [-1] * (N + 1)             # right[i]: i번 노드의 오른쪽 자식 노드의 번호

    # nodeinfo에 노드 번호 정보를 추가한다.
    for i in range(N):
        nodeinfo[i].append(i + 1)

    # nodeinfo를 y 좌표 기준 내림차순, x 좌표 기준 오름차순 정렬한다.
    nodeinfo.sort(key=lambda x: x[0])
    nodeinfo.sort(key=lambda x: x[1], reverse=True)

    nodes = [[] for _ in range(1001)]  # nodes[i]: 높이가 i인 노드의 리스트
    root = nodeinfo[0][2]              # root: 루트 노드의 번호
    nodes[0].append(root)
    x_coordinates[root] = nodeinfo[0][0]

    idx, height = 1, 1

    # 루트 노드부터 높이가 같은 노드들을 모두 순회하면서
    # 각 노드의 부모 노드 및 자식 노드의 번호를 저장한다.
    while idx < N:
        p_idx = 0
        cnt_parent = nodes[height - 1][p_idx]
        cnt_y = nodeinfo[idx][1]

        # 같은 높이에 있는 노드를 모두 탐색한다.
        while idx < N and nodeinfo[idx][1] == cnt_y:
            x, y, num = nodeinfo[idx]
            x_coordinates[num] = x

            while True:
                # 왼쪽 자식 노드인 경우
                if left[cnt_parent] == -1 and x < x_coordinates[cnt_parent]:
                    left[cnt_parent] = num
                    left_range[num] = left_range[cnt_parent]
                    right_range[num] = x_coordinates[cnt_parent]
                    break
                # 오른쪽 자식 노드인 경우
                elif right[cnt_parent] == -1 and x < right_range[cnt_parent]:
                    right[cnt_parent] = num
                    left_range[num] = x_coordinates[cnt_parent]
                    right_range[num] = right_range[cnt_parent]
                    break
                # 현재 부모 노드의 자식 노드가 아닌 경우
                else:
                    p_idx += 1
                    cnt_parent = nodes[height - 1][p_idx]

            nodes[height].append(num)
            idx += 1

        height += 1

    traverse_list = [[], []]

    # 이진 트리를 전위 순회한 결과를 traverse_list에 저장한다.
    pre_traverse(root, traverse_list, left, right)

    # 이진 트리를 후위 순회한 결과를 traverse_list에 저장한다.
    post_traverse(root, traverse_list, left, right)

    return traverse_list

from sys import stdin


while True:
    n, k = map(int, stdin.readline().split())

    if n == k == 0:
        break

    numbers = [int(x) for x in stdin.readline().split()]

    parents = [-1] * n  # 각 노드의 부모 노드의 인덱스를 저장하는 배열
    p_idx = -1          # 현재 노드의 부모 노드의 인덱스

    for i in range(1, n):
        if numbers[i] > numbers[i - 1] + 1:  # 이전 노드 + 1보다 더 크면,
            p_idx += 1                       # 부모 노드를 다음 노드로 이동시킨다.

        parents[i] = p_idx

    target_idx = numbers.index(k)  # k의 인덱스
    count = 0                      # k와 사촌 관계인 노드의 개수

    for i in range(n):
        """
        k와 1) 부모 노드가 다르고 / 2) 부모의 부모 노드는 같은 (부모끼리 형제 관계인) 노드의 개수를 구한다.
        """
        if (parents[i] != parents[target_idx]
                and parents[parents[i]] == parents[parents[target_idx]]):
            count += 1

    print(count)

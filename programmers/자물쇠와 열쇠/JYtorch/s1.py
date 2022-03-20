def solution(key, lock):
    N = len(key)
    M = len(lock)
    # 4개 키 만들기(0도, 90도, 180도, 270도 회전)
    key_list = [key]
    for _ in range(3):
        key = list(zip(*key[::-1]))
        key_list.append(key)

    # padding
    T = M + (N - 1) * 2

    # 키 사용
    for key in key_list:

        for i in range(N + M - 1):
            for j in range(N + M - 1):
                check = False

                # padding 포함한 arr 새로 만들기
                arr = [[0] * T for _ in range(T)]
                for r in range(M):
                    for c in range(M):
                        arr[r + N - 1][c + N - 1] = lock[r][c]

                # 키 넣어주기
                for r in range(N):
                    for c in range(N):
                        arr[i + r][j + c] += key[r][c]

                # 자물쇠에 잘 맞는지 확인
                for r in range(N - 1, M + N - 1):
                    for c in range(N - 1, M + N - 1):
                        if arr[r][c] == 2 or arr[r][c] == 0:
                            check = True
                            break
                    if check:
                        break

                if not check:
                    return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

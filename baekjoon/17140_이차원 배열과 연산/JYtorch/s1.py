import sys
sys.stdin = open('input.txt')

def solution():
    cnt = 0

    while cnt <= 100:
        if len(A) > r - 1 and len(A[0]) > c - 1:
            if A[r - 1][c - 1] == k: return cnt

        if len(A) >= len(A[0]):
            nums_set = []
            r_length = []
            for i in range(len(A)):
                r_arr = {}
                for j in A[i]:
                    if not j: continue
                    if r_arr.get(j, 0):
                        r_arr[j] += 1
                    else:
                        r_arr[j] = 1
                tmp = []

                for key, value in r_arr.items():
                    tmp.append((key, value))
                tmp.sort(key=lambda x:(x[1], x[0]))
                tmp_set = []
                for num_set in tmp:
                    tmp_set.append(num_set[0])
                    tmp_set.append(num_set[1])
                nums_set.append(tmp_set)
                r_length.append(len(tmp_set))

            for i in range(len(A)):
                A[i] = nums_set[i][:100]

            if max(r_length) > 100:
                r_len = 100
            else:
                r_len = max(r_length)

            for i in range(len(A)):
                while len(A[i]) < r_len:
                    A[i].append(0)


        else:
            nums_set = []
            c_length = []
            for i in range(len(A[0])):
                c_arr = {}
                for j in range(len(A)):
                    if not A[j][i]: continue
                    if c_arr.get(A[j][i], 0):
                        c_arr[A[j][i]] += 1
                    else:
                        c_arr[A[j][i]] = 1
                tmp = []

                for key, value in c_arr.items():
                    tmp.append((key, value))
                tmp.sort(key=lambda x:(x[1], x[0]))

                tmp_set = []
                for num_set in tmp:
                    tmp_set.append(num_set[0])
                    tmp_set.append(num_set[1])
                nums_set.append(tmp_set[:100])
                c_length.append(len(tmp_set[:100]))

            c_len = max(c_length)
            for i in range(c_len):
                if len(A) > i:
                    A[i] = [0] * len(A[0])
                else:
                    A.append([0] * len(A[0]))

            idx = 1
            while len(A) > c_len:
                A.pop(len(A) - idx)
                idx += 1

            for i in range(len(c_length)):
                for j in range(c_len):
                    if len(nums_set[i]) > j:
                        A[j][i] = nums_set[i][j]
                    else:
                        A[j][i] = 0
        cnt += 1

    return -1

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
print(solution())

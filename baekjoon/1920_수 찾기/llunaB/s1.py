"""
binary search
O(logN)
"""

# left = list[:mid] , mid 가 5000이면 5000개짜리 리스트를 다 복사함 ... 결과적으로는 N
# 아래는 새 리스트 복사가 아닌 기존 리스트 활용, 참조만 함


def binary_search(value, start, end):
    # 재귀 종료 기준 - 일치하는 값이 없으면 start 가 end 를 넘어감
    if start > end:
        return False

    mid = (start + end) // 2

    if data_list[mid] > value:
        return binary_search(value, start, mid - 1)
    elif data_list[mid] < value:
        return binary_search(value, mid + 1, end)
    else:
        return True


N = int(input())
data_list = sorted(list(map(int, input().split())))

M = int(input())
num_list = list(map(int, input().split()))

# N, M = 5, 5
# data_list = [1, 2, 3, 4, 5]
# num_list = [7, 9, 5]

for num in num_list:
    print(int(binary_search(num, 0, N - 1)))

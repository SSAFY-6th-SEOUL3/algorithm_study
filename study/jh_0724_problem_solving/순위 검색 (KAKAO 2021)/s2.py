def get_abbr(arr):
    return "".join([x[0] for x in arr])


def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid

    return start


def solution(info, query):
    info_dict = dict()

    for sub_info in info:
        sub_info = sub_info.split(' ')
        point = int(sub_info.pop())
        abbr = get_abbr(sub_info)

        if abbr in info_dict:
            info_dict[abbr].append(point)
        else:
            info_dict[abbr] = [point]

    for abbr in info_dict:
        info_dict[abbr].sort()

    counts = []

    for cnt_query in query:
        cnt_info = cnt_query.split(' and ')
        food_and_point = cnt_info.pop().split(' ')
        cnt_info.append(food_and_point[0])
        cnt_point = int(food_and_point[1])
        cnt_abbr = []
        count = 0

        for i, char in enumerate(get_abbr(cnt_info)):
            if char != '-':
                cnt_abbr.append([i, char])

        for abbr, points in info_dict.items():
            flag = True

            for i, char in cnt_abbr:
                if abbr[i] != char:
                    flag = False
                    break

            if flag:
                count += (len(points) - binary_search(points, cnt_point))

        counts.append(count)

    return counts

def solution(operations):
    heap = []
    for data in operations:
        # 숫자 삽입
        if data[0] == 'I':
            heap.append(int(data[2:]))


        else:
            if not heap: continue
            # 최솟값 삭제
            if data[2:] == '-1':
                heap.pop(0)

            # 최댓값 삭제
            elif data[2:] == '1':
                heap.pop()
        heap.sort()

    answer = [0, 0]
    if heap:
        answer[0] = heap[len(heap) - 1]
        answer[1] = heap[0]
    return answer
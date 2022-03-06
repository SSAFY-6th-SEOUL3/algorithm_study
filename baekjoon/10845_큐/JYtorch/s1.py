import sys
sys.stdin = open('input.txt')

N = int(input())

queue = [0] * 10000
front, rear = -1, -1
for _ in range(N):
    order_info = sys.stdin.readline().split()
    if len(order_info) == 2:
        order, number = order_info
    else:
        order = order_info[0]

    if order == 'push':
        rear += 1
        queue[rear] = int(number)

    elif order == 'pop':
        if front == rear:
            print(-1)
        else:
            front += 1
            print(queue[front])

    elif order == 'size':
        print(rear - front)

    elif order == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if front == rear:
            print(-1)
        else:
            print(queue[front + 1])

    elif order == 'back':
        if front == rear:
            print(-1)
        else:
            print(queue[rear])

from sys import stdin


N = int(stdin.readline())
queue = []
q_size = 0


for _ in range(N):
    current = stdin.readline().strip()

    if current[1] == 'u':   # push X
        command, num = current.split()
        queue.append(num)
        q_size += 1
    elif current[1] == 'o': # pop
        print(queue.pop(0)) if q_size else print(-1)
        if q_size:
            q_size -= 1
    elif current[1] == 'i': # size
        print(q_size)
    elif current[1] == 'm': # empty
        print(0) if q_size else print(1)
    elif current[1] == 'r': # front
        print(queue[0]) if q_size else print(-1)
    else:                   # back
        print(queue[-1]) if q_size else print(-1)

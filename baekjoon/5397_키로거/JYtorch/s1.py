import sys
sys.stdin = open('input.txt')

def solution():
    stack1 = []
    stack2 = []

    for input_data in log:
        # print(stack1, stack2)
        if input_data == '<':
            if stack1: stack2.append(stack1.pop())
        elif input_data == '>':
            if stack2: stack1.append(stack2.pop())
        elif input_data == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(input_data)
    return ''.join(stack1 + list(reversed(stack2)))
T = int(input())
for tc in range(1, T + 1):
    log = list(input())
    # print(log)
    print(solution())
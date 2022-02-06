import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
M = int(input())
infos = []
for _ in range(M):
    send, receive, box = map(int, input().split())
    infos.append((send, receive, box))
infos.sort(key=lambda x:  x[1])  # 도착 순으로 정리

capacity = [C]*N
total = 0
for send, receive, box in infos:
    minimum = C  # 트럭용량
    for i in range(send, receive):
        # 수송 구간을 순회하면서
        if minimum > min(capacity[i], box):
            minimum = min(capacity[i], box)
    for i in range(send, receive):
        capacity[i] -= minimum
    total += minimum

print(total)
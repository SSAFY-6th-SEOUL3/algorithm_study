# Linked List

linked list는 데이터를 노드 형태로 저장

### 1. 링크드리스트의 기본 구조

노드는 `데이터`와 `다음 노드를 가리키는 포인터`를 담은 구조로 이루어짐

![img](https://blog.kakaocdn.net/dn/bQVxyX/btq58YRuYMz/1Y7J1cfqh1GydKFeKT23i0/img.png)

- Node: 데이터와 다음 데이터를 가리키는 주소(포인터)로 이루어짐
- Pointer: 각 노드에서 다음 데이터를 가리키는 주소값을 가짐
- Head: 링크드리스트에서 가장 시작점인 데이터
- Tail: 링크드리스트에서 가장 마지막 데이터
- Next = None : 다음 데이터가 없을 경우 포인터의 주소값은 None 또는 Null



### 2. 링크드리스트의 장단점

##### 장점

- 배열은 미리 데이터 공간을 할당해야 하지만 링크드리스트는 미리 할당할 필요 없음. (유동적으로 데이터 추가, 삭제 가능)
- 링크드리스트 수정시 시간복잡도 O(1)을 가짐.(항상 일정한 속도)

##### 단점

- 다음 데이터를 연결하기 위해선 별도의 주소 공간을 가져야 함.(저장 공간 효율이 높지 않음)
- 배열은 인덱스를 통해 데이터에 접근하므로 시간복잡도 O(1)을 갖지만 링크드리스트의 경우 O(n)을 갖짐.(연결된 정보를 찾기 위해 주소를 확인하고 다음 데이터를 탐색하는 시간이 있기 때문에 접근 속도가 느림)
- 중간 데이터 삭제시, 앞뒤 데이터를 연결하고 재구성하는 코드가 추가로 필요하다.



### 3. 링크드리스트의 파이썬 코드

##### 1) class를 이용하여 Node 생성

```python
#Node 정의
class Node:
    def __init__(self, data, next=None):  #data 만 입력시 next 초기값은 None이다.
        self.data = data #다음 데이터 주소 초기값 = None
        self.next = next


#Node 생성해보기(data = 1)
node1 = Node(1)

#Node의 값과 포인터 출력하기
print(node1.data)
print(node1.next)


출처: https://ybworld.tistory.com/85 [투손플레이스]
```

##### 2) Node 연결하기

```python
#Node1 생성해보기
node1 = Node(1)
#Node2 생성해보기
node2 = Node(3)
#Node 연결하기
node1.next = node2
#가장 맨 앞 Node를 알기 위해 head 지정
head = node1

#node1을 통해 연결한 결과 확인(밑에 2줄은 동일한 결과를 가리킨다)
print(node1.next.data)
print(node2.data)


출처: https://ybworld.tistory.com/85 [투손플레이스]
```



### 4. 링크드리스트 대표 문제

- 2021 카카오 채용연계형 인턴십 - [표 편집](https://programmers.co.kr/learn/courses/30/lessons/81303)

#### s1.py

```python
class Node():
    def __init__(self):
        self.removed = False
        self.next = None
        self.prev = None

        def solution(n, k, cmd):
    node_arr = [Node() for _ in range(n)]
    removed_list = []
    for i in range(1, n):
        node_arr[i - 1].next = node_arr[i]
        node_arr[i].prev = node_arr[i - 1]
        
    curr = node_arr[k]
    for i in range(len(cmd)):
        command = cmd[i]
        if command[0] == "U":
            cnt = int(command[2:])
            for _ in range(cnt):
                if curr.prev:
                    curr = curr.prev
        elif command[0] == "D":
            cnt = int(command[2:])
            for _ in range(cnt):
                if curr.next:
                    curr = curr.next
        elif command[0] == "C":
            removed_list.append(curr)
            curr.removed = True
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            if curr.next:
                curr = curr.next
            else:
                curr = curr.prev
        else:
            node = removed_list.pop()
            node.removed = False
            if node.prev:
                node.prev.next = node
            if node.next:
                node.next.prev = node
    answer = ""
    for i in range(n):
        if node_arr[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer
```


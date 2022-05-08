### Heap과 Binary Heap

- 힙이란? 몇 가지 특수한 속성을 가진 트리

- **힙 속성 "노드의 값이 그 자식 노드의 값보다 작거나 같다. 또는 크거나 같다"**

- 트리의 높이 h > 0일때 모든 노드들은 h 또는 h-1 레벨에 있어야 한다. (완전이진트리)

- 즉, 힙은 완전 이진 트리여야 한다.

- 힙의 종류

  - **Min Heap (최소힙) : 노드의 값이 자식 노드의 값보다 작거나 같아야한다.**
  - **Max Heap (최대힙) : 노드의 값이 자식 노드의 값보다 크거나 같아야 한다.**

- **힙은 다 이진 힙 @@@ Binary Heap @@@** 각 노드는 최대 두 개의 자식노드를 가진다.

  - 힙은 내부를 '배열'로 만든다.

- 노드의 부모

  - **i번째 위치의 노드에서 부모 노드는 (i-1)/2 을 버림한 위치에 있어야 한다. (floor)**

  - ```c
    int Parent(struct Heap *h, int i) {
    	if (i <= 0 || i >= h -> count)
    			return -1;
      return (i-1)/2;
    }
    ```

  - 시간 복잡도 O(1)

- 노드의 자식

  - **노드의 부모가 i번째일 때, 자식은 (2*i) + 1, (2*i) + 2**



### 파이썬 구현 - heapq 모듈로 구현

```
"""
heapq 모듈은 최소 우선순위 큐를 지원한다.
key와 data를 push 하면 key가 작은 원소가 앞에 위치한다.
key가 높은 원소부터 꺼내고 싶으면 뒤집자.
루트 인덱스는 0이다.
"""
from heapq import heappush, heappop

h = []
heappush(h, (4, 'kim'))
heappush(h, (3, 'lee'))
heappush(h, (1, 'jong'))
heappush(h, (2, 'seo'))

print(h[0])
print(h[-1])

res = []
while h:
    res.append(heappop(h))
print(res[::-1])

```


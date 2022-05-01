# 4.25 ~ 5.1

## 알고리즘 강의

### [1주차](https://www.youtube.com/watch?v=-WhatBV8ELc) - 문자열, 누적합(prefix cum), 구현



#### 시간복잡도

- 시간복잡도 -  "문제를 해결하는 데 걸리는 시간과 입력의 함수 관계"

##### 자료구조에서의 시간복잡도

![img](https://mblogthumb-phinf.pstatic.net/MjAyMTEyMTlfMjQ2/MDAxNjM5ODc4ODU0MjQw.QBoa_QNtJE2wW3bl-kgF5-u_-6UB1nwYWjayKiFvCpAg.4h_9rHx2GEgZnYFTvOtlSGZpnu0rLKWcS0PQsaPWwz8g.PNG.jhc9639/1.PNG?type=w800)

##### STL에서의 시간 복잡도

```c++
sort()  :nlogn
lower_bound(), upper_bound(): nlogn
find() : n 
fill() : n 
unique(): n
```

#### 공간복잡도

알고리즘 문제에서 "배열의 경우 1000만은 안된다" => 1000만 이상의 배열을 만들어야 하는 경우 다른 방법(ex.이분탐색) 떠올리기







### 누적합

![img](https://mblogthumb-phinf.pstatic.net/MjAyMTEyMTlfMjM1/MDAxNjM5ODk4MTMzMjE3.OO03PJJIHQU0ECVADJgWcsDew8L12kXbTFtqlKspvbwg.wTcop7GC4BmrgvXCdF4u-Ga6JjPOR6RyOvHqx49fPIwg.PNG.jhc9639/%EC%A7%91%ED%95%84%EA%B7%B8%EB%A6%BC.png?type=w800)

- 누적합: 미리 요소들의 합을 저장해 두는 누적된 수의 합





**예시문제**

승철이는 뇌를 잃어버렸다. 학교에 갔더니 선생님이 자연수로 이루어진  N개의 카드를 주며 M개의 질문을 던진다. 그 질문은 나열한 카드 중 A번째부터 B번째까지의 합을 구하는 것이다. 뇌를 잃어버렸기 때문에 승철이는 이 문제를 풀 수 없다. 문제를 풀 수 있는 프로그램을 작성해보자.  

**입력**

수의 개수 N, 합을 구해야 하는 횟수 M, 그 이후 N개의 수가 주어진다. 수는 100 이하의 자연수. 그 이후 M개의 줄에는 합을 구해야 하는 구간 A, B가 주어진다. 

**출력**

M개의 줄에 A부터 B까지의 합을 구하라. 

**범위**

1 <= N <= 100,000

1 <= M <= 100,000

1 <= A <= B <= N  

**예제입력**

```
8 3 1 2 3 4 5 6 7 8 1 4 1 5 3 5
```

**에제출력**

```
10 15 12
```



##### S1

```c++
#include<bits/stdc++.h>
using namespace std;   
typedef long long ll;     
int a[100004], b, c, psum[100004], n ,m;
int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> n >> m; 
	for(int i = 1; i <= n; i++){
		cin >> a[i];
		psum[i] = psum[i - 1] + a[i]; 
	}
	for(int i = 0 ; i < m; i++){
		cin >> b >> c; 
		cout << psum[c] - psum[b - 1] << "\n";
	} 
	return 0;
}
```

- 누적합 만들기

  - 누적합을 만들 때는 반드시 "1번째 요소부터" 만드는 것이 좋음

    ```c++
    psum[i] = psum[i - 1] + a[i]; 
    ```

-  ```c++
   psum[c] - psum[b - 1]
   ```

  

## [2주차](https://www.youtube.com/watch?v=RFSAJrN0gCM) - 그래프이론, dfs, bfs, 트리순회

https://m.blog.naver.com/jhc9639/222289089015





# 문제 풀이

##### [[카카오 인턴] 키패드 누르기](https://programmers.co.kr/learn/courses/30/lessons/67256)

```python
def solution(numbers, hand):
    answer = ''
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#'],
    ]
    pos = {
        2: (0, 1),
        5: (1, 1),
        8: (2, 1),
        0: (3, 1),
    }
    left_pos = (3, 0)
    right_pos = (3, 2)
    for number in numbers:
        if number in set([1, 4, 7]):
            answer += "L"
            if number == 1:
                left_pos = (0, 0)
            elif number == 4:
                left_pos = (1, 0)
            else:
                left_pos = (2, 0)
        if number in set([3, 6, 9]):
            answer += "R"
            if number == 3:
                right_pos = (0, 2)
            elif number == 6:
                right_pos = (1, 2)
            else:
                right_pos = (2, 2)
        if number in set([2, 5, 8, 0]):
            r, c = pos[number]
            lr, lc = left_pos[0], left_pos[1]
            rr, rc = right_pos[0], right_pos[1]
            
            if abs(r - lr) + abs(c - lc) > abs(r - rr) + abs(c - rc):
                answer += "R"
                right_pos = (r, c)
            elif abs(r - lr) + abs(c - lc) < abs(r - rr) + abs(c - rc):
                answer += "L"
                left_pos = (r, c)
            else:
                if hand == "right":
                    answer += "R"
                    right_pos = (r, c)
                else:
                    answer += "L"
                    left_pos = (r, c)
    return answer
```



##### [[카카오 인턴] 수식 최대화](https://programmers.co.kr/learn/courses/30/lessons/67257)

```python
from itertools import permutations

def solution(expression):
    answer = 0
    opers_list = list(permutations(['+', '-', '*'], 3))

    expression_list = []

    tmp = ""
    for i in range(len(expression)):
        string = expression[i]
        if string in set("0123456789"):
            tmp += string
        else:
            expression_list.append(int(tmp))
            expression_list.append(string)
            tmp = ""
    if tmp:
        expression_list.append(int(tmp))

    exp_list = expression_list[:]
    max_value = 0
    for opers in opers_list:
        for oper in opers:
            while True:
                if oper not in set(exp_list):
                    break
                idx = exp_list.index(oper)

                if oper == '+':
                    res = exp_list[idx - 1] + exp_list[idx + 1]

                elif oper == '-':
                    res = exp_list[idx - 1] - exp_list[idx + 1]

                else:
                    res = exp_list[idx - 1] * exp_list[idx + 1]

                exp_list.pop(idx - 1)
                exp_list.pop(idx - 1)
                exp_list.pop(idx - 1)
                exp_list.insert(idx - 1, res)
        max_value = max(max_value, abs(exp_list[0]))
        exp_list = expression_list[:]
    return max_value
```



##### [[카카오 인턴] 보석 쇼핑](https://programmers.co.kr/learn/courses/30/lessons/67258) - 해결 중
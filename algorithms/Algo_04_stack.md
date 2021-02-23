# Stack

- 물건을 쌓아올리듯 자료를 쌓아 올린 형태의 자료구조.

- 선형구조를 가짐
- 



## 구현

### 자료구조

- 마지막에 삽입한 자료를 가장 먼저 꺼냄. 선입후출. or 후출선입.
- python에서는 리스트를 사용할 수 있다.
- 마지막에 삽입된 원소의 위치를 top이라고 부른다.



### 연산

- 삽입 : 저장소에 자료를 저장. 보통 push라 부른다
- 삭제: 저장소에서 자료를 꺼낸다. 역순으로꺼냄. 보통 pop이라 칭함.
- 스택이 공백일까? isEmpty
- top에 있는 item을 반환 : peek



#### pop의 알고리즘

```python
def pop():
    if len(a) == 0:
        # underflow
        return
    if len(a) > 0:
        return pop(len(a)-1)
```



#### push 알고리즘

1. ```python
   def push(item):
       s.append(item)
   ```



#### 총합

```python
class Stack:
    def __init__(self):
        self.top = []

    def __len__(self):
        return len(self.top)

    def __str__(self):
        return str(self.top[::1])

    def push(self, item):
        return self.top.append(item)

    def pop(self):
        if not self.isempty():
            return self.top.pop(-1)
        else:
            print('Stack underflow')
            exit()

    def isempty(self):
        return len(self.top) == 0

    def clear(self):
        self.top = []

    def iscontain(self, item):
        return item in self.top

    def peek(self):
        if not self.isempty():
            return self.top[-1]
        else:
            print('Stack underflow')
            exit()
```







## 스택의 응용

1. 괄호검사
   - 조건
     - 왼쪽괄호 개수와 오른쪽 괄호의 개수가 같아야한다.
     - 같은 괄호에서 왼쪽괄호는 오른쪽괄호보다 먼저 나와ㅏ야한다.
     - 괄호사이에는 포함관계만 존재한다.



2. Function call
   - 프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리.
   - 함수호출이 발생하면 호출한 함수 수행에 필요한 지역변수/매개변수 및 수행후 복귀할 주소 등의 정보를 스택프레임에 저장하여 시스템 스택에 삽입
   - 실행이 끝나면 시스템 스택의 top원소를 pop하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
   - 전체 프로그램 수행이 종료되면 시스템 스택은 공백으로 됨.



## 재귀호출

- 자기 자신을 호출하여 순환수행
- 프로그램 크기 down 
- base case가 없으면 계속 호출하다가 메모리터짐.
- base case까지 내려갔다가 원래값까지 복귀하여 값을 구함.

![image-20210222142650230](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210222142650230.png)

arr= [0]* n 을만들고 다음과 같이 코드를 짜면 호출횟수를 알 수 있다.



### Memoization

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록하여 전체적인 실행속도를 빠르게하는 기술.

- 메모리에 넣기'to put in memory'라는 의미.

- ```python
  def fibo1(n):
      global memo
      if n >= 2 and len(memo) <= n:
          memo.append(fibo1(n-1) + fibo1(n-2))
      return memo(n)
  
  memo = [0, 1]
  ```





## DFS

- 응용교재가 보기 편함.

### 그래프 표현

- 인접행렬
  - 배열의 배열
  - V(정점의 수) x V 크기의 2차원배열을 이용해서 간선정보를 저장0

### 인접행렬

- 두정점을 연결하는 간선의 유무를 행렬로 표현
- 간선이 있으면 1 없으면 0
  - ex) 1 2/ 1 4 / 2 3 등을 주면
    - 무향그래프의 경우 (1,2) (2,1) 이 1
    - (1,4) (4,1) (2,3) (3,2) = 1 나머지는 0

### 인접리스트

- 리스트로 행렬을 표시한것.

- 각 정점에 대한 인접정점을 순차적으로 표현

- arr = [[]*정점의 수]

  - ```python
    arr [j] = [i] 이면 정점 j에 연결된 정점이 i이다. 라는것을 표현.
    ```



### 재귀함수로 구현

![image-20210222174101733](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210222174101733.png)

for w in 인접v 이기 때문에 위 스택이 쌓인게 일 다하면 pop되고 다음 for문을 돌림!
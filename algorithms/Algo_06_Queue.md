# Queue



## 특성

- 큐의 뒤에서는 삽입만하고 큐의 앞에서는 삭메나 이루어지는 구조.
  - 선입선출구조 (FIFO)
  - ex) 서비스 대기열.
  - ![image-20210303090827802](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210303090827802.png)
    - Front                                                           																																		Rear



## 연산

- enQueue(item): Queue의 뒤쪽에 원소를 삽입
- deQueue() : Queue의 앞쪽에서 원소를 삭제하고 반환
- createQueue(): 공백상태의 Queue를 생성
- isEmpty(): Queue가 공백상태인지 확인
  - Front = Rear일 때 공백상태라 할 수 있다.
- isFull(): Queue가 포화상태인지 확인
- Qpeek(): Queue의 앞쪽에서 원소를 삭제없이 반환하는 연산.
  - Q[Front +1]



### 과정 (example)

1. 공백 Queue생성 : createQueue();
2. 원소 A 삽입: enQueue(A);
3. 원소 B 삽입: enQueue(B);
4. 원소 반환/삭제: deQueue()
5. 원소 C삽입: enQueue(C);
6. 원소 반환/삭제 : deQueue()
7. 원소반환/삭제: deQueue()



## 선형큐

### 선형큐 구현

- 1차원 배열을 이용한 큐

  - 큐의 크기 = 배열의 크기
  - front = 마지막에 꺼내진 원소의 인덱스
  - rear = 저장된 마지막 원소의 인덱스

- 상태표현

  - 초기상태 : front = rear = -1
  - 공백상태 : front = rear
  - 포화상태 : rear = n-1 (n:배열의 크기, n-1: 배열의 마지막인덱스)

- 1. 초기 공백 큐 생성

  - 크기가 n인 1차원 배열 생성
  - front와 rear를 -1로 초기화.

- 2. 삽입: enQueue(item)

  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해서

  - 1) rear값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련

  - 2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장

  - ```python
    def enQueue(item) :
        global rear
        rear = rear + 1
        Q[rear] = item
    ```

- 3. 삭제 : deQueue()

  - 가장 앞에 있는 원소를 삭제하기 위해서

  - front 값을 하나 증가시켜 Queue에 남아있는 첫번째 원소로 이동

  - 새로운 첫번째 원소를 리턴함으로써 삭제와 동일한 기능을 함.

  - ```python
    def deQueue():
        global front
        if isEmpty(): print('Queue is empty')
        else:
        	front = front +1
        	return Q[front]
    ```

- 4. 공백 및 포화 검사: isEmpty(), isFull()

  - 공백상태 : front = rear

  - 포화상태 : rear = n-1

  - ```python
    def isEmpty():
        return front == rear
    def isFull():
        return rear == len(Q) - 1
    ```

- 5. 검색: Qpeek()

  - 가장 앞에있는 원소를 검색하여 반환

  - 현재 front의 한자리 뒤에 있는 원소, 즉 큐의 첫번째 원소를 '삭제하지않고' 반환.

  - ```python
        def Qpeek():
            global front
            if isEmpty(): print('Queue is empty')
            else:
            	return Q[front+1]
    ```



### 선형큐 이용시 문제점

- 잘못된 포화상태 인식
  - 선형큐를 이용하여 삽입/삭제를 반복할 경우 배열의 앞부분의 활용할 수 있는 공간이 있음에도 불구하고 
    rear=n-1인 상태로 인식하여 삽입을 수행하지않게됨.
  - 해결방법 1.
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 저하.
  - 해결방법 2.
    - 1차원 배열을 사용하되 논리적으로 배열의 처음과 끝이 연결되어 원형형태의 큐를 이룬다고 가정하고 사용.



## 원형큐



- 원형 큐:![image-20210303100744643](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210303100744643.png)
  - 초기 공백상태 : front = rear = 0
  - index의 순환
    - front와 rear의 위치가 배열의 마지막인덱스인 n-1을 가리킨 후 논리적 순환을 통해 배열의 처음 인덱스인 0으로 이동
    - 나머지연산자 %(mod)를 이용
  - front 변수: 공백상태와 포화상태의 구분을 쉽게 하기위해 front가 있는 자리는 항상 빈자리로 고정해둠.
                        (공백이 없으면 꽉차도 front=rear이고 공백일때도 front=rear이기때문)
  - ![image-20210303101522035](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210303101522035.png)





### 구현

- 공백상태 및 포화상태검사:

  - 공백 : front = rear
  - 포화 : (rear+1) % n  = front

- 삽입:

  - rear = (rear+1) % len(cQ)
  - cQ[rear] = item

- 삭제 : deQueue(), delete()

  - 가장 앞에있는 원소를 삭제

  - ```python
    def deQueue():
        global front
        if isEmpty():
            print("Queue_Empty")
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]
    ```



## 연결큐

### 구조

#### 단순 연결리스트를 이용한 큐

- 원소 : 단순 연결 리스트의 노드
- 원소 순서: 노드의 연결순서(링크로 연결되어있음)
- front : 첫번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크.

#### 상태표현

- 초기상태 : front =rear= None
- 공백상태 : front = rear = None



## 우선순위 큐

- 특성
  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO 순서가아니라 우선순위가 높은순서대로 out
- 적용분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케쥴링
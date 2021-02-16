# List_2



## 2차 배열

- 다차원 list는 차원에 따라 index 선언
- 2차원 list는 세로길이(행의 개수), 가로길이(열의개수)를 필요로 함.

### 입력

```python
N, M = mpa(int, input().split())

arr = []

for i in range (N):
    arr.append(list(map(int, input().split())))
    
'''
3 4
1 2 3 4 
5 6 7 8
9 10 11 12 입력
'''
or

arr = [list(map(int, input().split())) for i in range(N)]
```



### 배열 순회

n * m 배열의 모든 원소를 전부 조사하는 방법

i행 j열의 좌표

- 행 우선순회

```python
for i in range(len(array)):
	for j in range(len(array[i])):
        Array[i][j]  # 필요한 연산 수행
```

- 열 우선순회

```python
for j in range(len(array[i])):
	for j in range(len(array)):
        Array[i][j]  # 필요한 연산 수행
```



### 전치행렬

- 열과 행을 바꾸는 것

```python
for i in range(len(array)):
	for j in range(len(array[i])):
        if i < j:
            array[i][j], array[j][i] = array[j][i], array[i][j]  # nxn 행렬에서만 사용가능.
```

- 



## 부분집합 생성

- 완전검색 기법으로 부분집합 합문제를 풀기위해서는 모든 부분집합을 생성해서 계산 후 검증해야됨.

### 비트연산자

- & (앤퍼센트 연산자): 비트단위로 and 연산을 한다.
- |(파이프, 버티컬바):비트 단위로 OR 연산을 한다.
- ">>"(right shift): 피연산자의 비트열을 오른쪽으로 이동시킨다.
- "<<"(left shift): 피연산자의 비트열을 왼쪽으로 이동시킨다.
  - 1 << n : 2^n 1을 n번 left shift하는것.



![image-20210215165237077](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210215165237077.png)

- arr를 생성할때 list안에 내포하는 형태로 해야 각각 다른객체로 인식하기 때문에
  4번 line의 명령이 복사가 안됨.





## 바이너리 search

### 순차검색

- 일렬로 되어있는 자료를 순서대로 검색하는 방법.
- 구현은 쉽지만 수가 많은경우 비효율적.

#### 정렬되어있지않은경우

- 순차검색의 평균 비교회수 = 1/n * n*(n+1)/2 = (n+1) / 2
  - 첫번째 원소는 1번, 2번째원소는 2번...
  - 시간복잡도: O(n)



#### 정렬이 되어있는 경우

- 정렬이 되어있으므로 검색실패를 반환하는 경우 평균 비교회수가 반으로 줄어듦
  - 시간 복잡도 : O(n)



### Binary search

- 자료의 가운데 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 이진 검색을 하기 위해서는 ***자료가 정렬된 상태***여야 한다.
  - 재귀함수를 이용한 search

  - ```python
    def binarysearch(a, low, high, key):
        if low > high:
            return False
        else:
            middle = (low+high) // 2
            if key == a[middle] :
                return True
            elif key < a[middle] :
                return binarysearch(a, low, middle-1, key)
            elif key  > a[middle] :
                return binarysearch(a, middle+1, high, key)
    ```

  - 

## 셀렉션 알고리즘

- 저장된 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 한다.



### pseudo code

- k번째로 작은 원소를 찾는 알고리즘.
  - 1번부터 k번째까지 작은 원소를 배열앞쪽으로 이동시키고 배열의 k번째를 반환
  - K가 비교적 작을 때 유용하며 O(kn)의 수행시간을 필요로함.
  - ![image-20210215152423142](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210215152423142.png)

## 선택정렬

- 

- ```python
  def selectionSort(a):
      for i in range(0, len(a)-1):
          minidx = i
          for j in range(i+1, len(a)):
              if a[minidx] > a[j]:
                  minidx = j
          a[i], a[min] = a[min], a[i]  # idx위치만 갱신하다가 마지막에 바꾸기
      print('기준자리 :', i, arr)  # 어떻게 변하고있는지 확인.
  ```

- 



## 실습 1, 2
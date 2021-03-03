# Stack2



## 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 계산식의 값을 계산할 수 있다.

  - 1. 중위표기법의 표기를 스택을 이용하여 후위표기법으로 변경
    
    - 후위표기법 : AB+
    - 중위표기법: A+B
    - ex)
      - ((A*B) - (C/D))
      - ((AB)*(CD)/)-
      - AB*CD/-
      - 
- ![image-20210224090840797](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210224090840797.png)
    
  - 스택 밖의 왼쪽 괄호는 우선순위가 가장 높으며, 스택안의 왼쪽 괄호는 우선 순위가 가장낮다.

ex2)

```python
5+(7+4/2*(5-4+5)*1/2 +1)


stack 
print 5 7 4 2 / 5 4 - 5 + *1 *2/ + 1 + +
```





2. 후위표기법의 수식을 스택을 이용하여 계산
   1. 피 연산자를 만나면 스택에 push
   2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고
   3. 연산결과를 다시 스택에 push
   4. 수식이 끝나면 스택을 pop하여 출력.

## 백트래킹

- 도중에 막히면 되돌아가서 다시 해를 찾아가는 기법이다.
- 최적화문제/ 결정문제를 해결하는데 사용
  - 결정문제 : 문제의 조건을 만족하는 해가 존재하는 지에 대한 여부를 답하는 문제.
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지않다고 한다.
  반대로 가능성이있으면 유망하다고 한다.



### 절차

1. 상태공간트리의 깊이우선검색을 실시
2. 각 노드가 유망한지 검사
3. 유망하지않은 노드를 검색결과에서 제외.



### 구현

- 일반 백트래킹 알고리즘

```python
def checknode(v):  # node
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for u in each child of v:
                checknode(u)
```



### 부분집합_재귀

모든 부분집합을 power set.

- 원소의 개수가 n이면 부분집합의 개수는 2^n
- for문을 이용하면 n번 for문을 이용하여 부분집합을 생성했었음.

![image-20210224110324876](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210224110324876.png)

```python
def backtrack(a, start, end):
    global Max_candidates
    c = [0] * Max_candidates
    
    if start == end:
        solution(a,start)  # 답이면 원하는 작업을 한다.
    else:
        start += 1 (or -= 1)
        ncandidates = construct_candidates(a, start, end, c)
        
```





```python
N = 3
arr = [1, 2, 3,]  # 우리가 활용할 데이터
sel = [0] * N  # 내가 해당 원소를 뽑았는지 체크하는 리스트
def powerset(idx):
    if idx == N:
        print(sel)
        return   # 밑에과정을 수행하려면 return을 시켜야돼!(idx=2인 상태)
    # idx자리의 원소를 뽑고가는 경우
    sel[idx] = 1
    powerset(idx+1)
	# idx자리의 원소를 안뽑고 가는 경우
    sel[idx] = 0
    powerset(idx +1)
    
powerset(0)
# 1 1 1 (idx=2로 return) 1 1 0 (return,시스템 스택상에서 idx=2일때가 다 끝났으므로 idx=1인 상태로 return)
# 1 0 1 (idx=2) 1 0 0 \n 0 1 1 \n 0 1 0 \n 0 0 1 \n 0 0 0
```



### 순열

#### 순열_재귀

ex)

```python
arr = [1, 2, 3]
N = 3
sel = [0] * N  # 결과들이 저장될 리스트
check = [0] * N  # 해당원소를 사용했는지에 대한 체크

def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]  # 값을 써라
                check[i] = 1  # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0  # 다음 반복문을 쓰기위해서 원상복구
        
perm(0)
```

![image-20210224142221980](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210224142221980.png)



#### 순열_비트

```python
arr = [1, 2, 3]
N = 3
sel = [0] * N  # 결과들이 저장될 리스트
# check는 10진수 정수
def perm(idx, check):
    if check == (1<<N)-1:
        print(sel)
        return
    for j in range(N):
        if check & (1<<j): continue
        sel[idx] = arr[j]  # 값을 써라
        perm(idx+1, check|(1<<j))  # 원상복구 안해도됨. 
        
# Check의 변화가 핵심이야.       
        
perm(0)
```



![image-20210224144636063](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210224144636063.png)

#### 순열_스왑

```python
arr = [1, 2, 3]
N = 3

def perm(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            # arr 내에서 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            # 원래 arr로 만들기.
            arr[idx], arr[i] = arr[idx], arr[i]
```





## 분할정복

- 설계 전략
  1. 분할 (Divide): 해결할 문제를 여러개의 작은 부분으로 나눈다.
  2. 정복 (Conquer) : 나눈 문제를 각각 해결한다.
  3. 통합 (Combine): 필요하다면 해결된 대답을 모은다.



ex) pow함수

```python
def recursive_pow(x ,n):
    if n == 1 : return x
    if n % 2 == 0:
        y = recursive_pow(x, n//2)
        return y * y
    else:
        y = recursive_pow(x, (n-1)//2)
        return y * y * x
```

- 2^300000을 계산하는데 있어서 pow(2, 300000)은 30만번 계산
- 그에비해 recursive_pow 함수의 시간복잡도는 log2n



## 퀵정렬

- 기준아이템 중심으로 좌우를 나누고 마지막에 붙임.



```python
def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)
        

def partition (a, begin, end):  # 호어파티션
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L<R): L+= 1
        while(a[R]>= a[pivot] and L<R): R -= 1
        if L < R:
            if L== pivot : 
                pivot = R
            a[L], a[R] = a[R], a[L]
   a[pivot], a[R]= a[R], a[pivot]
   return R
```



- 평균 시간복잡도는 O(nlogn)이다.


# 제어문(Control Statement)

- 특정 상황에서 코드를 선택적으로 분기하거나
- 동일한 코드를 계속해서 실행해야 하는경우 사용
- 조건문 / 반복문



## 조건문

- if 문은반드시 참/거짓(True, False)을 판단할 수 있는 조건과 함께 사용.



### if 조건문의 구성

- 문법 

  - ```python
    if <expression>:
        <code>
    else:
        <code>
    ```

- elif 복수 조건

  - 두개이상의 조건을 활용 할 경우 elif를 사용
  - flow가 진행될수록 elif expression의 조건식의 범위가 커져야함
    - 왜냐하면 그 전의 if expression이 False가 되야 다음 expression이 True/False를 검사할 수 있음.

- 조건 표현식

  - True_value if <조건식> else false_value



## 반복문(Loop statement)

- While, For



### While

- While 문은 조건식이 참(True)인 경우 반복적으로 코드를 실행하다.

- 문법

  - ``` python
    while <조건식>:
        <코드블럭>
    ```

  - 코드블럭에는 **반드시** 조건식을 finish될 수 있게 만드는 코드가 필요함.

    - 조건식을 False로 만들지 못할 경우 무한으로 코드블럭을 반복하게됨



### for

- for 문은 시퀀스 (string, tuple, list, range)나 다른 순회가능한 객체(iterable) 의 요소를 순회한다.

- 문법

  - ```python
    for <변수> in <iterable data>:
        <반복해서 실행할 코드블럭>
    ```

#### enumerate

- enumerate(iterable, start=())
  - enumerate(iterable)는 (idx, value) 값을 포함하는 튜플을 반환



## 반복제어 

### Break

- for, while문을 강제종료시키고 빠져나옴
  - (해당 코드블럭의 가장 바깥을 멈춤.)
  - (else문도 실행되지 않음)



## continue

**Continue이후의 코드를 수행시키지않고** 다음요소부터 계속하여 반복수행


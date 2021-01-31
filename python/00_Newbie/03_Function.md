# 함수(Function)

- 특정 기능을 하는 하는 코드의 묶음
  - 가독성 up
  - 재활용 EZ
  - 유지보수 EZ : 코드를 기능별로 묶어버리니까
- return이 없으면 None을 반환
- (print로 하는건 보여주는 것일뿐 결과값은 None임)



## 함수의 Output

### return

- 함수는 항상 반환되는 값이 있음
- but 오직 한 개의 객체만 반환

- return a, b 같이 여러 개를 써놓으면?
  - (a, b)같이 tuple로 묶어서 반환됨.



## 함수의 Input

### Parameter and argument



#### Parameter

입력을 받아 내부에서 활용할 **변수**

함수의 정의부분에서 볼 수 있다.

#### argument

전달되는 인자

실제 '입력 값'

##### 	위치인자

- 함수의 parameter가 2개이상일 때 인자가 어느 parameter에 대입될지 위치로 판단함.

- ex)

  - ```python
    def cylinder(r, h):
        return r**2 * 3.14 * h
    ```

  - ```python
    cylinder(2, 5) = 62.80
    cylinder(5, 2) = 157.0
    ```

##### 기본 인자 값

- parameter에 기본 값을 함수에 설정 해놓으면, input(함수 괄호 안의 값)을 넣지 않더라도 parameter에 설정해 놓은 기본인자를 활용하여 함수를 실행한다.

- ***기본인자 값을 가지는 변수 다음에 기본값이 없는 인자를 사용 불가능***
  - 만약 기본인자 값을 가지는 변수 다음에 오면
    - SyntaxError: Non-default argument follows default argument라는 문법에러가 발생

##### 키워드 인자

- 직접 변수의 이름으로 특정 인자를 전달 가능
- ***키워드 인자를 활용 한 후 위치인자를 활용 불가능***
  - 만약 이 경우 SyntaxError: positional arguments follows keyword argument라는 에러가 발생



## 정해지지 않은 여러 인자의 처리

### 가변 인자 리스트

- parameter 마지막에 *args를 추가해서 사용
  - 가변 인자 리스트는 tuple 형태로 처리가 됨
  - 가변 인자 리스트 이후에는 키워드인자만 올 수 있음



### 가변 키워드 인자

- parameter 마지막에 **kwarg를 추가해서 사용
- key = 'value' 형태로 키워드 인자를 추가.
- kwargs.items() :dict_items([(keyword, value), (keyword, value)])
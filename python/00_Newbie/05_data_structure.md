# 함수(Function)_part.2

## 함수와 스코프

### scope

- 함수는 코드 내부에 공간(scope)를 형성합니다. 함수로 생성됭 공간은 local scope, 그 외 공간은 global scope로 구분됩니다

### 이름 검색

- 이름(식별자) 들은 이름공간에 저장되어있음

- 이름을 찾는 순서는 L->E->G->B
  - Local
  - Enclosed
  - Global
  - Built-in

### 변수의 Lifecycle

- Built in scope:
  - 파이썬이 실행된 이후로부터 영원히 유지
- Global scope: 모듈이 호출된 시점 이후 혹은 이름선언 이후부터 인터프리터가 끝날 때까지 유지
- Local scope: 함수가 호출될 때 생성되고 종료되면 소멸





## 재귀함수

- 함수의 반환값에 자기 자신을 호출.

- ex

  - ```python
    def factorial(n):
        if n == 1:
            # base case...
            return 1
        else:
            return n * factorial(n-1)
    ```

- base case(= 최대 재귀 깊이) 를 설정하지 않을 경우 무한히 호출함. =>RecursionError 발생.

- 반복문으로도 만들 수 있음



### 반복문과 차이

1. 변수 사용을 줄일 수 있다.
2. 재귀함수의 호출 횟수가 많아지는 경우도 있으므로 반복문이 더 계산시간이 짧은 경우도 있다.
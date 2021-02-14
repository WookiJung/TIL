# 파이썬 모듈

## Numpy

### 넘파이 배열

- 메서드

  - numpy.array

- 산술연산

  - array끼리 같은 index에서 사칙연산이 이루어짐
  - 스칼라값으로 계산할 시 ***브로드캐스트*** 가 적용되어 넘파이 배열의 원소별로 한번씩 수행됨.
    - 브로드 캐스트
      - 앞의 배열과 맞춰 뒤의 배열 or 스칼라값이 확대되는것.

- N차원 배열

  - 리스트안에 리스트 여러개로 구성됨

    - ex) A=numpy.array([[3, 2], [1, 1]])

    - ```python
      print(A)
      [[3 2],
       [1 1]]
      ```

    - ```python
      B = numpy.array([10, 5])
      
      A * B =
      array([[30, 10],
             [10, 5]])
      ```

      - B가 1X2 배열에서 2X2배열로 자동으로 확대된 후 연산이 이루어짐.
      - .flatten() 메서드로 1차원 배열로 전환 가능

## matplotlib

### pyplot

- Numpy.arrange 메서드로 x축 데이터 생성

- 변수 y에는 필요한 함수 할당.

- ```python
  import numpy as np
  import matplotlib.pyplot as plt
  
  ====
  
  plt.plot(x, y)
  plt.show()
   # 위와같은 방식으로 graph를 만들 수 있음.
  ```

- 여러개를 그릴 때

- ```python
  plt.plot(x, y1, label="")
  plt.plot(x, y2, label="", linestyle="")
  ```

​	
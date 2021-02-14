# 퍼셉트론



## 정의

- 신경망의 기원이 되는 알고리즘.
- 다수의 신호를 입력으로 받아 하나의 신호를 출력함
  - 출력값은 0과 1 두가지 값을 가질 수 있음.
  - 입력신호가 뉴런에 보내질 때 가중치가 곱해져서 전달.
  - 보내진 신호의 총합이 정해진 한계를 넘어설 때만 1을 출력
  - 이 한계를 Theta, 임계값(역치)이라 한다.
  - 편향(bias) = -theta 값으로 뉴런이 얼마나 쉽게 활성화되는지를 나타낸다. 
    편향의 값이 클수록 쉽게 활성화된다.



## 단순 논리 회로

### AND 게이트

- x1, x2가 모두 1일때 1을 출력

### NAND게이트

- Not AND게이트
- x1, x2가 1일때만 0을출력

### OR게이트

- X1이나 x2 둘중 1가지가 1일때 1을 출력



## 구현

w1, w2는 가중치, theta 는 임계값.

아래 구현은 example임.

### AND 게이트

```python
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = w1x1 + w2x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
    # 가중치와 편향을 도입하여 numpy 배열로 식을 구현하면
def AND_2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
```

### NAND 게이트

```python
def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = w1x1 + w2x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
    # 가중치와 편향을 도입하여 numpy 배열로 식을 구현하면
def NAND_2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
```

### OR 게이트

```python
def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = w1x1 + w2x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
    # 가중치와 편향을 도입하여 numpy 배열로 식을 구현하면
def NAND_2(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
```

- 각각의 w1, w2, theta값은 수동적으로 설정해야됨.





### 한계점

- 단일 퍼셉트론으로 비선형 영역을 구현하기 어려움.

- 다층퍼셉트론을 통해 해결


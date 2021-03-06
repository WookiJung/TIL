# Greedy Algorithm

## 탐욕 알고리즘

- 최적 해를 구하는 데 사용되는 근시안적인 방법
  - 여러 경우중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적으로 해답에 도달
  - 각 선택의 시점에서 이루어지는 결정은 지역적으로 최적이지만, 그것들을 계속 수집하여 최종적인 해답을 만들었다고 하여 최적이라는 보장 X



### 수행과정

- 해 선택
  - 각 부분문제에서 최적해를 구한 뒤 이를 solution set(부분 해 집합)에 추가
- 실행 가능성 검사
  - 새로운 부분 해 집합이 실행가능한지를 확인
  - 문제의 제약조건을 위반하지않는지 검사
- 해 검사
  - 새로운 부분 해 집합이 문제의 solution이 되는지 확인
  - 전체 solution이 완성되지 않았다면 해선택부터 다시함.



```
num = 456789  # Baby Gin 확인할 6자리 수
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
	c[num % 10] += 1
	num //= 10
 
i = 0
tri = run = 0
while i < 10:
	if c[i] >= 3:  # triplete 조사 후 데이터 삭제
		c[i] -= 3
		tri += 1
		continue;
	if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 삭제
		c[i] -= 1
		c[i + 1] -= 1
		c[i + 2] -= 1
		run += 1
		continue
	i += 1
if run + tri == 2:
	print('Baby-Gin')
```



### 해답을 못 찾을 때

-  입력 받은 숫자를 정렬한 후, 앞 뒤 3자리씩 끊어서 run 및 triplete을 확인하는 방법을 고려할때
  - {1, 1, 2, 2, 3, 3}일 경우 Baby-gin 확인이 불가능.


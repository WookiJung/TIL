# Exhaustive Search

## 완전검색(exhaustive search)

- 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
  - Brute-force / Generate-and-test 기법이라고도 불림
  - 모든경우의수 테스트 후 최종해법 도출
  - 경우의수가 상대적으로 작을 떄 유용
  - 수행속도 slow, 정확도 good
    - So, 완전검색으로 해답을 도출한 후, 성능개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직함.

## Baby-gin game

### Rule

6자리 숫자를 입력받아 Baby-gin 여부 찾기 

0~9중 6개의 숫자를 중복가능으로 뽑아서

3개의 숫자가 같을 때 triplete/ 3개의 숫자가 연속될 때 run

6개의 숫자가 전부 triplete/run으로 구성되면 baby-gin

### 순열

- 서로 다른 n개 중 r개를 택하는 순열은 nPr
- nPr = n * (n - 1) * (n - 2) ... *(n-r+1) 
- nPn = n!



#### {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

```
for i1 in range(1, 4):
	for i2 in range(1, 4):
		if i2 != i1 :
			for i3 in range(1, 4):
				if i3 != i1 and i3 != i2:
					print(i1, i2, i3)
```



#### 코드 만들어보기

1. 고려할 수 있는 모든 경우의 수 생성

2. 해답 test
3. 










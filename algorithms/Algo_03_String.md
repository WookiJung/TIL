# String



## 문자열

- 영어가 대소문자 합쳐서 52가지이므로 2^6(64) 비트로 표현할 수 있다.
- 지역따라 같은문자를 다른문자료 표현
  - 혼동을 피하기 위해 표준안을 만듦 (ASCII(American Standard code for Information Interchange) code)
  - 표준안에는 7bit 인코딩으로 숫자,특수문자를 포함한 95개 출력가능한 문자로 이루어져있음.



### 유니코드

- 국가간 코드가 매칭이 안되서 발생
- Character set으로 재분류됨.
  - UCS-2, UCS-4인지 구분해야되는 불편함이 있으므로 적당한 외부 코딩을 통해 해석
  - 유니코드 인코딩 : UTF-8, UTF-16, UTF-32(Unicode trasformation format- (min bite))



### 파이썬에서 문자열 처리

- Char type이 없다
- 텍스트 데이터의 취급방법이 동일함.

- immutable, iterable



```python
line = '안녕하세요'

print(line.replace('세', '시'))  # 안녕하시오
print(line)  # 안녕하세요

line = line.replace('세', '시')
print(line)  # 안녕하시오

line = line.split('하')
print(line) = ['안녕', '시오']

```



#### 문자열 뒤집기

- 자기문자열에서 뒤집기
  - 자기문자열을 이용한 경우에는 임시 변수가 필요.
- 새로운 문자열에서 뒤집은 문자열을 배치



- 문자열을 숫자로 바꾸기
- ![image-20210217112106379](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210217112106379.png)

## 패턴매칭

- KMP
  - 불일치가 발생한 텍스트 문자열 앞부분에 어떤문자가 있는지 미리알고있으므로 앞부분에 대하여 다시비교X

### 보이어무어

- 패턴 내 동일한 글자가 없을때 :

- 찾고싶은 Pattern의 오른쪽에서 왼쪽으로 비교.
  - 오른쪽 끝에있는 문자가 불일치
    - and 이 문자가 패턴 내에서 존재하지 않는 경우. skip거리는 pattern 길이
    - and 이문자가 패턴내에 존재할 경우 - 패턴에서 일치하는 문자를 찾아서 맞추고 나머지 검사.



### Brute force

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴내의 문자들을 일일이 비교하는 방식
  - ![image-20210217140848310](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210217140848310.png)



### 알고리즘 비교

- 찾고자 하는 패턴의 길이를 m, 총 문자열 길이를 n이라 할때
  - Brute force : 수행시간 O(m*n)
  - KMP 알고리즘: 수행시간 BigTheta(n) (평균)
  - 보이어-무어 알고리즘 :최선의 경우 O(n)
    - 다 보지 않아도 됨
    - 패턴의 오른쪽부터 비교
    - 최악의 경우 O(mn)

## 문자열 암호화 (참고)

- #### 시저 암호

  - 시저 암호에서는 평문에서 사용되고있는 알파벳을 일정한 문자 수만큼 [평행이동] 시킴으로써 암호화.

- #### 단일치환암호

  - 1:1로 치환, key sheet가 필요함.

- #### Bit열의 암호화

  - 배타적 논리합 연산 사용.
  - 동일 key로 XOR 두번돌리면 원문으로 됨.

## 문자열 압축

- 저장소의 크기를 줄이며 정확한 정보를 저장
- run length encoding 알고리즘
  - 같은값이 몇번 반복되는가를 나타냄
  - 반복이없으면 손해봄

## 실습 1, 2

- 문자열 뒤집기
- itoa
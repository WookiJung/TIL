# Data Structure

## 문자열

### 조회 / 탐색

1. .find(x)
   - x의 **첫번째 위치**를 반환합니다. 없으면 -1을 반환합니다.
2. .index(x)
   - x의 **첫번째 위치**를 반환합니다. 없으면 오류가 발생



### 값 변경

1. .replace(old, new[, count])

   - Old string을 New string으로 바꿈 
   - count.default =all, count를 적으면 적은 갯수만큼 바꿈.

2. .strip([chars])

   - 특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip)

   - 지정하지않으면 글자 좌우의 공백을 제거.

     - ex) 

     - ```python
       oh = '    oh! '
       
       oh.strip() = 'oh!'
       oh.lstrip() = 'oh! '
       oh.rstrip() = '    oh!'
       
       
       escape = '\r\t\n'
       escape.strip() = ''
       ```

3. .split()

   - 문자열을 특정한 단위로 나누어 ***리스트로 반환***합니다.

4. 'separator' .join(iterable)

   - Iterable 컨테이너의 요소들을 separator 구분자로 합친 문자열로 반환.

   - seperator default값은 ''(아무것도 없는 것)

   - ex)

   - ```python
     list_x = ['t', 'e', 's', 't']
     ```

   - ```python
     ''.join(list_x) = 'test'
     ```



### 문자열 변형

1. .capitalize(), .title(), .upper()
   - .capitalize() : 앞글자를 대문자로
   - .title() : 어포스트로피나 공백 이후를 대문자로 만들어 반환
   - .upper() : 모두 대문자로 만들어 반환
2.  .lower(), .swapcase()
   - lower() : 모두 소문자로 바꾸어 반환
   - swapcase() : 대소문자 변경하여 반환
3. is ~ : true/false 확인



## 리스트

### 탐색 및 정렬

1. .index(x)
   - x값을 찾아 해당 index를 반환
2. .count(x)
   - x값의 개수
3. .sort()
   - 정렬, 보통 내림차순
   - returnX, 원본 리스트를 바꿈
4. .reverse()
   - 순서를 거꾸로 뒤집음

### 값 추가 및 삭제

1. .append(x)

   - 리스트의 마지막 index에 x를 추가함

   

2. .extend(iterable)

   - 리스트에 iterable 값을 붙일 수 있음

   - iterable의 요소를 각각 분해해서 넣음.

     - ex

     - ```python
       cafe=['starbucks', 'coffeebean']
       cafe.extend(['이디야']) -> '이디야'라는 값이 추가
       cafe.extend('ediya') -> 'e', 'd', 'i', 'y', 'a'를 추가.
       ```

3. .insert(i, x)

   - index[i] 에 'x'를 추가
   - i에 -1을 넣을경우 마지막 바로전ㅇ ㅔ추가
   - 길이를 넘어서는 index는 리스트 마지막에 x추가

4. .remove(x)

   - 리스트에서 값이 x인 첫번째 요소를 삭제 

5. .pop(i)

   - index(i)에 있는 값을 삭제하고 그 **항목을 반환**
   - i가 지정되지 않은 경우 마지막 항목을 삭제하고 반환

6. .clear()

   - 빈 리스트로 만듦



### List Comprehension

1. [Expression for 변수 in iterable] == list(expression for 변수 in iterable)

   - ex) cubic_list

   - ```python
     cubic_list = []
     for number in range(0, 11):
         cubic_list.append(number ** 3)
     cubic_list = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
     
     = [number ** 3 for number in range(0, 11)]
     ```

2. 조건문 까지 추가하려면

   - [expression if 변수 in iterable if 조건식]

   - [expression if 조건식 else 식 for 변수 in iterable]

     - ```python
       ['홀수' if i%2 == 1 else '짝수' for i in range(1, 11)]
       ```

     - 조건식을 뒤에쓰면 else 사용 불가.(SyntaxError 발생)



## 데이터 구조에 적용 가능한 Built-in Function

- list, dict, set, str, bytes, tuple, range
  - map()
    - map(function, iterable) :순회가능한 데이터구조의 모든 요소에 function을 적용 시킨 후 그 결과를 돌려준다.
    - return은 map_object 형태로 나오므로 list 등으로 바꿔줘야 볼 수 있음.
  - filter()
    - filter(function, iterable): 순회가능한 데이터구조의 모든요소에서 function을 적용시킨 후 그 결과가 True인 것들만 걸러내 반환됨
    - filter_object로 반환되므로 list 등으로 바꿔줘야 볼 수 있음.
  - zip()
    - 복수의 iterable객체를 모아줌.
    - iterable 객체는 index가 같은 것들만 반환됨.
    - index가 같은것 끼리 tuple로 묶어서 zip_object로 반환.



## 세트

- 변경 가능, unordered, iterable



1. .add(element)
   - element를 세트에 추가함
2. .update(*others)
   - 인자 = iterable한 자료
   - string -> char 형태로 분해해서 추가
3. .remove(element)
   - element를 세트에서 삭제. 없으면 KeyError가 발생.
4. .discard(element)
   - elem를 세트에서 삭제하고 없어도 에러발생 X
5. .pop()
   - 임의의 원소를 제거해 반환.



## 딕셔너리 (dictionary)

- 변경 가능, unordered, iterable
- key: value 페어의 자료구조.



1. .get(key[, default])
   - key를 통해 value를 가져옵니다
   - default = None (dictionary에 key가 없을 시 출력되는 값)
2. .pop(key[, default])
   - key가 딕셔너리에 있으면 제거하고 그 값을 돌려주고
   - 없으면 default를 반환
   - default가 없는 상태에서 key가 dictionary가 없으면 KeyError 발생.
3. .update()
   - 값을 제공하는 key,value를 추가
   - key가 있는경우 value를 덮어씀



#### Dictionary key, value에 대한 접근

```python
grades = {'john' : 80, 'eric':90, 'justin': 90}

for student in grades:
    print(student)  # john, eric, justin
    
for key, value in grades.items():
    print((key,value))  # dict_items([('john', 80), ('eric', 90), ('justin', 90)])


```



1. {키 : 값 for 요소 in iterable}
   - dict({키: 값 for 요소 in iterable})
2. Dictionary comprehension
   - {키: 값 for 요소 in iterable if 조건식}
   - {키 : 값 if 조건식 else 값 for 요소 in iterable}


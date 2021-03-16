# Django

## Model

- 웹 어플리케이션의 데이터를 구조화 및 조작하기 위한 도구

### Database

- 체계화된 데이터의 모임
- Query: 데이터를 조회하기 위한 명령어, 조건에맞는 데이터를 추출하거나 조작하는 명령어

- Schema(스키마) : 데이터베이스의 구조와 제약조건(자료의 구조, 표현방법, 관계)에 관련한 전반적인 명세를 기술한 것.
- Table(테이블): 열(column/field)과 행의 모델을 사용해 조직된 데이터요소들의 집합.
  - 열(column, field): 각 열에는 고유한 데이터형식이 있다.
  - 행(row, record): 테이블에 데이터는 행에 저장됨.
  - PK(기본키): 각 행의 고유값으로 Primary Key로 불림. ***반드시설정***하여야하며, 데이터베이스관리및 관계 설정시 주요하게 활용.



### ORM

- Object Relational Mapping 은 객체지향 프로그래밍 언어를 사용하여 호환되지않는 유형(django <-> SQL)의 시스템간에 데이터를 변환하는 기술이다.
- 가상 객체 데이터베이스를 만들어 사용

- 객체로 DB를 조작하기 위해 사용하는 기술!

#### 장점

SQL을 잘 알지못해도 조작가능

객체지향적 접근으로 인한 **높은 생산성**

#### 단점

ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음.





### Models.py

- models.py에 스키마(데이터 베이스의 구조)를 짜줌.

```python
class Article(models.Model):
    title = models.CharField(max_length=5)  
    # title, content 등 class 변수는 table에서 필드(db입장에서는 column)
    # CharField는 길이가 제한이 존재하는 경우 사용.
    # max_length = @@ 제목의 길이를 제한을 둚.
    content = models.TextField()
```

- 우리는 column 만드는 것에만 집중해!
- 이러한 models.py를 만든 후 매니저에게 makemigrations -> migrate하면
  - ![image-20210310101118584](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210310101118584.png)
  - 위와 같은 앱이름_클래스이름을 가진 Table이 생성됨.
  - id는 자동으로 생성
  - title / content와 같은 column들은 우리가 작성해준 클래스 변수로 만들어짐.

- ![image-20210310102236085](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210310102236085.png)
  - 작성시간도 알려고 해 : models.DateTimeField(auto_now_add=True)
    - Auto_now_add : automatically set the field to now when the object is first created. useful for '작성시간'
  - 수정 시간도..:models.DateTimeField(auto_now=True)
    - auto_now : automatically set the field to now every time the object is saved. Useful for '수정시간'
- ***새로 설계도를 작성했으면?***
  - ***매니저 불러서 makemigrations -> migrate*** 

### Migrations

- django가 model에 생긴 변화를 반영하는 방법.
- Migration 실행 및 DB스키마를 다루기 위한 몇가지 명령어
  - ***makemigrations***
  - ***migrate***
  - sqlmigrate 
  - showmigrations

#### Command

- makemigrations : 변경한 모델에 기반한 새로운 마이그레이션(like 설계도)을 만들 때 사용.
- migrate:
  - 마이그레이션을 DB에 반영하기 위해 사용
  - 설계도를 실제 DB에 반영
  - DB의 스키마와 모델의 변경사항을 동기화시킴.
- sqlmigrate: : 마이그레이션에 대한 SQL 구문을 보기위해 사용
  - python manage.py sqlmigrate '앱 이름' '번호'
- showmigrations: 마이그레이션상태를 확인하기위해 사용
  - migrate가 제대로 작동했는지 여부를 확인 가능
  - X 는 체크의 표시임.



## Database API

- DB API
  - DB를 조작하기 위한 도구
  - Model을 만들면 django가 객체들을 만들고 읽고 수정할 수 있는 database-abstract API를 자동으로 만듦

### 구문

![image-20210310104813279](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210310104813279.png)

- Manager = class와 querySet API를 연결
- Queryset:
  - 데이터베이스로부터 전달받은 객체목록
  - 데이터베이스로부터 조회,필터, 정렬등을 수행 가능.



## CRUD

- Create, Read, Update, Delete를 묶어서 일컫는 말.
- all() -> Query set 전부를 읽어옴
  - []로 표기됨 -> 우리가 python에서 리스트처럼 조작 가능



### C, Create

- 인스턴스를 생성하고 그안에 변수를 넣어주는방법
- `Classname.objects.create(변수 설정)` 해주는 방법.



### R, Read

- Queryset을 주는 메서드
  - ex) all() - 모든데이터를 줌.
- Queryset을 주지않는 메서드
  - ex) get(pk='#')



#### all() 

- 모든 instance를 가져옴



#### get(pk='#')

- pk값에 해당하는 인스턴스를 가져옴.

- 만약에 `get(columnname = '#')`를 했을 때 해당 열에 똑같은 내용이 2번있다면?
  - multipleobjectsreturned 

- 만약에 없는값을 인자로 쓴다면?
  - 없다고 뜸
- 위와 같은 특징을 가지고있기 때문에 unique and not null일 경우에만 사용.



#### Filter(column name = '#')

- 하나의 Query set 안에 해당하는 row들을 가져옴.



#### Field lookups

- 조회시 특정 조건을 적용시키기 위해서 사용
- filter, exclude, get에 사용

- `field__lookuptype = value`라는 형식의 구문으로 표현.



### U, Update

1. instance 지정
   - ex) article = Article.objects.get(pk=1)
2. instance 변수 갱신
   - ex) article.title = 'byebye'
3. ***세이브***



### D, Delete

1. instance 지정
2. instance.delete()



- 삭제된 pk는 재사용되지않는게 default



## Admin site

### Automatic admin interface

관리자가 활용하기 위한 페이지

record 생성여부확인에 매우 유용

직접 record 삽입가능



### 등록

앱의 admin.py를 킨다.

```python
from .models import '클래스이름'

admin.site.register('클래스이름')

```



### 표시

```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('보이게 하고싶은 컨텐츠들')  # 튜플이나 리스트로 작성.
```


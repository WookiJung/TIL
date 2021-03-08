# Django

## Django란?

Static web - 미리 저장된 정적 파일을 제공.

Dynamic web - 사용자가 요청을 보냈을 때 추가적인 서버side가 일해서 새로운걸 제공.

이러한 Dynamic web side를 만들어주는 프레임워크가 Django다.



- Python web Framework
  - Web Framework : 웹페이지를 개발하면서 겪는 어려움을 줄이는 용도로 만드는 것.
  - 기본적인 구조나 필요한 코드를 제공

- 모델-뷰-컨트롤러: 소프트웨어 공학에서 사용되는 소프트웨어 디자인 패턴이다.
  - 사용자 인터페이스와 비지니스 로직을 분리

- MTV 패턴
  - Model : 데이터베이스 관리
  - Template : 레이아웃(화면)
  - View : 중심 컨트롤러



![image-20210308091910447](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210308091910447.png)



```python
__init__.py : 이 폴더가 패키지임을 표시해주는 python file. 건들지마.
```

- articles 폴더(startapp으로 생성된 폴더)
  - Models.py - 
  - Admin.py - 
  - Views.py - 



## Settings.py

- installed apps - order가 기본적으로는 정해져 있음.
  1. Local apps
  2. 3rd-party apps
  3. django apps

순으로 작성하는 것이 좋음.

- language_code : 'ko-kr'
- Time_zone : 'Asia/Seoul'



## urls.py

- project folder안에 있음.
- urlpatterns = [path(arg1, arg2)]
  - arg 1= 'blabla/'  
    - 반드시 end slash 작성해야됨.
  - from app import views => views의 함수를 전부 사용 가능하도록 모듈을 불러오는것.
  - arg2 = 보여줄 페이지.

## views.py

1. views의 함수를 작성할때 첫번째인자는 반드시 Request가 들어온다.
2. render함수의 첫번째 인자도 반드시 request 2번째 인자는 탬플릿의 경로이다. 'templates' 까지는 인식하므로 그밑의 주소만 써주면된다.
3. 세번째 인자는 context에 필요한 인자. 딕셔너리형태로 넣어줘야한다.



```python
def greetings(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {'info': info
               'foods': foods,
    }  # key,value값의 이름은 맞추는게 일반적이다.
    return render(request, 'greetings.html', context)
```





## Template

app안에 ***templates***라는 이름의 폴더로 만들어서 그 안에 html 생성.

- App_name/templates/가 default.
- 다른곳에도 templates폴더가 있다는 것을 인식하기위해서는 project 폴더의 settings.py를 열어봐
- 

### Template란?

데이터 표현을 제어하는 도구이자 표현에 관련된 로직

DTL(template language)

- 조건,반복,변수치환,필터 등의 기능을 제공
- 프로그래밍 구조가 비슷하지만 python코드로 실행되는 것은 아님
- 단순히 Python이 HTML에 포함된것이아님.
  - 프로그래밍 로직이 아닌 프레젠테이션을 표현하기 위한것.

### DTL(Django Template Language)

#### Variable

view함수에서 받아온 인자들은

- {{ }}형태로 사용 index or key는 '.'를 통해서 접근

- 위 예제의 경우

  - ```python
    안녕하세요 {{ info.name }} 입니다
    저는 과일 중에서 {{ foods }}를 좋아합니다.
    그 중 {{ foods.0 }}를 가장좋아합니다.
    ```

  - 와 같이 작성.  {{}} 안에 변수명을 사용할 때 ***중괄호와 붙여쓰지않는걸 권장***

#### Filter

- {{ variable|filter }}
- 표시한 변수를 수정할 때 사용
- 약 60개의 built-in template filter 제공.



#### Tag

- {% tag %}
- 24개의 built-in tags 존재
- 일부 tag는 닫는태그도 존재



#### Comments

- {# --- #}
- 여러줄 주석은 {% comment %} {% endcomment %}



### Template Inheritance

- 코드의 재사용성에 초점을 맞춤

- 사이트의 모든 공통요소를 포함하고

- 하위 템플릿이 재정의할수있는 블록을 정의하는 기본 'skeleton'템플릿을 만들 수 있음.

  - ```python
    {% extends '부모템플릿의 경로'%}
    자식 템플릿이 부모템플릿을 확장한다는것을 알림
    반드시 최상단에 작성!
    
    {% block 'name' %}
    하위 템플릿에서 override할 수 있는 블록을 정의
    하위템플릿에서 채우면 부모 템플릿의 'name' 블럭에 자동으로 채워짐
    ```



### Template system

- 표현과 로직(view)를 분리
  - 표현을 제어하는 도구.
- 중복을 배제
  - 상속을 통해서 한곳에 저장하기 쉽게하여 중복코드를 없애는것!





## models.py



## HTML form

- 웹에서 사용자정보를 입력하는 여러방식을 제공하고 사용자로부터 할당된 데이터를 서버러 전송하는 역할을 담당.
- 핵심 속성
  - action: 입력데이터가 전송될 URL을 지정
  - method :입력 데이터 전달방식 지정.



### Input element

- 핵심속성
  - name
  - 중복 가능, 양식을 제출했을 때 name이라는 이름에 설정된값을 넘겨서 값을 가져올 수 있음
  - 주요 용도는 get/post방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 ?key = value & key=value 형태로 전달.



### HTTP request method - get

- 서버로부터 정보를 조회하는데 사용
- 데이터를 가져올 때 사용
- 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송.
- HTML 파일 한장을 받는데 사용하는 방식.



## URL

발송자 운항관리자로서의 URL

web application은 URL을 통한 클라이언트의 요청에서부터 시작.

### APP URL mapping

- 프로젝트의 urls.py에 다 작성하면 복잡해짐
- 각 앱에 urls.py를 만들어 관리하는것이 필요.
- 앱에 새로 urls.py를 만들고 기존 url의 admin제외 가져오기.
- 기존 pjt URL은 어느 앱의 URL로 보낼지 결정하는 역할로 바뀜.





### Variable routing

- 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것.

- urls.py에서

- ```python
  path('hello/<str:name>/', views.hello)
  
  와 같은 방식으로 만들면
  name에 적은 것이 변수로 들어간다.
  
  +@
  str:은 기본값이기때문에 <name>으로 작성해도 무관하다.
  ```

- 

### Naming URL pattern

![image-20210308154333795](C:\Users\wkjung\AppData\Roaming\Typora\typora-user-images\image-20210308154333795.png)
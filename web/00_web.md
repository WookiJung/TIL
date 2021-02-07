# WEB

## HTML

- Hyper Text Markup Language의 준말
  - 선형적인 텍스트가아닌 비선형적으로 이루어진 텍스트.
  - 웹페이지 맨앞에 들어가는 HTTP는?
    - Hyper Text Transfer Protocol
- Markup language
  - tag등을 이용해 문서나 데이터의 구조를 명시하는 언어.
  - Markup language는 화면을 보고 내용 작성하는 거 아님!
- Open Graph Protocol
  - HTML 문서의 메타데이터를 통해 문서의 정보를 전달.
  - 메타 데이터는 보통 html문서의 head에 들어가있음



### Element

- Tag와 내용으로 구성되어있다.
- h1, div, header, nav, aside, section, article, footer 등 block 요소
- span, a , br, img, strong(b), em(i), 등 inline 요소
  - strong tag나 b tag나 똑같은 작용을하지만 문서 상에서 tag의 의미를 알기 쉬운 Semantic tag인 strong tag를 쓰는편



### Attribute

- 태그 별로 사용할 수 있는 속성이 다름
- ex) href
  - <a href="#"></a>
  - 와같이 key = "value" 형식으로 attribute 구현
- 공통속성
  - `id, class`
  - `hidden`
  - `lang` : 언어 태그. BCP47에 정의된 형식의 언어태그 중 1개. (언어하위태그 - 활자 or 지역하위태그 형식)
  - `style` : font size, font weight, color, background-color 등..
  - `tabidex` : 요소가 포커스 가능함을 나타내며 주로 tab키를 사용하는 연속적인 키보드 탐색에서 어느 순서에 위치할 지 지정.
    - tabindex="-1" : 연속 키보드탐색으로는 접근 불가능, javascript나 마우스클릭 으로 포커스 가능.
    - tabindex="0" : default. 보통 양의정수값은 안쓰는게 좋음. tabindex가 1이 가장먼저나오지만 사용자의 페이지 탐색과 조작에 방해될수 있음.
  - `title`





## 단축키

### ! + tab

- 기본적인 틀에대한 자동완성.



### tag에 들어갈 문자 쓰고 + tab키

- opening+closing 자동완성



### ctrl + enter

어느 곳에 있든 다음줄 처음시작으로 갈 수 있음



### ctrl + shift + enter

어느곳에있든 윗줄 처음시작으로 엔터 가능



### alt + 방향키

줄 자체로 위 아래가 바뀜



## Tag

### h1 ~ h6

- heading



### ol ,ul

- ordered list, unordered list

- 내부에 들여쓰기하고 <li> </li>로 list에 들어갈 내용을 씀.



### 새로 추가된 시맨틱 태그 

#### section

- 같은 의미의 구역을 나눌 때 사용
- 섹션의 제목으로 사용되는 제목 컨텐츠는 상하구조를 갖지않음 (레이아웃에 영향 X)
- 신문기사와 같은 배포형은 section이 아닌 article을 사용
- section에 스타일을 지정하려면 div 사용 권장



#### article

- 문서 내 독립적인 글, 블로그 글이나 뉴스본문 등 구성하는 섹션을 나타냄.
- header, footer와 같은 하나의 페이지 형식으로 구현가능. 페이지 안에서 article 요소가 반복되어도 ok
- 단순한 삽입구를 위해 사용하는 것은 X
- article 요소가 중첩될 경우 중첩된 요소는 서로 상호관련이 있어야함.



#### aside

- 섹션의 내용과 관련은 있으나 분리되어도 문제없는 섹션으로 주로 사이드바 형태로 표현.
- 추가적인 설명을 할 때 사용하는 태그.



#### header

- 머릿말 태그.
- 소개, 또는 문서에 대한 탐색요소의 그룹을 지정



#### footer

- 페이지 하단부의 저작권 정보나 서비스 제공자 정보 등을 제공하는 부분을 의미



#### menu

- 페이지 내 기능을 하는 버튼/링크의 모음을 나타냄.
  - type은 context, toolbar, list 3가지의 type이 있고 기본값은 list



#### nav

- 외부 페이지로 연결되는 링크의 모음을 나타냅니다.


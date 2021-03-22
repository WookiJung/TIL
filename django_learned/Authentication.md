# Authentication System

- Authentication : 인증
- Authorization : 권한
- django에서는 어느정도 결합되어있어서 authentication system이라고 함.
- 기본적으로 built-in-form 제공

## Login & Logout

django는 *세션*과 *미들웨어*를 사용하여 인증시스템을 request객체에 연결

- 이를통해 사용자를 나타내는 모든 요청에 request.user를 제공
- 로그인하지 않은 경우 AnonymousUser클래스의 인스턴스로 설정되며, 
  로그인된 경우 User클래스의 인스턴스로 설정됨.



### Login

- Session을 create하는 로직과 같음.
- login()
  - 세션에 연결하려는 인증된 사용자가 있는 경우 login()함수로 로그인 진행
  - Request객체와 User객체를 통해 로그인 진행.
  - Session framework를 통해 ID를 세션에 저장



### Logout

- 세션 delete
- logout()
  - 현재요청에 대한 DB의 세션데이터를 삭제하고 클라이언트 쿠키에서도 sessionid를 삭제



### HTTP

- 웹에서 이루어지는 데이터 교환의 기초
- 클라이언트 - 서버 프로토콜
- 요청 : 클라이언트에 의해 전송되는 메세지
- 응답: 서버에서 응답으로 전송되는 메세지
- 특징
  - 비연결지향:응답후 접속 끊음
  - 무상태(stateless):서버-클라이언트 통신이 끝나면 상태를 저장하지 않음.



### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터조각
- 브라우저(클라이언트)는 쿠키를 key-value형태로 저장.
  - 동일한 서버에 재 요청시 저장된 쿠키를 함께 전송.
- ***목적***
  - 세션관리 : 상태를 만들기 위해서!,
    - 로그인 유지
    - 아이디 자동완성
    - 팝업체크
    - 장바구니 등
  - 개인화
    - 사용자 선호, 테마등의 세팅
  - 트래킹
    - 사용자 행동을 기록 및 분석하는 용도
- 라이프타임
  - Session cookie
    - 세션 종료시 삭제
    - 브라우저는 현재 세션이 종료되는 시기를 정의
    - 일부는 다시시작할때 세션복원해서 계속 지속
  - Permanent cookie
    - Expires속성에 지정된 날짜 혹은 max-age속성에 지정된 기간이 지나면 삭제
- 쿠키 확인
  - 개발자도구 - application -storage : Cookie, local storage 등 확인가능.



### 세션

- 사이트와 특정 브라우저 사이의 "state"를 유지시키는 것.
- 서버가 쿠키에 session_id를 넣어 발급.  클라는 해당쿠키를 이용해 서버에 session id를 전달
- django는 session id를 포함하는 쿠키를 사용해 브라우저가 연결된 세션을 알아냄.
  (session 정보는 django가 가지고있음. key를 주면 맞는 방을 찾아주는것.)
- 주로 로그인 상태 유지에 사용.



Cookie&Session

- 쿠키는 클라이언트 로컬에 파일로 저장
- Session은 서버에 저장. 이때 session ID는 쿠키에 저장



### is_authenticated

- user class의 속성

- user에서는 true, 비로그인시 False.

- 권한에대해서는 판단 X

- html문서에서

- ```django
  {% if request.user.is_authenticated %}
  	로그아웃 페이지, update페이지 버튼 등등
  {% endif %}
  ```





### login required decorator

- 사용자가 로그인했는지 확인하느 view를 위한 데코레이터
- 로그인 되지않은 사용자는 settings.login_url에 설정된 경로로 redirect.
- Default = ''/accounts/login/"
- '?next=' 
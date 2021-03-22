# Error messages

1. No such table ~
   - migrate가 안되어있다는 것이야!
   - 그럼 DB에 아무것도없어서 저장할 location도 없음!



2. 



## Http Status Code

1. 400 : Bad request : 잘못된 문법으로 인해 서버가 요청을 이해불가능함.
2. 401 : Unauthorized : 인증 안함.
3. 403 : Forbidden
   - 보안통과못함
   - csrf_token없을때
   - admin만 접근할 수 있을때 등등
4. 404: page not found
   - 페이지가 없을때
5. 405: mehtod not allowed
   - method가 잘못되었을 때. 
6. 500 : Internal Server Error
   - 서버가 처리방법을 모르는 상황이 발생.
7. 502 : Bad gateway
   - 서버가 요청을 처리하는데 필요한 응답을 얻기위해 게이트웨이로 작업하는 동안 잘못된 응답을 수신했음을 의미합니다.
8. 503 : Serviece Unavailable
   - 서버가 요청을 처리할 준비가안됨. 일반적으로 작동이 일시적으로 중단되었거나 과부하가 걸렸을때 해당메세지를 출력.
## WSGI vs ASGI
### WSGI
: 웹 서버와 애플리케이션 사이의 통신을 위한 주요 파이썬 표준 인터페이스
- 웹 프레임워크와 웹 서버 간의 통신을 가능하게 해주는 프로토콜
- 동기식 코드만 지원
- HTTP 스타일로 request/response 형식에 고정
    - 단일 처리만 가능한 동기 호출 방식
    - 긴 대기시간 가지는 HTTP 연결에는 부적합
<br>
[Client] → [Web Server] → [WSGI] → [Python Web App]
<br>

- WSGI를 지원하는 웹 서버가 python 앱을 실행할 때 WSGI 인터페이스를 통해 실행하는 구조


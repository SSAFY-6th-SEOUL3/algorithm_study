# 5.8 Network



### www.google.com에 접속할 때 일어나는 일

1. URL을 브라우저 주소창에 입력한다.
2. DNS 서버에서 도메인 주소에 대응하는 IP 주소가 캐시 데이터로 있는지 확인한다.
   - 브라우저 캐시, OS 캐시, 라우터 캐시, ISP 캐시 순으로 확인한다.
3. 캐시 데이터가 없으면, DNS 서버에 DNS 쿼리를 보내 IP 주소를 알아낸다.
   - 도메인의 각 레벨을 담당하는 네임 서버가 있다.
   - 각 네임 서버는 바로 하위 레벨의 네임 서버 주소밖에 모른다.
   - ex. `artsandculture.google.com`의 IP 주소를 알아낸다고 하자.
     - 루트 서버로 쿼리 보냄 => com 네임 서버 주소 반환
     - com 네임 서버로 쿼리 보냄 => google.com 네임 서버 주소 반환
     - google.com 네임 서버로 쿼리 보냄 => artsandculture.google.com 네임 서버 주소 반환
     - 원하는 IP 주소를 찾았으니 캐시를 갱신하고, IP 주소를 브라우저에 전달한다.
4. 브라우저는 받은 IP주소로 서버와 연결을 수립한다.
   - 일반적으로 TCP를 사용해서 연결한다. TCP의 경우 3 way handshaking을 사용한다.

5. 연결이 완료되면 브라우저가 서버에 GET 요청을 보낸다.

6. 서버는 요청을 처리하고 응답을 브라우저에 보낸다. 응답의 message body 부분에 html 문서가 포함될 것이다.
7. 브라우저는 받은 HTML 문서를 렌더링해서 사용자에게 보여준다.



### GET vs POST

**GET**은 주로 데이터를 조회할 때 사용한다.

**POST**는 주로 리소스를 생성하거나, 요청 데이터를 처리할 때 사용한다.

**GET**은 서버에 전달할 데이터를 URL의 쿼리 스트링에 전달한다. 따라서 header 부분이 데이터를 저장한다. 따라서 전달값이 노출되기 때문에 비밀번호 같은 정보를 GET 요청으로 전달하면 안 된다. 

**POST**는 메시지 바디를 통해 서버에 요청 데이터를 전달한다. (PUT, PATCH도) 따라서 전달값이 사용자에게 직접 노출되지 않는다.

**GET**은 멱등성을 보장한다. 몇 번을 호출해도 결과가 같다는 뜻이다. 반면 **POST**는 멱등성을 보장하지 않는다. 



### POST vs PUT

**POST**는 리소스를 생성할 때 사용된다. 클라이언트가 리소스 위치를 모르는 상태에서 요청을 하면, 서버가 리소스 위치를 결정한다.

**PUT**는 리소스를 생성하거나 수정할 때 사용된다. 클라이언트가 리소스 위치를 직접 URI에 지정해서 요청을 보낸다. 해당 위치에 리소스가 없으면 생성하고, 있으면 대체한다.

**POST**는 멱등성을 보장하지 않지만, **PUT**은 멱등성을 보장한다.



### 401 vs 403

**401 Unauthorized**는 인증(authentication)이 되지 않음을 의미한다. (인증 X) 

- ex. 로그인 안 됨

**403 Forbidden**은 권한이 없어 요청이 거부되었음을 의미한다. (인가 X)

- ex. 일반 유저가 관리자 페이지에 접속함.



### HTTP vs HTTPS

- **HTTP**는 하이퍼텍스트를 교환하기 위한 프로토콜로, **80번 포트**를 사용한다.
- **HTTPS**는 HTTP의 보안 문제를 해결하기 위해 등장한 프로토콜이다.
  - HTTP에 데이터 암호화가 추가된 프로토콜로, **443번 포트**를 사용한다.
- HTTPS가 데이터 암호화를 위해 사용하는 것이 **SSL/TSL 프로토콜** 이다.
  - TLS은 SSL을 표준화한 방식이다.
- 전송계층(TCP)과 응용계층(HTTP) 사이에 SSL 프로토콜를 통해 데이터가 암호화된다.
- SSL 연결을 통해 데이터를 암호화하더라도, header 부분은 여전히 볼 수 있다.
  - GET 요청에 중요한 정보를 담으면 안 됨을 알 수 있다.




### 대칭키 암호화 vs 개인키 암호화

- **대칭키 암호화 방식**

  - 암호화와 복호화에 같은 key를 사용한다.
  - key를 알면 암호를 복호화할 수 있기에, 보안상 문제가 있다.

- **비대칭키 암호화 방식**

  - 두 개의 key를 사용하는데, 하나의 key로 암호화하면 다른 key로 복호화할 수 있다.

    - 공개키로 암호화, 개인키로 복호화할 수도 있고,
    - 개인키로 암호화, 공개키로 복호화할 수도 있다.

  - 개인키를 공유하지 않아도 되므로 대칭키 암호화 방식보다 안전하다.

    (공개키는 누구에게나 공유되어도 상관 X)

- **SSL 통신에서는 대칭키 방식을 사용하되, 대칭키를 암호화하는 방식은 공개키 방식을 사용한다.**



### SSL Handshake

> TCP Handshake 이후 수행

1. **Client Hello**

   - 클라이언트가 서버에 접속한다.

   - 클라이언트의 랜덤 데이터, 지원하는 암호화 방식들을 전달한다.

  2. **Server Hello**

     - 서버가 클라이언트에 응답한다.

     - 선택한 클라이언트의 암호화 방식, 서버의 랜덤 데이터, SSL 인증서를 전달한다.
       - SSL 인증서에는 서비스의 정보 및 서버 측 공개키가 담겨 있다.

3. 클라이언트는 SSL 인증서가 CA(인증기관)에서 발급한 것인지 확인한다.

   - CA의 공개키로 인증서를 복호화한다. 성공한다면 인증서가 CA의 개인키로 암호화된 것임을 알 수 있다.

   - 이후 클라이언트의 랜덤 데이터와 서버의 랜덤 데이터를 조합하여 pre master secret(PMS)라는 값을 생성한다.

   - PMS 값을 SSL 인증서에 담긴 서버의 공개키로 암호화하여 서버로 보낸다.

4. 서버는 암호화된 PMS 값을 개인키로 복호화한다.
   - 클라이언트와 서버는 각각 PMS 키로 session key를 생성한다.

5. 클라이언트와 서버는 핸드쉐이크의 종료를 서로에게 알린다.



이후 session key를 사용하여 대칭키 방식으로 암호화된 데이터를 주고받다가, 

데이터 전송이 끝나면 session key를 폐기한다.
# 쿠키 vs 세션

### `왜 쓰나요?`

HTTP는 필요할 때마다 요청을 보내고 응답을 받는 비연결성 특징을 가지고 있다.

클라이언트가 응답을 받으면 서버는 접속을 끊기때문에 연결이 끝나면 상태 정보가 유지되지 않는다.

로그인 정보를 유지하기 위한 방법이 쿠키와 세션이다.



### `Cookie`

클라이언트의 웹 브라우저에 저장되는 작은 데이터 조각으로 서버가 클라이언트의 요청을 식별하는데 사용된다. 보통 아래와 같은 목적으로 사용한다.

* **세션 ID 관리**, 서버에 저장해야 할 민감한 정보에 대한 식별자 ID
* **개인화**, 사용자 선호 및 테마
* **트래킹**, 사용자 행동 기록 및 분석

#### `쿠키의 동작 순서`

1. 클라이언트가 페이지를 요청한다. 웹 서버는 쿠키를 생성한다.
2. 생성한 쿠키에 정보를 담아 HTTP 화면을 돌려줄 때, 같이 클라이언트에게 돌려준다.
3. 넘겨 받은 쿠키는 클라이언트가 가지고 있다가(로컬 PC에 저장) 다시 서버에 요청할 때 요청과 함께 쿠키를 전송한다.
4. 동일 사이트 재방문시 클라이언트의 PC에 해당 쿠키가 있는 경우, 요청 페이지와 함께 쿠키를 전송한다.

#### `사용 예시`

1. 방문했던 사이트에 다시 방문 하였을 때 아이디와 비밀번호 자동 입력
2. 팝업창을 통해 "오늘 이 창을 다시 보지 않기" 체크

#### `쿠키의 약점`

1. 쿠키의 특징으로는 클라이언트(브라우저)단에 저장된다는 것이다.
2. 즉, 보안에 약할 수 있다.
3. 쿠키를 훔쳐서 계정 접근 권한 등을 탈취하여 유저의 정보를 악용할 수 있다.

```
document.cookie 를 통해 쿠키 스토리지에 저장된 사용자 권한이 있는 쿠키에 접근
```



### `Session`

클라이언트가 웹 서버에 연결된 순간부터 웹 브라우저를 닫아 서버와의 HTTP 통신을 끝낼 때 까지 유지되는 데이터 집합이다.

사용자가 웹 사이트에 방문하여 서버에 요청을 보내게 되면, 사용자의 정보를 서버에 저장하고 그 정보를 식별할 수 있는 "세션 ID"를 `Set-Cookie` 헤더로 클라이언트에게 전송한다. 클라이언트는 쿠키로 세션 ID를 관리하고 해당 서버에 요청할 때마다 `Cookie` 헤더에 세션 ID를 포함시켜 전송하기 때문에 서버는 클라이언트를 식별하여 그에 맞는 정보를 응답으로 줄 수 있게 된다. 

* **민감한 정보 관리**, 사용자의 비밀번호 및 개인정보

#### `세션의 동작 방식`

1. 클라이언트 페이지가 요청한다.
2. 서버가 클라이언트마다 개별의 세션 ID를 부여한다.
3. 클라이언트는 요청할 때마다 세션 ID를 서버에 전달한다.
4. 서버는 받은 세션 ID로 클라이언트 정보를 가져와 활용한다.



### `쿠키와 세션의 차이점`

1. 저장 위치

   쿠키: 클라이언트에 파일로 저장되어 있다.

   세션: 서버에 저장되어 있다.

2. 보안

   쿠키: 클라이언트의 브라우저 로컬에 저장되기 때문에 변질되거나 HTTP request 요청 시에 이를 갈취당할 수 있어서 보안에 취약하다.

   세션: 쿠키를 이용해서 세션id만 저장하고 그것으로 구분해서 서버에서 처리하기 때문에 비교적으로 안전하다.

3. 라이프 사이클

   쿠키: 만료시간은 있지만 파일로 저장되기 때문에 브라우저를 종료해도 계속해서 정보가 남아있다. 만료기간에 따라 상대적으로 넉넉하게 쿠키를 삭제할 때까지 유지된다.

   세션: 만료기간을 정할 수는 있지만 브라우저가 종료되면 그에 상관없이 삭제된다.

4. 속도

   쿠키: 쿠키에 정보가 있기 때문에 서버에 요청시 속도가 빠르다.

   세션: 정보가 서버에 있기 때문에 처리가 요구되어 비교적으로 느리다.


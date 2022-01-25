# REST API 와 소켓 통신 차이점

## HTTP 통신

* Client의 요청이 있을 때만 서버가 응답, 해당 정보를 전송하고 곧바로 연결 종료
  * 단방향적 통신. server가 client로 요청을 보낼 수 없다
* 요청을 보낼 때, 기다리는 시간 + 연결하는 시간. 필요한 경우에만 server로 접근하는 콘텐츠 위주의 데이터를 사용할 때 용이하다.

| METHOD | 역할                                                         |
| ------ | ------------------------------------------------------------ |
| POST   | 해당 URI를 요청하면 리소스를 생성                            |
| GET    | 해당 리소스를 조회, 해당 도큐먼트에 대한 자세한 정보를 가져옴 |
| PUT    | 해당 리소스를 수정                                           |
| DELETE | 리소스를 삭제                                                |

## Socket 통신

* server와 client가 특정 port를 통해 실시간으로 양방향 통신을 하는 방식
* 실시간 streaming 중계나 실시간 채팅과 같이 즉각적으로 정보를 주고받는 경우에 사용



## Websocket 사용하기

웹소켓을 사용하려면 **Web Socket 객체 생성**을 해야한다. -> 이 객체는 **자동**으로 **서버와 연결**을 열려고 할 것이다.

* 필수 파라미터 1개 : **Url**
* 선택 파라미터 : protocols
* ERROR : SECURITY_ERR -> 포트 차단일 경우 발생

```javascript
var exampleSocket = new WebSocket("wss://~", "protocolOne")

var exampleSocket = new WebSocket("wss://~", ["protocolOne", "protocolTwo"])
```

#### 서버에 데이터 전송

* 전송 가능한 데이터 유형 : String, Blob, ArrayBuffer
* 바로 데이터를 전송하면 실패할 수 있기 때문에 **onopen()** 으로

```js
exampleSocket.onopen = function (event) {
    exampleSocket.send("socket open");
};
```

#### 서버로부터 데이터 수신

* 메세지가 수신되면 **message** 이벤트 => **onmessage** 함수로 전달

```js
exampleSocket.onmessage = function (event){
    console.log(event.data);
}
```

#### 연결 종료

* 웹 소켓 사용 종료 시 **close()** 메소드를 호출하여 연결을 종료

```js
exampleSocket.close();
```

* 네트워크에 전달이 되지 않은 정보가 아직 남았을 수도 있으니, **bufferedAmount** Attribute를 조사하여 데이터를 검사하는 것도 좋다.
* 고려사항 - 보안
  * 웹소켓은 **혼합 연결 환경**에 이용할 수 없다.
  * ex) HTTPS로 로드 된 페이지 → non-secure 웹소켓 연결 수립, non-secure 웹소켓 연결 → HTTPS로 로드 된 페이지
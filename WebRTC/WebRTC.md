# WebRTC

| HTTP   | Fetch API  |
| ------ | ---------- |
| WebRTC | WebRTC API |

### WebRTC 4단계

1. Signaling
2. Connecting
3. Securing
4. Communicating

WebRTC는 RTCPeerConnection을 사용하여 브라우저간의 data streaming을 communicate. `signaling`이라고 불리는 메커니즘이 필요하다. => `Socket.io` 사용

WebRTC는 P2P로 작동한다. client application은 `NAT gateways`, 방화벽 등을 넘어야하고, 직접 접속(direct connection)이 끊어질 경우의 fallbacks도 필요하다.

WebRTC API는 STUN 서버를 사용하여 해당 컴퓨터의 ip 주소를 얻고, TURN 서버를 P2P 커뮤니케이션이 실패했을 경우의 relay server로 사용한다.

### What you'll learn

* webcam을 통해 video 가져오기
* `RTCPeerConnection`을 통해 video stream
* `RTCDataChannel`을 통해 data stream
* 메세지 교환을 위한 signaling service 세팅
* peer connection과 signaling combine
* 사진을 찍고 data channel을 통해 이를 공유

### WebRTC(API)는 어떻게 작동?

- MediaStream(getUserMedia) - 사용자의 카메라/마이크 등 데이터 스트림 접근
- RTCPeerConnection - user들 간에 audio, video 스트리밍
- RTCDataChannel - user들 간에 data 스트리밍

`MediaStream`으로 peer(WebRTC의 Client)의 스트림을 얻고,
`RTCPeerConnection`으로 연결하고자 하는 peer의 정보를 주고 받아 연결된다.
이 과정을 `Signaling`이라고 한다.

simple peer 라이브러리

#### MediaStream(getUserMedia)

사용자의 카메라와 마이크 같은 곳의 데이터 스트림에 접근한다.

navigator.mediaDevices.getUserMedia()에서 생성된 입력과 video 태그 또는 RTCPeerConnection으로 넘겨주는 출력을 갖는다.

navigator.mediaDevices.getUserMedia()가 받는 3개의 매개변수

* 제약 오브젝트(video 사용 여부(또는 해상도), audio 사용 여부 등)
* 성공 시 콜백(MediaStream)
* 실패 시 콜백(error)

**getUserMedia()는 반드시 로컬 파일 시스템이 아닌 서버에서 사용되어야 하며, 이외의 경우에는 PERMISSION_DENIED: 1 에러가 발생한다.**

#### RTCPeerConnection

암호화 및 대역폭 관리를 하는 기능을 가지고 있고, 오디오 또는 비디오 연결을 한다. Peer들 간의 데이터를 안정적이고 효율적으로 통신하게 처리하는 WebRTC 컴포넌트이다.

![KakaoTalk_20220129_233318651](https://user-images.githubusercontent.com/60650518/152140324-b90ae12d-4303-450f-aab3-395e93e12a5c.jpg)

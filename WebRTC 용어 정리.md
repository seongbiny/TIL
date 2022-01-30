# WebRTC 용어 정리

## ICE (Interactive Connectivity Establishment)

웹 브라우저가 다른 동료들과 연결할 수 있게 하는 프레임워크

Peer A와 Peer B를 직접적으로 연결할 수 없는 다양한 이유가 있다.

1. 연결을 생성하지 못하게 막는 방화벽을 우회해야 한다.
2. public ip 주소를 갖고 있지 않은 장치에게 고유한 주소를 배정해야 한다.
3. 라우터가 직접적으로 동료들과 연결하는 것을 허락하지 않으면 서버를 거쳐 데이터를 주고 받아야 한다.

ICE 는 STUN 서버나 TURN 서버를 이용한다.

## STUN(Session Traversal Utilities for NAT

public address를 발견하고 라우터에 걸려 있는 제약 사항을 알아내는 프로토콜

클라이언트가 STUN 서버에 요청을 보내면 STUN 서버는 클라이언트의 public address와 클라이언트가 라우터의 NAT에 연결 가능한지 알려준다.

**클라이언트 자신의 Public Address(IP:PORT)를 알려준다.**

클라이언트는 인터넷을 통해 **클라이언트의 Public Address**와 **라우터의 NAT 뒤에 있는 클라이언트가 접근 가능한지에 대한 답변**을 STUN서버에 요청한다.

## NAT(Network Address Translation)

당신의 장치에 public IP 주소를 부여하기 위해 사용한다.

라우터는 public IP 주소를 갖게되고, 라우터에 연결되어 있는 장치들은 private IP 주소를 갖게 된다. 이 방법을 통해 모든 장치에 unique public IP를 부여하지 않고도 각 장치를 식별할 수 있게 된다.

몇몇 라우터는 특정 자치만 네트워크에 연결할 수 있는 제약조건을 가지고 있다. 이 경우 STUN 서버에서 public IP를 찾아도 연결이 불가능하다. 이럴 때 TURN 서버를 이용한다.

위에서 말하는 제약 조건은 'Symmetric NAT'이라고 불리낟. 이 제약은 이전에 연결된 적이 있는 동료들로부터의 연결만 허용한다.

## TURN(Traversal Using Relays around NAT)

'Symmetric NAT' 제약 조건을 우회하기 위해 사용한다.

이를 위해 **TURN 서버와 연결**을 한 후 **모든 peer들에게 저 서버에 모든 패킷을 보내고 다시 나(TURN서버)에게 전달**해달라고 해야 한다.

명백히 오버헤드가 발생하므로 이 방법은 다른 대안이 없을 경우만 사용해야한다.

TURN 서버와의 연결을 만들고 모든 정보를 서버를 통해 전달한다.

## SDP(Session Description Protocol)

mulitmedia content를 묘사하는 기준(standard)이다.

multimedia content로는 해상도(resoultion), 서식(formats), codecs, 암호화(encryption) 등이 있다.

두 개의 peer가 다른 한 쪽이 **데이터가 전송되고 있다는 것을 알게 해준다.**

따라서 각각의 참여자들(peers)은 데이터가 전송됐을 때 서로를 이해할 수 있다. 이것은 본질적으로 content를 묘사하는 metadata이지 media content 그 자체를 묘사하는 metadata인 것은 아니다. 

엄밀히 말하면 SDP는 프로토콜이 아니다. **장치들 간 media를 공유하기 위한 연결에 사용되는 data format 이다.**

# WebRTC 구현방식

* WebRTC는 ICE, STUN, TURN, SDP로 작동된다. P2P 연결을 완성시키기 위해서는 개발자가 peer간의 offer와 answer를 통한 session 정보를 중계해주는 서버를 만들어줘야한다.
* 하지만 p2p 연결로 다인원의 데이터 송수신을 지원하게되면 클라이언트 측면에서의 과부하가 심하게 오기 때문에 권장하지 않는다. 이러한 문제의 해결책으로 나온 것이 SFU와 MCU 방식의 미디어 서버를 두는 것이다.

### 서버의 종류

WebRTC를 위해 개발자가 구현할 수 있는 서버는 크게 세 종류가 있다.

* Signaling
* SFU
* MCU

#### Signaling 서버(P2P/Mesh)

peer 간의 offer, answer라는 session 정보 signal 만을 중계한다. 따라서 처음 WebRTC가 peer간의 정보를 중계할 때만 서버에 부하가 발생한다.

peer간의 연결이 완료된 후에는 서버에 별도의 부하가 없다. 1:1 연결에 적합하다.

#### SFU(Selective Forwarding Unit) 서버

종단 간 미디어 트래픽을 중계하는 중앙 서버 방식이다.

클라이언트 peer간 연결이 아닌, 서버와 클라이언트 간의 peer를 연결한다.

1:1, 1:N, 혹은 N:M 등 모든 연결 형식에서 클라이언트는 연결된 모든 사용자에게 데이터를 보낼 필요없이 서버에게만 자신의 영상 데이터를 보내면 된다.(즉, Uplink가 1개다.)

하지만 상대방의 수만큼 데이터를 받는 peer를 유지해야한다.

1:N 형식 또는 소규모 N:M 형식의 실시간 스트리밍에 적합하다.

#### MCU(Multi-point Control Unit) 서버

다수의 송출 미디어를 중앙 서버에서 혼합(muxing) 또는 가공(transcoding)하여 수신측으로 전달하는 중앙 서버 방식이다.

*예를들어, 5인이 WebRTC 연결을 한다면 자신을 제외한 다른 4인의 video 데이터를 하나의 video 데이터로 편집하고, audio 데이터도 마찬가지로 편집하여 한 명에게 보낸다. 이 작업을 남은 4명에게도 동일하게 적용한다.*

클라이언트 peer간 연결이 아닌, 서버와 클라이언트 간의 peer를 연결한다.

모든 연결 형식에서 클라이언트는 연결된 모든 사용자에게 데이터를 보낼 필요없이 서버에게만 자신의 영상 데이터를 보내면 된다.

모든 연결 형식에서 클라이언트는 연결된 사용자의 수와 상관없이 서버에게서 하나의 peer로 데이터를 받으면 된다.
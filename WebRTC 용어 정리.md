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

## NAT(Network Address Translation)

당신의 장치에 public IP 주소를 부여하기 위해 사용한다.

라우터는 public IP 주소를 갖게되고, 라우터에 연결되어 있는 장치들은 private IP 주소를 갖게 된다. 이 방법을 통해 모든 장치에 unique public IP를 부여하지 않고도 각 장치를 식별할 수 있게 된다.

몇몇 라우터는 특정 자치만 네트워크에 연결할 수 있는 제약조건을 가지고 있다. 이 경우 STUN 서버에서 public IP를 찾아도 연결이 불가능하다. 이럴 때 TURN 서버를 이용한다.

위에서 말하는 제약 조건은 'Symmetric NAT'이라고 불리낟. 이 제약은 이전에 연결된 적이 있는 동료들로부터의 연결만 허용한다.

## TURN(Traversal Using Relays around NAT)

'Symmetric NAT' 제약 조건을 우회하기 위해 사용한다.

TURN 서버와의 연결을 만들고 모든 정보를 서버를 통해 전달한다.

## SDP(Session Description Protocol)

mulitmedia content를 묘사하는 기준(standard)이다.

multimedia content로는 해상도(resoultion), 서식(formats), codecs, 암호화(encryption) 등이 있다.

따라서 각각의 참여자들(peers)은 데이터가 전송됐을 때 서로를 이해할 수 있다. 이것은 본질적으로 content를 묘사하는 metadata이지 media content 그 자체를 묘사하는 metadata인 것은 아니다. 

엄밀히 말하면 SDP는 프로토콜이 아니다. 장치들 간 media를 공유하기 위한 연결에 사용되는 data format 이다.
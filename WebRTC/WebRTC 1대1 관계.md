# WebRTC 1:1 관계

## 구현 방식

### 간략한 연결 구조

![5](C:\Users\SSAFY\Desktop\image\5.PNG)

Caller가 Signaling 서버를 통해 자신의 SessionDescription을 보내면 Callee도 마찬가지로 Signaling 서버를 통해 자신의 SessionDescription을 보낸다. 그 외에도 ICECandidate를 Signaling 서버를 통해 주고받으며 peer 간 연결을 완료하고 Caller와 Callee 간에 Media 데이터를 주고받는다.

### STUN 서버 동작

![image-20220114210329834](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220114210329834.png)

STUN 서버를 통해 자신의 Public Address를 알아내고 접근 가능한 지 여부(Symmetric NAT 제한 여부)를 알아낸다. Relay server란 TURN 서버를 나타내는 것으로 Symmetric NAT 제한을 우회하는 방식이다. 이 방식은 오버헤드가 발생하므로 대안이 없을 경우에만 사용해야 한다.

### 연결 후 데이터 흐름

![image-20220114210524594](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220114210524594.png)

peer 연결이 완료됐을 때 peer간의 데이터 흐름을 보여준 것으로 만약 TURN 서버가 필요하지 않다면(Symmetric NAT 제한이 걸리지 않는 다면) Relay server 없이 peer간의 통신이 이루어지고, 만약 TURN 서버가 필요하다면(Symmetric NAT 제한이 걸렸다면) 모든 peer들에게 서로가 주고받는 데이터를 TURN 서버에 같이 전달해야 한다.

### 주고받는 Signal 데이터

1. 각각의 peer들은 STUN 서버에 자신의 Public Address와 접근 가능한지 여부를 전달받는다.
2. peer1(Caller)이 createOffer를 통해 먼저 자신의 SessionDescription을 생성하고 Signaling Server를 통해 peer2(Callee)에게 전달한다.
3. peer2가 peer1의 SessionDescription을 전달받고 이에 대한 답으로 createAnswer을 통해 자신의 SessionDescription을 생성하고 Signaling Server를 통해 peer1에 전달한다.
4. peer1과 peer2 모두 자신의 SessionDescription을 생성한 후부터 자신의 ICECandidate 정보를 생성하기 시작하고 이를 각각 서로에게 전달한다.
5. 서로의 MediaStream을 peer간 통신으로 주고받는다.
6. 만약 peer1과 peer2 둘 중 Symmetric NAT을 가진 Peer가 있는 경우 TURN 서버를 사용해 data relay로 연결을 진행해야 한다.




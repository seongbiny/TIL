# 생활코딩 CLI백업 #



### 백업의 방법에는 2가지가 있다. ###

* 자유롭지만 어려운 방법 : 직접 백업 서버를 구축하는 것
* 제한적이지만 쉬운 방법 : 
  * 인터넷에 연결된 컴퓨터 = 호스트
  * 호스팅 = 인터넷에 연결 되어서 원격으로 사용할 수 있는 서버를 임대해 주는 사업
  * git hosting : 로컬 저장소에 버전을 업로드할 원격 저장소를 임대해주는 비즈니스



작업용 컴퓨터 : 지역 저장소 local repository

저장용 컴퓨터 : 원격 저장소 remote repository

작업이 끝나고 push를 하면 두개의 컴퓨터가 같은 상태가 된다. =백업

작업용 컴퓨터2 : 원격 저장소의 내용 복제를 하는 과정 = 클론

작업용 컴퓨터를 저장용 컴퓨터에서 pull을 하면 같은 상태가 된다.



### 원격 저장소를 마련해야 한다. (git hosting) ###

GitHub , gitlab

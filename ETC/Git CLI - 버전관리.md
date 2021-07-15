# 생활코딩 버전관리 #



## Git 명령어 ##

<h3> 0. 폴더 생성 </h3>

git 저장소로 만들 폴더 생성

* `cd [폴더명]` : 폴더 변경
  * `cd ..` : 상위 폴더 이동
  * `cd ~` : 홈 폴더 이동

* `mkdir [폴더명]` : 폴더 생성
* `rm [파일명]` : 파일 삭제
* `rm -r [폴더명]` : 폴더 삭제
  * `rm -rf [폴더명]` : 강제 폴더 삭제 (확인X)
  * `rm -rf /` : /폴더 모두 삭제

* `touch [파일명]` : 파일 생성



### 1.`git init` (initialze repository) ###

Git 프로젝트(저장소)를 시작 (<h3>폴더 단위</h3>)

```Initialized empty Git repository in C:/Users/student/git_basic/.git/```

1.(`master`)

2.`.git` (git repository) 폴더 생성

### (중요) git 프로젝트를 종료 ###

* `.git` 폴더 삭제



### 2. `git status` (working tree status) ###

git의 현재 상태를 출력



### 3. `git add [파일명]` ###

commit 하기 위한 stage에 파일 추가



### 4. `git commit -m "커밋메세지"` ###

스냅샷 & 버전 생성

### commit의 구성 요소 ###

* Committer(author) : commit 을 찍은 사람
* commit datetime(date) : commit 을 찍은 시간
* commit message : commit 에 대한 내용 (필수)



### 5. `git config` ###

* `git config --global user.email "이메일"` : 사용자 이메일 설정
* `git config --global user.name "이름"` : 사용자 이름 설정
* `git config --global user.email` : 사용자 이메일 출력
* `git config --global user.name` : 사용자 이름 출력



### 6. `git log` ###

Commit 목록(log) 출력

* `git log --oneline` : 한줄 출력
* `git log --stat` :
* `git log -p` : 모든 파일의 추가되고, 삭제된 내용을 보여준다.
* `cat [파일명]` : 파일 내용을 보여준다



### 7. `git diff` (Show changes) ###

파일의 추가되고, 삭제된 내용을 보여준다.



### 8. `git reset` ###

지금까지의 내용이 사라진다. 그 이전 버전의 상태로 돌아간다.

다른 사람과 공유한 버전은 reset 하면 안됨!

###  여기까지 Create read 의 과정. Update Delete 를 알아보자 ###



### 9.`git checkout ` ###

과거로 돌아갔다가 다시 미래로 오는

* (master) : 가장 최신 버전. 현재의 버전
* HEAD -> master : 현재 상태가 최신버전, 실제 마지막 버전을 가르키고 있다.

* `git checkout 돌아가고싶은 버전의 아이디` 
* `git checkout master` : 다시 최신상태로 복귀



### 10.`git revert` ###

버전을 삭제하지 않으면서 되돌리는 방법

충돌을 막기위해 역순으로 리버트를 한다. (?)



### 11.diff tool ###

* .gitignore [파일명] : 버전관리를 안하는 파일

* branch 마치 평행우주처럼 우리의 저장소를 여러가지 상태로 공존하게 해줌.

* 커밋아이디 너무 길어서 기억하기 쉽지않음 -> tag를 이용

* Backup 
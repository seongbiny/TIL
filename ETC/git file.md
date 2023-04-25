### git add

`git add` 는 작업 디렉토리 상의 변경 내용을 스테이징 영역에 추가하기 위해서 사용하는 명령어이다.

- `git add <파일/디렉토리 경로>`

  - 작업 디렉토리의 변경 내용의 일부만 스테이징 영역에 넘기고 싶을 때, 수정한 파일이나 디렉토리의 경로를 인자로 넘긴다.

- `git add *.txt`

  - 현재 디렉토리상에 .txt 확장자를 가지고 있는 모든 파일을 스테이징 영역으로 넘기고 싶을때 사용

- `git add .`

  - 현재 디렉토리의 모든 변경 내용을 스테이징 영역으로 넘기고 싶을 때, “.”을 인자로 넘긴다.

- `git add *`

  - 현재 디렉토리의 모든 변경 내용을 스테이징 영역으로 넘기고 싶을 때 사용

- git add . VS git add *

  git add . 은 .gitignore에 있는 파일은 제외하고 스테이징에 올린다.

### gitignore

로그파일, 빌드파일, 암호 등 민감한 내용은 GitHub에 올리지 않아야한다.

### git status

우리가 작업하고 있는 모든 내용들을 간단하게 확인할 수 있다.

- git status -s

### 파일 비교 diff

파일의 추가되고, 삭제된 내용을 보여준다.

- git diff -h
- git diff —staged == git diff —cache

### 첫번째 커밋 git commit

- git commit -m “내용 작성”
- git log
  - history 확인
- git commit -am “내용 작성”

### 커밋 팁

- 커밋은 너무 커도, 너무 작아도 안되고 최소 1개의 의미를 담아 1개의 커밋을 하자!
# SQL

### SQL (Structured Query Language)

* 관계형 데이터베이스 관리시스템의 **데이터 관리**를 위해 설계된 **특수 목적 프로그래밍 언어**
* 데이터베이스 스키마 생성 및 수정
* 자료의 검색 및 관리
* 데이터베이스 객체 접근 조정 관리

#### SQL 분류

| 분류                   | 개념                                                         | 예시                         |
| ---------------------- | ------------------------------------------------------------ | ---------------------------- |
| DDL - 데이터 정의 언어 | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE DROP ALTER            |
| DML - 데이터 조작 언어 | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT SELECT UPDATE DELETE  |
| DCL - 데이터 제어 언어 | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT REVOKE COMMIT ROLLBACK |

#### SQL keywords - Data Manipulation Language

* INSERT : 새로운 데이터 삽입(추가)
* SELECT : 저장되어있는 데이터 조회
* UPDATE : 저장되어있는 데이터 갱신
* DELETE : 저장되어있는 데이터 삭제

### 테이블 생성 및 삭제

#### 데이터베이스 생성하기

```python
$ sqlite3 tutorial.sqlite3
sqlite> .database
```

#### csv 파일을 table로 만들기

```sqlite
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
examples
```

#### SELECT

```sqlite
SELECT * FROM examples;
```

#### SELECT 확인하기

```SQLITE
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232
```

**SELECT 문은 특정 테이블의 레코드(행) 정보를 반환!**

#### 테이블 생성 및 삭제 statement

* CREATE TABLE
  * 데이터베이스에서 테이블 생성
* DROP TABLE
  * 데이터베이스에서 테이블 제거

#### CREATE

```sqlite
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
```

#### CREATE - 테이블 생성 및 확인하기

![image-20211004014530174](md-images/image-20211004014530174.png)

#### 특정 테이블의 schema 조회

![image-20211004014608261](md-images/image-20211004014608261.png)

#### DROP

```sqlite
DROP TABLE classmates;
```

### CRUD

### CREATE

#### INSERT

```sqlite
INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ..);

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
```

**INSERT는 특정 테이블에 레코드(행)를 삽입(생성)!**

**모든 열에 데이터가 있는 경우 column을 명시하지 않아도 됨!**

SQLite는 따로 **PRIMARY KEY 속성의 컬럼을 작성하지 않으면** 값이 자동으로 증가하는 PK옵션을 가진 **rowid 컬럼을 정의** 

### READ

#### SELECT와 함께 사용하는 clause

* LIMIT
  * 쿼리에서 반환되는 행 수를 제한
  * 특정 행부터 시작해서 조회하기 위해 **OFFSET** 키워드와 함께 사용하기도 함
* Where
  * 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
* SELECT DISTINCT
  * 조회 결과에서 중복 행을 제거
  * DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

```sqlite
SELECT 컬럼1, 컬럼2, ... FORM 테이블이름; 
```

**모든 컬럽 값이 아닌 특정 컬럼 조회하기**

#### LIMIT

```sqlite
SELECT 컬럼1, 컬럼2, ... FORM 테이블이름 LIMIT 숫자;
```

**모든 컬럼 값이 아닌 특정 컬럼만 원하는 수 만큼 데이터 조회하기**

#### OFFSET keyword

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
```

**특정 부분에서 원하는 수 만큼 데이터 조회하기**

#### WHERE

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건;
```

**특정 데이터(조건) 조회하기**

#### DISTINCT

```sqlite
SELECT DISTINCT 컬럼 FROM 테이블이름;
```

**특정 컬럼을 기준으로 중복없이 가져오기**

### DELETE




# Django_2

### Django Model

* 목차

1. Model
2. ORM
3. Migrations
4. Database API
5. CRUD
6. Admin Site

-----------------------------------

#### Model

* 단일한 데이터에 대한 정보를 가짐
  * 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
* 저장된 데이터베이스의 구조(layout)
* django는 model을 통해 데이터에 접속하고 관리
* 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑 됨

#### Database

* 데이터베이스(DB)
  * 체계화된 데이터의 모임
* 쿼리(Query)
  * 데이터를 조회하기 위한 명령어
  * 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  * "Query를 날린다." -> DB를 조작한다.

* 스키마(Schema)
  * 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(structure)
* 테이블(Table)
  * 열(column) : 필드(field) or 속성
    * 각 열에는 고유한 데이터 형식이 지정된다. 
  * 행(row) : 레코드(record) or 튜플
    * 테이블의 데이터는 행에 저장된다.

* **PK(기본키)**
  * 각 행의 고유값으로 primary key로 불린다.
  * 반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다.

![image-20210902141641270](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210902141641270.png)


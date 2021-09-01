# Django Intro

> Django 시작하기

* Django 설치 전 **가상환경 생성 및 활성화**

![image-20210901232950960](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901232950960.png)

* 메인 페이지 로켓 확인

> 프로젝트 구조

![image-20210901233321061](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901233321061.png)

* \_\_init\_\_.py

  * python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시

* asgi.py

  * asynchronous server gateway interface
  * django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

* settings.py

  * 애플리케이션의 모든 설정을 포함

* urls.py

  * 사이트의 url과 적절한 views의 연결을 지정

* wsgi.py

  * web server gateway interface
  * django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움

* manage.py

  * django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

  * ```
    $ python manage.py <command> [options]
    ```

> Application 생성

* **복수형** 으로 하는 것을 권장

```
$ python manage.py startapp articles
```

> Application 구조

![image-20210901234041804](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901234041804.png)

* admin.py
  * 관리자용 페이지를 설정 하는 곳
* apps.py
  * 앱의 정보가 작성된 곳
* models.py
  * 앱에서 사용하는 model을 정의하는 곳
* tests.py
  * 프로젝트의 테스트 코드를 작성하는 곳
* views.py
  * view 함수들이 정의 되는 곳

#### Project & Application

* Project
  * 프로젝트는 앱의 집합
  * 프로젝트에는 여러 앱이 포함될 수 있음
  * 앱은 여러 프로젝트에 있을 수 있음
* Application
  * 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
  * 하나의 프로젝트는 여러 앱을 가짐
  * 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함

#### 앱 등록

![image-20210901234347677](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901234347677.png)

* 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해야 함
* **INSTALLED_APPS**
  * Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록

> 앱 생성 시 주의 사항

* **"반드시 생성 후 등록 !"**
* INSTALLED_APPS에 먼저 작성(등록)하고 생성하려면 앱이 생성되지 않음

----------------------------------------

### 요청과 응답

#### URLS

![image-20210901234705174](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901234705174.png)

* HTTP 요청을 알맞은 view로 전달

#### View

![image-20210901234851426](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901234851426.png)

* HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
* Model을 통해 요청에 맞는 필요 데이터에 접근
* Template에게 HTTP 응답 서식을 맡김

#### Templates

* 실제 내용을 보여주는데 사용되는 파일
* 파일의 구조나 레이아웃을 정의
* Template 파일 경로의 기본 값은 **app 폴더 안의 templates 폴더**로 지정되어 있음

#### 추가 설정

![image-20210901235241542](C:/Users/seongbiny/AppData/Roaming/Typora/typora-user-images/image-20210901235241542.png)

* LANGUAGE_CODE
  * 모든 사용자에게 제공되는 번역을 결정
* TIME_ZONE
  * 데이터베이스 연결의 시간대를 나타내는 문자열 지정

---------------------------------

### Template

#### Django Template Language (DTL)

* 단순히 python이 HTML에 포함 된 것이 아니며, 프로그래밍적 로직이 아니라 **프레젠테이션을 표현하기 위한 것**

> DTL Syntax

1. Variable
2. Filters
3. Tags
4. Comments

#### DTL Syntax - Variable

```django
{{ varible }}
```

* render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
* dot(.)를 사용하여 변수 속성에 접근할 수 있음
* render()의 세번째 인자로 {'key': value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

#### DTL Syntax - Filters

```django
{{ variable|filter }}
```

* 표시할 변수를 수정할 때 사용

#### DTL Syntax - Tags

```django
{% tag %}
```

* 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
* 일부 태그는 시작과 종료 태그가 필요

```django
{% if %}{% endif %}
```

#### DTL Syntax - Comments

```django
{# #} # 한줄 주석
{% comment %}
  여러줄 주석
{% endcomment %}
```

#### **코드 작성 순서**

* 데이터의 흐름에 맞추어 작성

1. urls.py
2. views.py
3. templates

#### Template inheritance (템플릿 상속)

* 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
* 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 "skeleton" 템플릿을 만들 수 있음

> Template inheritance = "tags"

```
{% extends ' ' %}
```

* 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
* 반드시 템플릿 최상단에 작성 되어야 함

```
{% block content %} {% endblock %}
```

* 하위 템플릿에서 재지정(overriden)할 수 있는 블록을 정의
* 하위 템플릿이 채울 수 있는 공간

----------------------------


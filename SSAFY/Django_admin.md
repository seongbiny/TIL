# Django_admin

### Admin Site

> 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지

* 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
* Article class를 `admin.py`에 등록하고 관리
* record 생성 여부 확인에 매우 유용하고 CRUD 로직을 확인하기에 편리하다

**관리자 생성**

```python
$ python manage.py createsupteruser
```

* 관리자 계정 생성 후 서버를 실행한 다음 `/admin` 으로 가서 관리자 페이지 로그인
* 모델을 등록하지 않으면 기본적인 사용자 정보만 확인 할 수 있다.
* `admin.py`로 가서 관리자 사이트에 등록하여 내가 만든 record를 보기 위해서는 Django 서버에 등록

**model 등록**

```django
# articles/admin.py

from django.contrib import admin
from .models import Article

# admin site에 등록(register)한다.
admin.site.register(Article)
```

**admin site 확인**

* admin 사이트에 방문해서 우리가 현재까지 작성한 글들을 확인
* `admin.py`는 관리자 사이트에 Article 객체가 관리 인터페이스를 가지고 있다는 것을 알려주는 것
* 이렇게 admin 사이트에 등록된 모습이 어딘가 익숙하다?'
* 바로 `model.py`에 정의한 `__str__`의 형태로 객체가 표현된다


# Django_4

## Managing Static Files

* Static files
* Media files
* Image Upload
* Image Resizing



#### Static file

* 정적 파일
* 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  * 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일
* ex, 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함
* Django에서는 이러한 파일들을 "static file"이라 함

**Static file 구성**

1. **django.contrib.staticfiles** 가 INSTALLED_APPS에 포함되어 있는지 확인
2. settings.py에서 **STATIC_URL**을 정의
3. 템플릿에서 **static 템플릿 태그**를 사용하여 지정된 상대경로에 대한 URL을 빌드

```python
{% load static %}
<img src="{% static 'my_app/example.jpg' %}" alt="My image">
```

4. 앱의 static 폴더에 정적 파일을 저장

**Django templates tag**

* load
  * 사용자 정의 템플릿 태그 세트를 로드
  * 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드
* static
  * STATIC_ROOT에 저장된 정적 파일에 연결

**The staticfiles app**

* STATIC_ROOT

  * collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
  * django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
  * 개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 적용되지 않음
    * 직접 작성하지 않으면 django 프로젝트에서는 settings.py에 작성되어 있지 않음
  * 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

* STATIC_URL

  * STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용한 URL
    * 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/경로 (기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색함
  * 실제 파일이나 디렉토리가 아니며, URL로만 존재
  * 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

  ```python
  STATIC_URL = '/static/'
  ```

* STATICFILES_DIRS

  * app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
  * 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함

  ```python
  STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
  ```

### 이미지 업로드 (기본 설정)

**Media file**

* 미디어 파일
* 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
* 유저가 업로드 한 모든 정적 파일

**Model field**

* ImageField
  * 이미지 업로드에 사용하는 모델 필드
  * FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함
  * ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있음
  * [주의] 사용하려면 반드시 Pillow 라이브러리가 필요
* FileField
  * 파일 업로드에 사용하는 모델 필드
  * 2개의 선택 인자를 가지고 있음
    1. upload_to
    2. ~~storage~~

**upload_to argument**

* 업로드 디렉토리와 파일 이름을 설정하는 2가지 방법을 제공
  1. 문자열 값이나 경로 지정
  2. 함수 호출

**upload_to argument -1.문자열 경로 지정 방식**

* 파이썬의 strftime() 형식이 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체 됨

```python
# models.py

class MyModel(models.Model):
    # MEDIA_ROOT/uploads/ 경로로 파일 업로드
    upload = models.FileField(upload_to='uploads/')
    # or
    # MEDIA_ROOT/uploads/2021/01/01 경로로 파일 업로드
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```

**upload_to argument -2.함수 호출 방식**

* 반드시 2개의 인자(instance, filename)를 사용 함

1. **instance**
   * FileField가 정의된 모델의 인스턴스
   * 대부분 이 객체는 아직 데이터베이스에 저장되지 않았으므로 PK 값이 아직 없을 수 있음
2. **filename**
   * 기존 파일에 제공된 파일 이름

```python
# models.py

def articles_image_path(instance, filename):
    # MEDIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    return f'user_{instance.user.pk}/{filename}'

class Article(models.Model):
    image = models.ImageField(upload_to=articles_image_path)
```

**ImageField (or FileField)를 사용하기 위한 몇 가지 단계**

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의하여 업로드 된 파일에 사용 할 MEDIA_ROOT의 하위 경로를 지정
3. 업로드 된 파일의 경로는 django가 제공하는 'url' 속성을 통해 얻을 수 있음

```python
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```

**MEDIA_ROOT**

* 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
* django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
  * 실제 데이터베이스에 저장되는 것은 **파일의 경로**
* [주의] MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

**MEDIA_URL**

* MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
* 업로드 된 파일의 주소(URL)를 만들어 주는 역할
  * 웹 서버 사용자가 사용하는 public URL
* 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함
* [주의] MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함

**STATIC_URL과 MEDIA_URL**

* static, media 결국 모두 서버에 요청해서 조회하는 것
* 서버에 요청하기 위한 url을 urls.py가 아닌 settings에 먼저 작성 후 urlpatterns에 추가하는 형식

### 이미지 업로드(CREATE)

**ImageField 작성**

* upload_tp='images/'
  * 실제 이미지가 저장되는 경로를 지정
* blank=True
  * 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정 (이미지를 선택적으로 업로드 할 수 있도록)

```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # saved to 'MEDIA_ROOT/images'
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Model field option - "blank"**

* 기본 값 : False
* True인 경우 필드를 비워 둘 수 있음
  * DB에는 ''(빈 문자열)이 저장됨
* 유효성 검사에서 사용 됨(is_valid)
  * 필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음

**Model field option = "null"**

* 기본 값 : False
* True면 django는 빈 값을 DB에 NULL로 저장
* 주의 사항
  * CharField, TextField와 같은 **문자열 기반 필드에는 사용하는 것을 피해야 함**
* blank
  * Validation-related
* null
  * Database-related
* 문자열 기반 및 비문자열 기반 필드 모두에 대해 null option은 DB에만 영향을 미치므로, form에서 빈 값을 허용하려면 **blank=True**를 설정해야 함

```python
# models.py

class Person(models.Model):
    nama = models.CharField(max_length=10)
    
    # null=True 금지
    bio = models.TextField(max_length=50, blank=True)
    
    # null, blank 모두 설정 가능 -> 문자열 기반 필드가 아니기 때문
    birth_date = models.DateField(null=True, blank=True)
```

- 34p


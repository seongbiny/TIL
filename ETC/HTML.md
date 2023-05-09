# 

# HTML 이해하기

### HTML이란?

HTML은 프로그래밍 언어로 웹 페이지를 만들 때 사용된다.

### HTML의 의미와 특징

Hyper Text Markup Language

Hyper Text: 웹 페이지의 특정 부분과 연결할 수 있는 기능을 가진 텍스트 즉, 링크를 의미한다.

Markup Language: 프로그래밍 언어의 한 종류로 정보를 구조적, 계층적으로 표현 가능하다는 특징이 있다.

HTML은 파일 확장자로 .html을 쓰며, 그 파일 안에 html 코드를 작성한다.

## HTML 문법

- 태그
- 속성
- 중첩
- 빈 태그
- 공백
- 주석

### 태그란?

HTML은 태그들의 집합

태그는 <,> 기호로 표현하며 <,> 기호 사이에 태그 이름이 들어간다.

대부분 태그는 시작 태그와 종료 태그로 이루어지며 종료 태그는 태그 이름 앞에 ‘/’ 기호가 붙는다.

```html
<h1>Hello, HTML</h1>
```

### 요소란?

내용을 포함하는 태그 전체를 요소(Element)라고 한다.

### 속성이란?

속성은 태그에 추가로 정보를 제공하거나 태그의 동작이나 표현을 제어할 수 있는 설정값을 의미한다.

속성은 이름과 값으로 이루어져 있다.

시작태그에서 태그 이름 뒤에 공백으로 구분 후 속성 이름=”속성 값”으로 표현한다.

```html
<h1 id="title" class="main">Hello, HTML</h1>
```

속성은 종류에 따라 모든 태그에 사용할 수 있는 글로벌 속성과 특정 태그에서만 사용할 수 있는 속성으로 구분된다.

선택적으로 쓸 수 있는 속성과 특정 태그에서 필요한 필수 속성으로 구분된다.

### 태그의 중첩

태그 안에 다른 태그를 선언할 수 있다.

태그를 중첩해서 사용 시 중첩되는 태그는 부모 태그를 벗어나서는 안된다.

태그의 중첩이 불가한 태그도 있다. 이런 태그를 **빈 태그**라고 한다.

### 빈 태그란?

빈 태그는 내용이 없어서 종료 태그가 필요하지 않다.

```html
<br>
<img src="">
<input type="">
```

### HTML에서의 공백

기본적으로 HTML은 두 칸 이상의 공백을 모두 무시한다.

```html
<h1>Hello, HTML</h1>
<h1>Hello,  HTML</h1>
<h1>
  Hello,
	HTML
</h1>
```

위 세가지 모두 같은 텍스트가 화면에 나타나게 된다.

### HTML에서의 주석

주석은 화면에 노출되지 않고 메모의 목적으로만 사용하는 것을 의미한다.

```html
<!-- 주석처리 -->
```

### HTML의 기본 구조

HTML의 기본 구조는 웹 문서를 작성할 때 반드시 들어가야 하는 기본적인 내용으로 크게는 문서 타입 정의와 <html> 요소로 구분한다.

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>HTML</title>
    </head>
    <body>
        <h1>Hello, HTML</h1>
    </body>
</html>
```

### 문서 타입 정의

문서 타입 정의는 보통 DTD(doctype)라고 부른다.

이 문서가 어떤 버전으로 작성되었는지 브라우저에 알려주는 선언문이며 반드시 문서 내 최상단에 선언되어야 한다.

### <html>요소

문서 타입 선언 후에는 <html> 태그가 나와야 하고, 자식으로는 <head> 태그와 <body> 태그가 있다.

<html> 태그의 lang 속성: 문서가 어느 언어로 작성되었는지를 의미

<head> 태그에 위치하는 태그들은 브라우저 화면에 표시되지 않는다.

대신 문서의 기본 정보 설정이나 외부 스타일 시트 파일 및 js 파일을 연결하는 등의 역할을 한다.

<meta> 태그의 charset 속성: 문자의 인코딩 방식을 지정

<body> 태그에 실제 브라우저 화면에 나타나는 내용들이 들어간다.

# HTML 태그

## HTML 태그 소개

현재 태그의 개수는 대략 130여 개

실제로 대다수의 웹 페이지는 대략 25개 정도의 서로 다른 태그가 사용된다.

## 제목과 단락 요소

### 제목 태그

제목(heading) 태그는 문서 내에 제목을 표현할 때 사용하는 태그이다.

<h1>~<h6>

### 단락 태그

단락(paragraph) 태그: <p></p>

### 개행

<p>를 사용해서 단락으로 구분하면 자연스럽게 개행이 된다.

그럼 <p> 내부에서 임의로 개행을 하려면 어떻게 해야 할까?

linebreak 를 줄여서 <br> 을 사용한다.

## 텍스트를 꾸며주는 요소

### 텍스트 표현 태그

- <b> : bold 글자를 굵게 표현하는 태그
- <i> : italic 글자를 기울여서 표현하는 태그
- <u> : underline 글자의 밑줄을 표현하는 태그
- <s> : strike 글자의 중간선을 표현하는 태그

## 앵커 요소

앵커 태그는 링크를 생성한다. 앵커 태그를 이용해 다른 페이지로 이동하거나 현재 페이지 내에서 특정 위치로 초점을 이동시킬 수 있다.

### <a>

```html
<a href="<http://www.naver.com/>" target="_blank">네이버</a>
```

### href 속성

링크를 만들기 위해 <a>는 반드시 href(hypertext reference) 속성을 가지고 있어야 한다.

### target 속성

target 속성은 링크된 리소스를 어디에 표시할지를 나타내는 속성이다.

_self: 현재 화면에 표시한다는 의미, 기본 값

_blank: 새로운 창에 표시한다는 의미

_parent, _top 은 잘 쓰이지 않음

### 내부링크

<a>를 통해 페이지 내부의 특정 요소로 초점을 이동할 수도 있는데, 이를 내부 링크라고 한다.

내부 링크를 사용할 때는 href 속성값에 #을 쓰고 그 뒤에 페이지 내에서 이동하고자 하는 요소의 id 속성값을 적으면 된다.

```html
<a href="#some-element-id">회사 소개로 이동하기</a>
```

## 의미가 없는 컨테이너 요소

태그 자체에 아무 의미가 없으며, 단순히 요소들을 묶기 위해 사용되는 태그이다.

<div>, <span>

### <div>태그와 <span>태그

div(division) 태그는 블록 레벨 태그이다.

블록 레벨 요소는 기본적으로 한 줄을 생성해서 내용을 표현하는 반면 span 태그는 인라인 레벨 태그이다.

## 리스트 요소

### <ul>

ul(unordered list) 태그는 순서가 없는 리스트를 표현할 때 사용한다.

```html
<ul> 
    <li> 콩나물</li> 
    <li> 파</li> 
    <li> 국  간장</li> 
    ... 
</ul>
```

### <ol>

ol(ordered list) 태그는 순서가 있는 리스트를 표현할 때 사용한다.

```html
<ol>
    <li>냄비에 국물용 멸치를 넣고 한소끔 끓여 멸치 육수를 7컵(1,400ml) 만든다.</li>
    <li>콩나물을 넣고 뚜껑을 덮어 콩나물이 익을 때까지 끓인다.</li>
    <li>뚜껑을 열고 대파, 마늘, 고춧가루를 넣고 끓인다.</li>
    ...
</ol>
```

### <dl>

dl(definition/description list)태그는 용어와 그에 대한 정의를 표현할 때 사용한다.

```html
<dl>
    <dt>리플리 증후군</dt>
    <dd>허구의 세계를 진실이라 믿고 거짓된 말과 행동을 상습적으로 반복하는 반사회적 성격장애를 뜻하는 용어</dd>
    <dt>피그말리온 효과</dt>
    <dd>타인의 기대나 관심으로 인하여 능률이 오르거나 결과가 좋아지는 현상</dd>
    <dt>언더독 효과</dt>
    <dd>사람들이 약자라고 믿는 주체를 응원하게 되는 현상</dd>
</dl>
```

- <dt> : 용어를 나타내는 태그
- <dd> : 용어에 대한 정의 또는 설명을 나타내는 태그

## 이미지 요소

### <img>

```html
<img src="./images/pizza.png" alt="피자">
```

### src 속성

<img>의 필수 속성으로 이미지의 경로를 나타내는 속성이다.

### alt 속성

이미지의 대체 텍스트를 나타내는 속성이다.

### width/height 속성

이미지의 가로/세로 크기를 나타내는 속성이다.

### 상대경로와 절대경로

src 속성에는 이미지의 경로가 들어가며 이미지의 상대경로와 절대경로가 있다.

상대경로: 현재 웹 페이지를 기준으로 상대적으로 이미지의 위치를 나타내는 경로

절대경로: 실제 그 이미지가 위치한 곳의 전체 경로

```html
<!-- 상대경로 -->
<img src="./images/pizza.png" alt="피자">

<!-- 절대경로 -->
<img src="C:/users/document/images/pizza.png" alt="피자">
<img src="<http://www.naver.com/pizza.png>" alt="피자">
```

## 테이블 요소

### 표의 구성 요소

- <table> : 표를 나타내는 태그
- <tr> : 행을 나타내는 태그
- <th> : 제목 셀을 나타내는 태그
- <td> : 셀을 나타내는 태그

하나의 <table>은 하나 이상의 <tr>로 이루어져 있으며, <tr>은 셀을 나타내는 <th>, <td>를 자식으로 가지게 된다.

표를 구성할 때는 위에서 밑으로, 좌측에서 우측으로 작성하면 된다.

### 표의 구조와 관련된 태그

- <caption>: 표의 제목을 나타내는 태그
- <thead>: 제목 행을 그룹화하는 태그
- <tfoot>: 바닥 행을 그룹화하는 태그
- <tbody>: 본문 행을 그룹화하는 태그

## 폼 요소

사용자로부터 데이터를 받아야 하는 경우 사용되는 요소들을 폼 요소라고 한다.

### type

```html
<input type="text" placeholder="ㅇㅇㅇ">

<input type="password">

<input type="radio" name="gender">남자
<input type="radio" name="gender">여자

<input type="checkbox" name="hobby"> 등산
<input type="checkbox" name="hobby"> 독서
<input type="checkbox" name="hobby"> 운동

<input type="file">
<form action="./test.html">
    메시지: <input type="text" name="message"><br>
    <input type="submit">
    <input type="reset">
    <input type="image" src="<http://placehold.it/50x50?text=click>" alt="click" width="50" height="50">
    <input type="button" value="버튼">
</form>
```

- submit : form의 값을 전송하는 버튼
- reset : form의 값을 초기화하는 버튼
- image : 이미지를 삽입할 수 있는 버튼 (submit과 동작이 동일함)
- button : 아무 기능이 없는 버튼

```html
<select>
    <option>서울</option>
    <option>경기</option>
    <option>강원</option>
    ...
</select>
<textarea rows="5" cols="30">
    ...
</textarea>
```

- cols : 가로 크기를 조절하는 속성(한 줄에 들어가는 글자의 수)
- rows : 세로 크기를 조절하는 속성(화면에 보여지는 줄 수)

```html
<button type="submit|reset|button">ㅇㅇㅇ</button>
<label for="name">이름</label>: <input type="text" id="name"><br>
<label for="nickname">이름</label>: <input type="text" id="nickname"><br>
<label for="address">이름</label>: <input type="text" id="address"><br>
```

<label>은 form 요소의 이름과 form 요소를 명시적으로 연결시켜주기 위해 사용한다.

form 요소의 id 속성값과 <label>의 for 속성값을 같에 적어주어야 한다.

```html
<form action="" method="">
    <fieldset>
        <legend>기본 정보</legend>
        ... 폼 요소들 ...
    </fieldset>
    <fieldset>
        <legend>부가 정보</legend>
        ... 폼 요소들 ...
    </fieldset>
</form>
```

- <fieldset> : 여러 개의 폼 요소를 그룹화하여 구조적으로 만들기 위해 사용
- <legend> : 폼 요소의 제목으로 <fieldset> 내부에 작성

<form>은 form 요소들을 감싸는 태그로 데이터를 묶어서 실제 서버로 전송해주는 역할을 하는 태그이다.

form의 속성

- action: 데이터를 처리하기 위한 서버의 주소
- method: 데이터를 전송하는 방식을 지정

method 속성값

- get: 데이터가 전송될 때 주소창에 파라미터 형태로 붙어 데이터가 노출된다.
- post: 데이터가 전송될 때 데이터가 노출되지 않는다.

# 콘텐츠모델, 시멘틱마크업, 블록 & 인라인

## 콘텐츠 모델

### Content Models의 7분류

1. *Metadata Content*
2. *Flow Content*
3. *Sectioning Content*
4. *Heading Content*
5. *Phrasing Content*
6. *Embedded Content*
7. *Interacitve Content*

### 1. Metadata

"base, link, meta, noscript, script, style, title"

Metadata에는 콘텐츠의 스타일, 동작을 설정하거나 다른 문서와의 관계 등 정보를 포함하는 요소들이 포함된다.

메타 태그, 타이틀 태그, 스타일 태그, 링크 태그가 이에 해당하며 대부분 <head>내에 들어간다.

### 2. Flow

"a, abbr, address,maparea, article, aside,audio, b, bdo, blockquote,br, button, canvas, cite, code, datalist, del, details, dfn, div, dl, em, embed, fieldset, figure, footer, form, h1 ~ h6, header, hgroup, hr, i, iframe, img, input, ins, kbd, keygen, label, map, mark, math, menu, meter, nav, noscript, object, ol, output, p, pre, progress, q, ruby, samp, script, section, select, small, span, strong, style[scoped], sub, sup, svg, table, textarea, time, ul, var, video, wbr"

Flow에는 문서의 자연스러운 흐름에 의해 배치되는 요소들이 포함된다.

### 3. Sectioning

"article, aside, nav, section“

문서의 구조와 관련된 요소들이 포함된다.

### 4. Heading

"h1, h2, h3, h4, h5, h6“

각 section의 header를 정의하는 heading 태그가 포함된다.

### 5.Phrasing

"a, abbr, map, area, audio, b, bdo, br, button, canvas, cite, code, datalist, del, dfn, em, embed, i, iframe, img, input, ins, kbd, keygen, label, map, mark, math, meter, noscript, object, output, progress, q, ruby, samp, script, select, small, span, strong, sub, sup, svg, textarea, time, var, video, wbr"

문서의 텍스트 또는 텍스트를 꾸며주는 문단 내부 레벨로 사용되는 요소들이 포함된다.

### 6. Embedded

"audio, canvas, embed, iframe, img, math, object, svg, video"

외부 콘텐츠를 표현하는 요소들이 포함되며 오디오나 비디오, 이미지 등 멀티미디어 관련 요소들이 해당된다.

### 7.Interactive

"a, audio[controls], button, details, embed, iframe, img[usemap], input, keygen, label, menu, object[usemap], select, textarea, video[controls]"

사용자와 상호작용을 하는 요소들이 포함된다.

## 시멘틱 마크업

검색 엔진 최적화는 HTML 코드에서 정보를 모아 검색 키워드에 맞는 적절한 웹사이트를 구성하여 검색 결과의 상위에 나올 수 있도록 하는 작업이다.

해당 웹페이지의 내용을 파악하고 검색엔진에 노출이 잘 되도록 하기 위해서는 HTML 요소를 적절하게 사용한 시멘틱한 마크업이 필요하다.

### 블록 레벨 요소

부모 요소의 가로 영역에 맞게 꽉 채워져 표현되는 요소

블록 레벨 요소는 일반적인 모든 요소(블록, 인라인 레벨 등)를 포함할 수 있다.

"div, h1~h6, p, ul, li, table ...”

### 인라인 레벨 요소

하나의 라인 안에서 자신의 내용만큼의 박스를 만드는 요소

인라인 레벨 요소는 블록 레벨 요소를 포함할 수 없다.

" span, i, img, em, strong, a ...”
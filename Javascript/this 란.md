# this 란?

### 1-1 그냥 쓰거나 함수 안에서 쓰면 this는 window를 뜻한다.

```js
console.log(this)
// Window {window: Window, self: Window, document: document, name: '', location: Location, …}

function this가뭘까(){
    console.log(this)
}
this가뭘까();
// Window {window: Window, self: Window, document: document, name: '', location: Location, …}
```

똑같이 window라고 출력된다.

**window는 모든 전역변수, 함수, DOM을 보관하고 관리하는 전역객체**

**전역변수 : 코드 내 모든 곳에서 참조해서 쓸 수 있는 범용적인, 범위가 넓은 변수**



### 1-2 strict mode일 때 함수 안에서 쓰면 this는 undefined

```javascript
<script>
    'use strict';

	function 함수(){
        console.log(this)
    }
	함수();
</script>
```

페이지 최상단에 'use strict'라는 키워드를 추가하면 strict mode로 자바스크립트를 작성할 수 있다.

strict mode에선 var 키워드 없이 변수를 선언하거나, 변수를 이상한 키워드로 선언하거나 하는 실수를 방지해준다.

strict mode에선 this 키워드를 일반함수 안에서 불렀을 때 undefined라는 값으로 강제로 지정해준다.



### 2 object 자료형 내에 함수들이 있을 때 거기서 this값은 '주인님'을 뜻한다

object 자료형에 함수를 넣을 수 있다

```js
var object1 = {
    data : 'Yun',
    함수 : function(){ console.log(this) }
}
object1.함수();
```

object에 들어가는 함수들을 메소드 method라고 부른다.

메소드 안에 this를 쓰면 `{data: 'Yun', 함수: ƒ}` 출력된다. 

= 메소드안에 this를 쓰면 **this는 메소드를 가지고있는 오브젝트**를 뜻한다



### 3 constructor 안에서 쓰면 constructor로 새로 생성되는 object를 뜻한다

자바스크립트에서 object를 비슷한걸 여러개 만들고 싶을 경우 object를 복사하는게 아니라 constructor라는 걸 만들어서 사용한다

**constructor는 object를 복사해서 생성해주는 기계**

```js
function 복사해주는기계(){
    this.이름 = 'Yun'; // 새로 생성되는 object의 이름 key값에 'Yun'이라는 value를 넣어주세요
}
```

여기서 this는 **기계로부터 새로 생성될 object**들을 의미한다.

```js
function 기계(){
    this.이름 = 'Yun'
}
var 오브젝트 = new 기계();
```

이렇게 new 키워드를 이용하면 새로운 오브젝트를 꺼낼 수 있다.

새로운 오브젝트는 this라는 키워드 덕분에 {이름: 'Yun'} 이라는 값을 가지고 있다



### 4 eventlistener 안에서 쓰면 this는 e.currentTarget이라는 의미

```js
document.getElementById('버튼').addEventListener('click', function(e){
    console.log(this)
})
```

여기서 this는 e.currentTartget이라는 뜻과 똑같은 의미이다

**e.currentTarget은 지금 이벤트가 동작하는 곳**을 뜻한다

지금 addEventListenter 부착된 HTML 요소를 뜻한다



#### arrow function을 쓰면 내부에서 this값을 쓸 때 밖에 있던 this값을 그대로 사용한다

```js
var 오브젝트1 = {
    함수 : function(){ console.log(this) }
}
오브젝트1.함수();
// 오브젝트1이 출력된다

var 오브젝트2 = {
    함수 : () => { console.log(this) }
}
오브젝트2.함수();
// window가 출력된다
```

this 값을 함수를 만나면 항상 변하는데 arrow function 안에서는 변하지 않고 밖에 있던 this를 그대로 쓴다.
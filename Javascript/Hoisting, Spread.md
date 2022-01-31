# Hoisting, Spread

### 자바스크립트 변수, 함수의 Hoisting 현상

자바스크립트는 변수나 함수의 선언부분을 변수의 범위 맨 위로 강제로 끌고가서 가장 먼저 해석한다

```js
function 함수(){
    console.log('hello');
    var 이름 = 'Yun';
}
```

```js
function 함수(){
    var 이름;
    console.log('hello');
    이름 = 'Yun';
}
```

let 변수는 Hoisting이 되긴 하지만 undefinde라는 값이 할당되지 않는다



#### ES6 Spread Operator

**괄호제거 해주는 연산자**

#### 1. Array 합치기/복사에 매우 자주 쓴다

```js
var a = [1,2,3];
var b = [4,5];
var c = [...a, ...b]; // [1,2,3,4,5]
```

a 라는 array를 복사해서 b를 만들고싶으면?

```js
var a = [1,2,3];
var b = a;
```

이렇게하면 안돼!!!

등호로 복사를 하면 a와 b 변수는 [1,2,3]을 각각 따로 하나씩 가진게 아니라 **값 공유**가 일어난다

그래서 a라는 array를 수정하면 b도 똑같이 바뀜

등호를 쓰면 값을 복사한게 아니라 **[1,2,3] 값이 저기 있어요~라고 가리키는 화살표**를 복사한 것이다

```js
var a = [1,2,3];
var b = [...a];
```

#### 2. Object 합치기/복사에 매우 자주 쓴다

```js
var o1 = {a:1, b:2};
var o2 = {c:3, ...o1};

var o1 = {a:1, b:2};
var o2 = {a:3, ...o1};
console.log(o2); // {a: 1, b: 2}
```

오브젝트의 key값이 중복되면?

**무조건 뒤에 오는a**가 이긴다. 

#### 3. array를 파라미터 형태로 집어넣고 싶을 때 쓴다

```js
function 더하기(a,b,c){
    console.log(a + b + c)
}
var 어레이 = [10, 20, 30];
더하기(...어레이);
```


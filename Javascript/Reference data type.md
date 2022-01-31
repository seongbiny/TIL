# Reference data type

### Primitive data type

자바스크립트의 자료형(문자, 숫자, array, object 등)은 크게 2개로 분류한다

Primitive & reference

Primitive data type들은 자료 자체가 변수에 저장되는 자료들이다. (문자, 숫자 자료형들)

```js
var name = 'seongbin';
var age = 27;
```

문자나 숫자 자료형은 문자나 수자가 변수에 직접 저장된다



### Reference data type

Array, Object 자료형은 reference data type에 속한다.

reference data type은 자료를 변수에 직접 저장하는게 아닌, 자료가 저쪽에 있습니다 라는 **화살표 (레퍼런스)**를 변수에 저장한다.

```js
var 사람 = {name : 'Yun'};
```

변수에 저장된건 {name : 'Yun'} 이 아니다

**{name : 'Yun'} 값을 가리키는 화살표**가 저장되어있을 뿐이다


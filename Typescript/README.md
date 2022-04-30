# TypeScript

> JavaSript + Type문법
>
> 자바스크립트의 타입부분을 업그레이드해서 사용하고싶을 때 설치해서 쓰는 일종의 자바스크립트의 대용품
>
> 완전 다른 언어는 아니라 자바스크립트 문법 그대로 이용가능한데 타입문법을 업그레이드해서 쓸 수 있다.

#### 일반 HTML CSS JS 웹 개발시 타입스크립트 사용하려면?

- nodejs 최신버전 설치

- ```
  $ npm install -g typescript
  ```

- `tsconfig.json` 파일 생성

- index.ts 파일에 코딩 시작

#### React 프로젝트에서 타입스크립트 사용하려면?

* 이미 있는 React 프로젝트에 설치

  * ```
    npm install --save typescript @types/node @types/react @types/react-dom @types/jest
    ```

  * .js 파일을 .ts 파일로 바꿔서 이용

* React 프로젝트를 새로 만들거면

  * ```
    npx create-react-app my-app --template typescript
    ```

## 타입스크립트 기본 타입 정리 (primitive types)

> 변수 만들 때 타입 정하기 (타입 실드씌우기)

```typescript
// String
let str: string = 'hi';
// Number
let num: number = 10;
// Boolean
let isLoggedIn: boolean = false;
// Array
let arr: number[] = [1,2,3];
let arr: Array<number> = [1,2,3];
// Tuple
let arr: [string, number] = ['hi', 10];
// Any 모든 타입에 대해서 허용
let str: any = 'hi';
let num: any = 10;
// Void 변수에는 undefined와 null만 할당하고, 함수에는 반환 값을 설정할 수 없는 타입
let unuseful: void = undefined;
function notuse(): void {
    console.log('sth');
}
// Never 함수의 끝에 절대 도달하지 않는다는 의미
function neverEnd(): never {
    while (true) {
        
    }
}
```

### But, 변수 생성시 타입스크립트가 타입을 자동으로 부여해준다.

## 타입을 미리 정하기 애매할 때 (union type, any, unknown)

#### 가장 좋은 Union type 사용

```typescript
let 이름 :string | number = 'kim';
let 나이 :(string | number) = 100;
```

할당하는 순간 타입은 string 또는 number 중 하나로 변한다.

```typescript
var array :(number | string)[] = [1, '2', 3]
var object :{data : (number | string) } = { data : '123' }
```

#### any 타입

아무 자료나 집어넣을 수 있는 타입 = 실드해제

```typescript
let 이름 :any = 'kim';
이름 = 123;
이름 = undefined;
이름 = [];
```

막쓰면 안됨 타입관련 버그가 생길 경우 왜 그런지 추적하기가 어렵다

비상시 쓰는 **변수 타입체크 해제기능** 이런 용도로만 사용

#### any 보다는 unknown 타입 사용

1. unknown 타입엔 모든 자료 다 집어넣을 수 있다.
2. 자료집어넣어도 타입은 그대로 unknown 이다.

```typescript
let 이름 :unknown;
let 변수1 :string = 이름;
let 변수2 :boolean = 이름;
let 변수3 :number = 이름;

let 이름 :unknown;
이름[0];
이름 - 1;
이름.data;
```

nuknown 타입을 다른 곳에 집어 넣으려고 하면 에러가 난다. (any는 에러안남)

왜냐면 타입스크립트는 정확하고 확실한걸 좋아한다.

확실하지않은 타입에 뺄셈해주는거 싫어한다.

아직 뭘 집어넣을지 모르겠는데 약간의 안전성을 도모하고 싶으면 unknown 타입을 쓴다.

현실은 any, unknown 부여할 경우 별로 없음

## 함수에 타입 지정하는 법 & void 타입

> 함수에 타입지정 2곳 가능
>
> 1. 파라미터
> 2. return

```typescript
function 함수(x :number) :number {
    return x * 2
}
```

#### 함수는 void 타입이 있음

return할 자료가 없는 함수의 타입으로 사용가능하다.

> 파라미터가 옵션일 경우

함수에 파라미터자리를 만들어놨지만 가끔 파라미터 없이 쓸 때도 있다.

그럴 경우 타입스크립트에선 미리 "이 파라미터는 옵션임" 정의를 해줘야 에러가 나지 않는다.

```typescript
function 함수(x? :number) {
    
}
함수(); // 가능
함수(2); // 가능
```

**물음표는 `x : number | undefined` 와 똑같은 의미이다**

파라미터가 정의 안되면 자동으로 undefined가 되는걸 반영한 의미

> 함수도 Union type을 사용하면?

Q. 예를 들어 함수에 숫자 또는 문자를 넣었을 때 +1 해주는 함수를 만들어보자

```typescript
function 함수(x :number | string){
    return x + 1
}

function 함수(x? :number) :number {
    return x * 2
}

// 둘 다 에러
```

1.  타입을 하나로 Narrowing 해주거나
2.  Assert 해주거나

## 타입 확정하기 Narrowing & Assertion

## Type Narrowing

> if문 등으로 타입을 하나로 정해주는 것

```typescript
function 함수(x :number | string){
    if (typeof x === 'number') {
        return x + 1
    }
    else if (typeof x === 'string') {
        return x + 1
    }
    else {
        return 0
    }
}
```

- 꼭 typeof를 쓸 필요는 없고 타입을 하나로 확정지을 수 있는 코드라면 어떤 것도 Narrowing 역할을 할 수 있다
- in, instanceof 키워드도 사용 가능

## Type Assertion

> "이 변수의 타입을 number로 생각해주세요"
>
> **변수명 as string**

```typescript
function 함수(x :number | string){
    return (x as number) + 1
}
console.log( 함수(123) )
```

변수명 as number = "나는 이 변수를 number라고 주장하겠습니다~"

as 키워드 사용 시 특징

1. as 키워드는 union type 같은 복잡한 타입을 하나의 정확한 타입으로 줄이는 역할을 수행
2. 타입실드 임시 해제용. 실제 코드 실행결과는 as 있을 때나 없을 때나 거의 동일

as 쓰면 간편하지만 정확히 코드짜려면 narrowing을 씁시다.

as 키워드는 타입을 개발자 맘대로 주장하는 역할이라 엄격한 타입체크기능을 잠깐 안쓰겠다는 뜻과 동일

as 문법은 이럴 때 쓰도록 합시다.

1. 왜 타입에러가 나는지 정말 모르겠는 상황에 임시로 에러해결용으로 사용
2. 내가 어떤 타입이 들어올지 정말 확실하게 알고 있는데 컴파일러 에러가 방해할 때

## 타입도 변수에 담아쓰세요 type 키워드 써서 & readonly

```typescript
let 동물 :string | number | undefined;
```

코드를 열심히 짜다보면 매우 길고 복잡하게 타입을 나열하는 경우가 많다.

1. 이게 길고 보기 싫거나
2. 나중에 또 사용하고 싶으면

변수에 담아 쓰자

```typescript
type Animal = string | number | undefined;
let 동물 :Animal;
```

`type 타입변수명 = 타입종류`

타입을 변수처럼 만들어서 쓰는 alias 문법. 관습적으로 대문자로 시작한다.

일반 자바스크립트 변수랑 차별을 두기 위해 AnimalType 이런 식으로 작명하는 걸 추천

#### object 타입도 저장가능

```typescript
type 사람 = {
    name : string,
    age : number,
}

let teacher :사람 = { name : 'john', age : 20 }
```

type 키워드를 안쓴다면?

```typescript
let teacher :{
    name : string,
    age : number,
} = { name : 'john', age : 20 }
```

#### readonly 로 잠그기

```typescript
const 출생지역 = 'seoul';
출생지역 = 'busan'; // const 변수는 여기서 에러남
```

```typescript
const 남친 = {
    name : '은우'
}
남친.name = '강준'; // const 변수지만 에러안남
```

object 자료를 const에 집어넣어도 object 내부는 마음대로 변경가능

const 변수는 재할당만 막아줄 뿐이지 그 안에 있는 object 속성 바꾸는 것 까지 관여하지 않기 때문

object 속성을 바뀌지 않게 막고 싶으면 타입스크립트 문법을 쓰자!

```typescript
type Boyfriend = {
    readonly name : string,
}
let 남친 :Boyfrined = {
    name : '은우'
}
남친.name = '강준' // readonly라서 에러남
```

readonly 키워드는 속성 왼쪽에 붙일 수 있으며 특정 속성을 변경불가능하게 잠궈준다.

한 번 부여된 후엔 앞으로 바뀌면 안될 속성들을 readonly로 잠궈서 쓰자

#### 속성 몇 개가 선택사항이라면?

어떤 object 자료는 color, width 속성이 둘 다 필요하지만, 어떤 object 자료는 color 속성이 선택사항이라면 type alias를 여러개 만들어야하는게 아니라 물음표연산자만 추가하면 된다.

```typescript
type Square = {
    color? : string,
    width : number,
}
let 네모2 :Square = {
    width : 100
}
```

물음표는 **"undefined 라는 타입도 가질 수 있다~"** 라는 뜻임을 잘 기억해두자

#### type 키워드 여러 개 합치기

```typescript
type Name = string;
type Age = number;
type NewOne = Name | Age;

type PositionX = { x :number };
type PositionY = { y :number };
type XandY = PositionX & PositionY // { x :number, y :number }
let 좌표 :XandY = { x : 1, y : 2 }
```

object에 지정한 타입도 `&` 사용해서 합치기 가능 

#### type 키워드는 재정의가 불가능

```typescript
type Name = string;
type Name = number;
// 에러발생
```

## Literal Types로 만드는 const 변수 유사품

> 어떤 변수가 미리 골라놓은 데이터만 가질 수 있게 도와준다

```typescript
let apple :'사과';
let banana :'바나나';
```

특정 글자나 숫자만 가질 수 있게 제한을 두는 타입 = literal type

```typescript
let 방향 :'left' | 'right';
방향 = 'left';

function 함수(a :'hello') :1| 0 | -1 {
    return 1
}
```

```typescript
var 자료 = {
    name : 'kim'
}
function 함수(a :'kim') {
    
}
함수(자료.name)
// 에러남
// 함수는 'kim'타입만 입력할 수 있다.
// 자료.name 은 string타입이다.

var 자료 = {
    name : 'kim'
} as const;
function 함수(a :'kim') {
    
}
함수(자료.name)
```

`as const` 의 효과

1. 타입을 object의 value로 바꿔준다. (타입을 'kim'으로 바꿔준다.)
2. object안에 있는 모든 속성을 readonly로 바꿔준다. (변경하면 에러남)

## 함수와 methods에 type alias 지정하는 법

```typescript
type NumOut = ( x :number, y :number ) => number;
let ABC :NumOut = function(x,y){
    return x + y
}
```

```typescript
let 회원정보 = {
    name : 'kim',
    age : 30,
    plusOne (x){
        return x + 1
    },
    changeName : () => {
        console.log('안녕')
    }
}
회원정보.plusOne(1);
회원정보.changeName();
```



## 타입스크립트에서의 함수

1. 함수의 파라미터(매개변수) 타입
2. 함수의 반환 타입
3. 함수의 구조 타입

### 함수의 기본적인 타입 선언

```typescript
function sum(a: number, b: number): number {
    return a + b;
}
// 함수의 반환 값에 타입을 정하지 않을 때는 void라도 사용
```

### 함수의 인자

타입스크립트에서는 함수의 인자를 모두 필수 값으로 간주한다. 따라서 함수의 매개변수를 설정하면 `undefined`나 `null`이라도 인자로 넘겨야하며 컴파일러에서 정의된 매개변수 값이 넘어 왔는지 확인한다. 정의된 매개변수 값만 받을 수 있고 추가로 인자를 받을 수 없다!

```typescript
function sum(a: number, b?: number): number {
    return a + b;
}
sum(10); // 10
sum(10, 20); // 30
sum(10, 20, 30); // error
```


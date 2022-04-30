# TypeScript

## 기본타입

> 타입스크립트로 변수나 함수와 같은 자바스크립트 코드에 타입을 정의할 수 있다.

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

## 함수

웹 애플리케이션을 구현할 때 자주 사용되는 함수는 타입스크립트로 크게 3가지 타입을 정의할 수 있다.

* 함수의 파라미터(매개변수) 타입
* 함수의 반환 타입
* 함수의 구조 타입

### 함수의 기본적인 타입 선언

```typescript
function sum(a: number, b: number): number {
    return a+b;
}
```

Tip! 함수의 반환 값에 타입을 정하지 않을 때는 `void`라도 사용한다.

### 함수의 인자

타입스크립트에서는 함수의 인자를 모두 필수 값으로 간주한다. 함수의 매개변수를 설정하면 `undefined`나 `null`이라도 인자로 넘겨야하며 컴파일러에서 정의된 매개변수 값이 넘어 왔는지 확인한다. **정의된 매개변수 값만 받을 수 있고 추가로 인자를 받을 수 없다는 의미**이다.

```typescript
function sum(a: number, b: number): number {
    return a + b;
}
sum(10, 20); //30
sum(10, 20, 30); // error
sum(10); // error
```

정의된 매개변수의 갯수 만큼 인자를 넘기지 않아도 되는 자바스크립트의 특성을 살리고 싶다면 `?`를 이용한다.

```typescript
function sum(a: number, b?: number): number {
    return a + b;
}
sum(10, 20); // 30
sum(10, 20, 30); // error
sum(10); //10
```

## 인터페이스

> 인터페이스는 상호 간에 정의한 약속 혹은 규칙을 의미한다. 타입스크립트에서의 인터페이스는 보통 다음과 같은 범주에 대해 약속을 정의할 수 있다.

* 객체의 스펙(속성과 속성의 타입)
* 함수의 파라미터
* 함수의 스펙(파라미터, 반환 타입 등)
* 배열과 객체를 접근하는 방식
* 클래스

### 인터페이스 예

```typescript
let person = { name: 'seongbin', age: 27};

function logAge(obj: { age: number }) {
    console.log(obj.age); 
}
logAge(person); // 27
```

여기에 인터페이스를 적용하면?

```typescript
interface personAge {
    age: number;
}

function logAge(obj: personAge) {
    console.log(obj.age);
}
let person = { name: 'seongbin', age: 27 };
logAge(person);
```

**`logAge()`의 인자는 `personAge`라는 타입을 가져야한다!**

### 옵션 속성

> 인터페이스를 사용할 때 인터페이스에 정의되어 있는 속성을 꼭 모두 다 사용하지 않아도 된다. 이를 옵션 속성이라고 한다.

```typescript
interface 인터페이스_이름 {
    속성?: 타입;
}
```

속성 끝에 `?`를 붙인다.

```typescript
interface CraftBeer {
  name: string;
  hop?: number;  
}

let myBeer = {
  name: 'Saporo'
};
function brewBeer(beer: CraftBeer) {
  console.log(beer.name); // Saporo
}
brewBeer(myBeer);
```

`hop` 속성은 옵션 속성이기 때문에 없어도 에러 안남

### 읽기 전용 속성

> 읽기 전용 속성은 인터페이스로 객체를 처음 생성할 때만 값을 할당하고 그 이후에는 변경할 수 없는 속성을 의미한다. `readonly` 속성을 앞에 붙인다.

```typescript
interface CraftBeer {
    readonly brand: string;
}

let myBeer: CraftBeer = {
  brand: 'Belgian Monk'
};
myBeer.brand = 'Korean Carpenter'; // error!
```

### 읽기 전용 배열

> 배열을 선언할 때 `ReadonlyArray<T>` 타입을 사용하면 읽기 전용 배열을 생성할 수 있다.

```typescript
let arr: ReadonlyArray<number> = [1,2,3];
arr.splice(0,1); // error
arr.push(4); // error
arr[0] = 100; // error
```

`ReadonlyArray`로 선언하면 배열의 내용을 변경할 수 없다!

### 객체 선언과 관련된 타입 체킹

> 타입스크립트는 인터페이스를 이용하여 객체를 선언할 때 좀 더 엄밀한 속성 검사를 한다.

```typescript
interface CraftBeer {
    brand?: string;
}

function brewBeer(beer: CraftBeer) {
    // ..
}
brewBeer({ brandon: 'what' }); // error: Object literal may only specify known properties, but 'brandon' does not exist in type 'CraftBeer'. Did you mean to write 'brand'?
```

`CraftBeer` 인터페이스에는 `brand`라고 선언되어 있지만 `brewBeer()` 함수에 인자로 넘기는 `myBeer` 객체에는 `brandon`이 선언되어 있어 에러가 난다.

이런 타입 추론을 무시하고 싶다면 아래와 같이 선언한다.

```typescript
let myBeer = { brandon: 'what' };
brewBeer(myBeer as CraftBeer);
```

그럼에도 불구하고 만약 인터페이스에 정의하지 않은 속성들을 추가로 사용하고 싶을 때는 아래와 같이 선언한다.

```typescript
interface CraftBeer {
    brand?: string;
    [propName: string]: any;
}
```

### 함수 타입

인터페이스는 함수의 타입을 정의할 때에도 사용할 수 있다.

```typescript
interface login {
    (username: string, password: string): boolean;
}

// 함수의 인자의 타입과 반환 값의 타입을 정한다.
let loginUser: login;
loginUser = function(id: string, pw: string) {
    console.log('로그인 했습니다.');
    return true;
}
```

### 인터페이스 확장

```typescript
interface Person {
    name: string;
}
interface Developer extends Person {
    skill: string;
}
let fe = {} as Developer;
fe.name = 'seongbin';
fe.skill = 'TypeScript';
```

여러 인터페이스를 상속받아 사용할 수 있다.

```typescript
interface Person {
    name: string;
}
interface Drinker extends Person {
    drink: string;
}
interface Developer extends Drinker {
    skill: string;
}
let fe = {} as Developer;
fe.name = 'seongbin';
fe.skill = 'TypeScript'
fe.drink = 'Beer';
```

## 이넘

## 연산자를 이용한 타입 정의

### Union Type

> 유니온 타입이란 자바스크립트의 OR 연산자(`||`)와 같이 A이거나 B이다 라는 의미이다.

```typescript
function logText(text: string | number) {
    // ...
}
```

`text`에는 문자열 타입이나 숫자 타입이 모두 올 수 있다. `|` 연산자를 이용하여 타입을 여러 개 연결하는 방식을 유니온 타입 정의 방식이라고 부른다.

### Union Type의 장점

```typescript
// any를 사용하는 경우
function getAge(age: any) {
    age.toFixed(); // 에러 발생, age의 타입이 any로 추론되기 때문에 숫자 관련된 API를 작성할 때 코드가 자동 완성되지 않는다.
    return age;
}

// 유니온 타입을 사용하는 경우
function getAge(age: number | string) {
    if (typeof age === 'number') {
        age.toFixed(); // 정상 동작, age의 타입이 `number`로 추론되기 때문에 숫자 관련된 API를 쉽게 자동완성 할 수 있다.
        return age;
    }
    if (typeof age === 'string') {
        return age;
    }
    return new TypeError('age must be number or string');
}
```

### Intersection Type

> 인터섹션 타입은 여러 타입을 모두 만족하는 하나의 타입을 의미한다.

```typescript
interface Person {
    name: string;
    age: number;
}
interface Developer {
    name: string;
    skill: number;
}
type Capt = Person & Developer;
```

`Capt`의 타입은 아래와 같다.

```typescript
{
    name: string;
    age: number;
    skill: string;
}
```

### Union Type을 쓸 때 주의할 점

유니온 타입은 OR, 인터섹션은 AND라는 생각 멈춰 !

```typescript
interface Person {
    name: string;
    age: number;
}
interface Developer {
    name: string;
    skill: string;
}
function introduce(someone: Person | Developer) {
    someone.name; // O 정상 동작
    someone.age; // X 타입 오류
    someone.skill; // X 타입 오류
}
```

`introduce()` 함수의 파라미터 타입을 `Person`, `Developer` 인터페이스의 유니온 타입으로 정의했다. 유니온 타입은 A도 될 수 있고, B도 될 수 있는 타입이라고 생각하여 파라미터 타입이 `Person`도 되고 `Developer`도 될테니까 함수 안에서 당연히 이 인터페이스들이 제공하는 속성들인 `age`나 `skill`를 사용할 수 있겠지라는 생각 XXXX

타입스크립트 관점에서는 `introduce()` 함수를 호출하는 시점에 `Person` 타입이 올지 `Developer` 타입이 올 지 알 수가 없기 때문에 어느 타입이 들어오든 간에 오류가 안나는 방향으로 타입을 추론하게 된다.

```typescript
const capt: Person = { name: 'capt', age: 100 };
introduce(capt); // 만약 `introduce` 함수 안에서 `someone.skill` 속성을 접근하고 있으면 함수에서 오류 발생

const tony: Developer = { name: 'tony', skill: 'iron making' };
introduce(tony); // 만약 `introduce` 함수 안에서 `someone.age` 속성을 접근하고 있으면 함수에서 오류 발생
```

`introuce()` 함수 안에서는 별도의 **타입 가드(Type Guard)**를 이용하여 타입의 범위를 좁혀주지 않으면 `Person`과 `Developer` 두 타입에 공통적으로 들어있는 속성인 `name`만 접근할 수 있게 된다.

## 클래스

## 제네릭

> 재사용성이 높은 컴포넌트를 만들 때 자주 활용되는 특징이다. 특히, 한가지 타입보다 여러 가지 타입에서 동작하는 컴포넌트를 생성하는데 사용된다.

**제네릭이란 타입을 마치 함수의 파라미터처럼 사용하는 것**을 의미한다.

```typescript
function getText(text) {
    return text;
}

getText('hi'); // 'hi'
getText(10); // 10
getText(true); // true
```

제네릭은?

```typescript
function getText<T>(text: T): T {
    return text;
}

getText<string>('hi');
getText<number>(10);
getText<boolean>(true);

// 어떻게 동작하는 가?
function getText<string>(text: string): string {
  return text;
}
```

### 제네릭을 사용하는 이유

```typescript
function logText(text: string): string {
    return text;
}

// 여러 가지 타입을 허용하고 싶다면? `any` 사용
function logText(text: any): any {
    return text;
}
```

함수의 동작에 문제가 생기진 않지만 **함수의 인자로 어떤 타입이 들어갔고 어떤 값이 반환되는지는 알 수가 없다.**

이러한 문제점을 제네릭으로 해결할 수 있다.

```typescript
function logText<T>(text: T): T {
    return text;
}
```

함수의 이름 뒤에 `<T>`를 추가하면 함수의 인자와 반환 값에 모두 `T`라는 타입을 추가한다. 

```typescript
// 호출하는 방법 #1
const text = logText<string>("Hello Generic");
// 호출하는 방법 #2
const text = logText("Hello Generic");
```

### 제네릭 타입

제네릭 인터페이스

```typescript
function logText<T>(text: T): T {
    return text;
}
// #1
let str: <T>(text: T) => T = logText;
// #2
let str: {<T>(text: T): T} = logText;
// #1과 #2는 같은 의미
```

```typescript
interface GenericLogTextFn {
    <T>(text: T): T;
}
function logText<T>(text: T): T {
    return text;
}
// #1
let myString: GenericLogTextFn = logText; // Okay
// #2
let myString: GenericLogTextFn<string> = logText;
```

## 타입 추론

> 타입 추론이란 타입스크립트가 코드를 해석해 나가는 동작을 의미한다.

```typescript
let x = 3;
```

`x`에 대한 타입을 따로 지정하지 않더라도 일단 `x`는 `number`로 간주된다. 이렇게 변수를 선언하거나 초기화 할 때 타입이 추론된다. 이 외에도 변수, 속성, 인자의 기본 값, 함수의 반환 값 등을 설정할 때 타입 추론이 일어난다.

## 타입 호환

> 타입 호환이란 타입스크립트 코드에서 특정 타입이 다른 타입에 잘 맞는지를 의미한다.

```typescript
interface Ironman {
    name: string;
}

class Avengers {
    name: string;
}

let i: Ironman;
i = new Avengers(); // Ok
```

### 구조적 타이핑 예시

```typescript
interface Avengers {
    name: string;
}

let hero: Avengers;
// 타입스크립트가 추론한 capt의 타입은 { name: string; location: string; } 입니다.
let capt = { name: "Captain", location: "Pangyo"};
hero = capt;
```

## 타입 별칭

> 타입 별칭은 특정 타입이나 인터페이스를 참조할 수 있는 타입 변수를 의미한다.

```typescript
// string 타입을 사용할 때
const name: string = 'capt';

// 타입 별칭을 사용할 때
type MyName = string;
const name: MyName = 'capt';
```

```typescript
type Developer = {
    name: string;
    skill: string;
}

type User<T> = {
    name: T
}
```

### 타입 별칭의 특징

타입 별칭은 새로운 타입 값을 하나 생성하는 것이 아니라 정의한 타입에 대해 나중에 쉽게 참고할 수 있게 이름을 부여하는 것과 같다.

![image-20220429010716041](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220429010716041.png)

### type vs interface

타입 별칭과 인터페이스의 가장 큰 차이점은 **타입의 확장 가능 / 불가능 여부**이다.

인터페이스는 확장이 가능한데 타입 별칭은 확장이 불가능하다. 따라서 가능한 한 **`type`보다는 `interface`로 선언해서 사용하는 것을 추천**한다.

## Export, Import

`export`를 변수, 함수, 타입, 인터페이스 등에 붙여 사용한다.

```typescript
// math.ts
export interface Triangle {
    width: number;
    height: number;
}

// index.ts
import { Triangle } from './math.ts';

class SomeTriangle implements Triangle {
    // ...
}
```

## 타입스크립트에서 배열과 객체를 인덱싱 하는 방법

> 타입스크립트에서 배열 요소와 객체의 속성을 접근할 때는 인터페이스를 사용한다.

```javascript
// javascript

const arr = ['Thor', 'Hulk'];
arr[0]; // 'Thor'
```

```typescript
// typescript

interface StringArray {
    [index: number]: string;
}
const arr: StringArray = ['Thor', 'Hulk'];
arr[0]; // 'Thor'
```

### 타입으로 배열 변경 제한하기

배열에 강한 타입을 적용함과 동시에 배열의 요소를 변경하지 못하게 하려면?

```typescript
interface ReadonlyStringArray {
    readonly [index: number]: string;
}

const arr: ReadonlyStringArray = ['Thor', 'Hulk'];
arr[2] = 'Capt'; // error
```

## mapped type

맵드 타입이란 기존에 정의되어 있는 타입을 새로운 타입으로 변환해 주는 문법을 의미한다. 마치 자바스크립트 `map()` API 함수를 타입에 적용한 것과 같은 효과를 가진다.

### 자바스크립트에서 map 함수란?

```javascript
let arr = [{ id: 1, title: '함수'}, { id: 2, title: '변수'}, { id: 3, title: '인자'}];
let result = arr.map((item)=>{
    return item.title;
});
console.log(result); // ['함수', '변수', '인자'];
```

### 타입스크립트에서 맵드 타입의 기본 문법

```typescript
{ [ P in K ] : T }
{ [ P in K ] ? : T }
{ readonly [ P in K ] : T }
{ readonly [ P in K ] ? : T }
```

#### 맵드 타입 기본 예제

```typescript
type Heroes = 'Hulk' | 'Thor' | 'Capt';

type HeroProfiles = { [K in Heroes]: number };
const heroInfo: HeroProfiles = {
  Hulk: 54,
  Thor: 1000,
  Capt: 33,
}
```

...

## 타입스크립트에서의 타입이란?

- 타입 별칭 `type sn = number | string;`
- 인터페이스 `interface I { x: number[]; }`
- 클래스 `class C { }`
- 이넘 `enum E { A, B, C }`
- 타입을 가리키는 `import` 구문

## 자바스크립트 코드에 타입스크립트를 적용할 때 주의해야 할 점

- 기능적인 변경은 절대 하지 않을 것
- 테스트 커버리지가 낮을 땐 함부로 타입스크립트를 적용하지 않을 것
- 처음부터 타입을 엄격하게 적용하지 않을 것 (점진적으로 strict 레벨을 증가)
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
let 이름 :string = 'kim'
```

`변수명:타입` 

```typescript
let 나이 :number = 20;
let 결혼했니 :boolean = false;
```

#### array 또는 object 자료 안에도 타입 지정 가능

```typescript
let 회원들 :string[] = ['kim', 'park']
let 내정보 : { age : number } = { age : 20 }
```

`타입명[]`

**변수명 오른쪽에 오는 것들은 전부 타입지정 문법**이다

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


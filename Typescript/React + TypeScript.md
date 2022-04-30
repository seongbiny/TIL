# React + TypeScript 

기존 프로젝트에 타입스크립트 도입할 때 checklist

* 프로젝트 사이즈가 큰가?
* 협업 시 다른 사람이 짠 코드를 참조할 일이 많은가?
* 장기적으로 유지보수에 도움이 되는가?
* 나중에 팀원이 더 필요해도 인력수급이 쉽게 가능한가?
* 팀원들 학습에 필요한 시간과 비용이 적게 드는가?

## React에서 TS 문법을 어디에 써야하나? (4가지)

### 1. 일반 변수, 함수 타입지정

타입스크립트 배운대로 지정해주면 됨

### 2. JSX 타입지정

```typescript
let Box: JSX.Element = <div></div>
let Button: JSX.Element = <button></button>

let view: JSX.Element = <View></View>
```

더 정확히 타입지정하려면?

div, a, h4 와 같은 기본 태그들은 `JSX.IntrinsicElements` 라는 이름의 타입을 쓰면 된다.

```typescript
let Box: JSX.IntrinsicElements['div'] = React.createElement('div'); // <div></div>
let Button: JSX.IntrinsicElements['button'] = <button></button>
```

### 3. function component 타입지정

```react
function App() {
    return (
    	<div>안녕하세요</div>
    )
}
```

리액트의 컴포넌트 타입지정은? 

함수니까 파라미터와 return 타입지정 해주면 된다.

파라미터는 항상 props 니까 props가 어떤 타입인지 지정하면 됨

근데 컴포넌트는 JSX를 return한다. => return 타입에는 어떤 타입을 지정해야할까?

```typescript
type AppProps = {
    name: string;
};

function App (props: AppProps): JSX.Element {
    return (
    <div>{message}</div>
    )
}
```

return 타입은 `JSX.Element` 써주면된다. 근데 생략해도 자동으로 타입지정해줌

### 4. state 문법 사용 시 타입지정

state 만들 땐 그냥 자동으로 타입이 할당되어서 걱정할 필요는 없다.

state 타입이 나중에 변할 수도 있다? 그런 경우는 흔치 않겠지만 미리 지정해주면 된다.

```typescript
const [user, setUser] = useState<string | null>('yun');
```

`<>` 열고 타입을 넣으면 된다.

제네릭 문법 이용해서 타입을 useState 함수에 넣는 식으로 설정!



**타입스크립트 쓴다고 리액트 개발방식이 달라지는게 아님!**

함수 변수 정의부분 타입지정을 할 수 있다는것만 달라진다.

"props엔 무조건 { name: string }만 들어올 수 있습니다."

이런 문법만 작성해주면 됨!
# Redux toolkit + typescript

### redux 쓰는 이유

1. state를 한 곳에서 관리할 수 있어서 컴포넌트들이 props없이 state를 다루기 쉽다.
2. 수정방법을 미리 reducer라는 함수로 정의해놔서 state 수정 시 발생하는 버그를 줄일 수 있다.

* (전통방식) 기존 redux
* (신규방식) redux toolkit

## (전통방식 redux) state와 reducer 만들 때 타입지정 필요

### 버튼을 누르면 state가 +1, -1 되는 예제를 만들어보자.

```typescript
// index.ts

import { Provider } from 'react-redux';
import { createStore } from 'redux';

interface Counter {
    count : number
}

const initialState: Counter = { count: 0};

function reducer(state = num, action: any) {
    if (action.type === 'plus') {
        return { count: state.count + 1}
    } else if (action.type === 'minus'){
        return { count: state.count - 1}
    } else {
        return initialState
    }
}

const store = createStore(reducer);

// store의 타입 미리 export 해두기
export type RootState = ReturnType<typeof store.getState>
                                   
ReactDOM.render(
    <React.StrictMode>
    	<Provider store={store}>
      		<App />
    	</Provider>
  	</React.StrictMode>,
  	document.getElementById('root')
)
```

1. initialState = { count: 0 } // state 초기값 생성
2. function reducer를 만들어서 state가 변경되는 방법을 정의. 1. plus 2. minus

보이는 변수와 함수에 타입지정 해준다.

**(1) 초기값 변수 오른쪽에 타입지정 잘 해주기**

**(2) reducer 함수는 state, action 이 이름의 파라미터 2개 타입지정 잘 해주기**

state는 타입지정 필요없음 초기값 넣으면 타입지정 알아서 해줌

action은 나중에 dispatch 날릴 때 object 자료 넣는거랑 똑같이 생겨야 함

`{type: string, payload: number}` 이런거...

**(3) reducer 함수의 return 타입도 타입지정 해주기**

reducer 타입지정은 reducer 안의 코드들을 잘못 짜서 생기는 버그를 방지하는 용도!

App.tsx 에서 dispatch() 를 잘쓰냐 못쓰냐 캐치해주는게아님!

### (전통방식 redux) state를 꺼낼 때

redux에 있던 state를 가져오려면 `useSelector`훅을 사용, state를 변경하려면 `useDispatch`훅을 사용

```typescript
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Dispatch } from 'redux';
import { RootState } from './index';

function App() {
    const 꺼내온거 = useSelector( (state: RootState) => state );
    const dispatch: Dispatch = useDispatch();
    
    return (
    <div className="App">
    	{ 꺼내온거.count }
		<button onClick={()=>{dispatch({type : 'plus'})}}>버튼</button>
      	<Profile name="yun"></Profile>
    </div>
    )
}
```

1. `useSelector`를 쓰면 redux에 있던 state를 빼오기 쉽다. 안에 콜백함수 넣으면 거기 있던 파라미터가 그대로 state가 됨
2. `useDispatch`를 쓰면 redux로 수정요청을 날릴 수 있다. 

**(1) useSelector() 안에 파라미터 있는 곳에 타입지정**

state가 어떻게 생겼는지 파악한 다음 타입 손수 지정해주거나 아니면 index.ts에서 타입을 export해서 가져와도 된다.

index.ts에 있던 `export type RootState = ReturnType<typeof store.getState>`코드가 store의 타입을 미리 export 해두는 방법이다.

**(2) useDispatch도 타입지정하면 좋음**

import {Dispatch} from 'redux' 타입을 가져와서 `const dispatch: Dispatch` 쓰면 됨.



### (신규방식 redux) state와 reducer 만들 때 타입지정 필요

```bash
$ npm install redux react-redux
$ npm install @reduxjs/toolkit 
```

```typescript
import { createSlice, configureStore } from '@reduxjs/toolkit';
import { Provider } from 'react-redux';

const initialState = { count: 0, user : 'kim' };

const counterSlice = createSlice({
  name: 'counter',
  initialState : initialState,
  reducers: {
    plus (state){
      state.count += 1
    },
    minus (state){
      state.count -= 1
    },
    plusByAmount (state, action :any){
      state.count += action.payload
    }
  }
})

let store = configureStore({
  reducer: {
    counter1 : counterSlice.reducer
  }
})

//state 타입을 export 해두는건데 나중에 쓸 데가 있음
export type RootState = ReturnType<typeof store.getState>

//수정방법 만든거 export
export let {plus, minus, plusByAmount} = counterSlice.actions
```

하단에 `<Provider store={store}>` 추가해주면 끝!

1. createSlice() 로 slice 라는걸 만들어줍니다. slice는 state와 reducer를 합쳐놓은 새로운 뭉텅이

2. slice 안에는 slice 이름, state초기값, reducer가 정확한 이름으로 들어가야한다. 맘대로 작명 불가 

3. state는 그냥 맘대로 만들고 reducer는 함수 형태로 만들어주면 된다. 첫 파라미터는 state, 둘째는 actions가 자동으로 부여

4. 다 만든 것들은 configureStore 안에 등록.

5. 내가 만들어둔 reducer를 쓰고 싶으면 reducer 안의 함수명을 export 해준다.

**(1) state 초기값 타입지정은 알아서**

**(2) reducer 안의 action 파라미터의 타입지정** 

**(3) 나머지는 타입지정 필요없다. 자동임** 

`action`은 타입지정 방법이 따로 있다.

```typescript
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

(상단 생략)
  incrementByAmount (state, action: PayloadAction<number>){
      state.value += action.payload
  },
```

### (신규방식 redux) state를 꺼낼 때

```typescript
import { useDispatch, useSelector } from 'react-redux'
import {RootState, increment} from './index'

function App() {

  const 꺼내온거 = useSelector( (state :RootState) => state);
  const dispatch = useDispatch();

  return (
    <div className="App">
      {꺼내온거.counter1.count}
      <button onClick={()=>{dispatch(increment())}}>버튼</button>
    </div>
  );
} 
```

1. useSelector 함수를 쓰면 state를 쉽게 꺼낼 수 있다.

쓰는 법은 안에 콜백함수 ()=>{} 하나를 집어넣으면 되는데 그 함수의 첫 파라미터는 항상 state가 된다.

2. useDispatch 함수를 쓰면 쉽게 수정요청을 날릴 수 있다.

 

타입지정은 state와 dispatch에 해준다.

**(1) useSelector() 안의 파라미터에 타입지정**

state가 어떻게 생겼는지 파악한 다음 타입알아서 지정해주거나 아니면 

타입을 index.ts 이런 리듀서 만든 곳에서 미리 RootState라는 타입을 export 해두면 import 해서 쉽게 타입지정이 가능하다.

 

**(2) useDispatch() 사용할 때 타입지정 가능한데** 그냥 예전 방식처럼 하거나

아니면 공식 문서에서는 

index.ts에서 export type AppDispatch = typeof store.dispatch 해두고

App.tsx에서 import 해와서 useDispatch<AppDispatch>() 이렇게 타입지정하라고 되어있다.
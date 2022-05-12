# Next.js + mobile responsive [react-responsive]

`css media`로 반응형 처리를 해주면 css마다 일일이 구현해야해서 불편하고 귀찮다

=> [react-responsive](https://github.com/yocontra/react-responsive#react-responsive--) 사용하기

리브리브는 반응형이 아닌, 모바일 웹으로만 구현하기때문에 PC환경으로 접속시 모바일로 접속해달라는 안내 화면을 띄워줘야한다.

```jsx
const isMobile = useMediaQuery({
    query: "(max-width:767px)"
});
// ...
return(
	<>
    	{isMobile ?
    	<div>환영합니다.</div> :
    	<div>모바일로 접속해주세요.</div>
    	}
    </>
)
```

`isMobile`은 모바일 환경일 시 (width>767px) `true`를 return하고 아닐시에는 `false`를 return한다.

## Server Side Rendering

#### SSR vs CSR

* Server Side Rendering : 서버쪽에서 렌더링 준비를 끝 마친 상태로 클라이언트에 전달하는 방식 -> Next.js

* Client Side Rendering : 서버는 요청을 받으면 클라이언트에 HTML, JS를 보내준다. 클라이언트는 그것을 받아 렌더링을 시작한다. -> React

퍼포먼스, 혹은 검색 최적화 등의 목적을 위해 SSR을 구현해야 한다면 위의 코드를 그대로 사용하면 안된다.

* 이유

`Next의 SSR`은 `Server`에서 React 코드를 html, css, js 등으로 변환하여 응답해주는 방식을 띄고 있는데, 최초 응답 시 window 객체가 초기화 되지 않아 window에 대한 정보(width, height..)를 참조하지 않은 채로 데이터가 전송된다.

따라서 `isMobile`을 이용해서 모바일, PC 두 환경으로 나눠서 구현을 했다고 하더라고, 새로고침시에 나타나는 화면은 **window 정보를 모르기 때문에 기본 스타일이 적용**되어 나타나게 된다.

* 해결방법

SSR을 구현한다고 해도 Client Side에서 컴포넌트들이 마운트 되었을 때 `isMobile` 변수에 대한 정보를 업데이트 해주면 된다!

```jsx
// useState를 이용해서 isMobile state 생성
const [isMobile, setIsMobile] = useState(false);
const mobile = useMediaQuery({
    query: "(max-width:767px)"
});

useEffect(()=>{	// mobile 쿼리로 인해 값이 바뀔 때 수행
  if(mobile) setIsMobile(true);
},[mobile]);

// some codes...
return(
	<>
    	{isMobile ?
    	<div>환영합니다.</div> :
    	<div>모바일로 접속해주세요.</div>
    	}
    </>
)
```

컴포넌트가 마운트 되고 `isMobile` State를 업데이트 시켜서 컴포넌트 re-rendering을 발생시키면 원했던 대로 구현이 가능하다.

이를 커스텀 훅으로 만들어서 더 쉽게 사용할 수 있다.

```jsx
export function useIsMobile () {
  const [isMobile, setIsMobile] = useState(false);
  const mobile = useMediaQuery({query: "(max-width:767px)"});
  
  useEffect(()=>{
    setIsMobile(mobile);
  },[mobile]);

  return isMobile;
}
```


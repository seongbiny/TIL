# Next.js

```
npm run dev
```

```javascript
export const getServerSideProps = async()=>{
    const res = await fetch('url');
    const posts = await res.json();
    
    return {
        props: {
            posts
        }
    }
}
```

```javascript
<style jsx>
	{`
		nav {
			background-color: tomato;
		}
	`}    
</style>
```

```javascript
useEffect(() => {
    (async () => {
        const response = await fetch(
        `https://~~${}`
      	);
        const json = await response.json();
    })();
}, []);
```

```javascript
useEffect(() => {
    (async () => {
        const data = await (
        	await fetch(
            `https://~~${}`
           	);
        ).json();
    })();
}, []);
```

```javascript
useEffect(() => {
    (async () => {
        const { results } = await (
        	await fetch(
            `https://~~${}`
           	);
        ).json();
    })();
}, []);
```

![image-20220502012633024](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220502012633024.png)



## 라이브러리 vs 프레임워크

* 라이브러리 
  * 우리가 가져다쓰는 것
  * 사용자가 파일 이름이나 구조 등을 정하고 모든 결정을 내림

* 프레임워크 
  * 정해진 틀 안에서 커스터마이징
  * 파일 이름이나 구조 등을 정해진 규칙에 따라 만들고 따름

## pages 폴더 안에 있는 파일명에 따라 route가 결정된다.

pages/about.js 생성 ->

localhost:3000/about (O)

localhost:3000/about-us(X)

* index.js는 앱이 시작하는 파일, localhost:3000/ 

## SSR vs CSR

Server Side Rendering : 서버쪽에서 렌더링 준비를 끝 마친 상태로 클라이언트에 전달하는 방식 -> Next.js

Client Side Rendering : 서버는 요청을 받으면 클라이언트에 HTML, JS를 보내준다. 클라이언트는 그것을 받아 렌더링을 시작한다. -> React

### getServerSideProps

page에서 서버 측 렌더링 함수인 getServerSideProps함수를 export하는 경우 Next.js는 getServerSideProps에서 반환된 데이터를 사용하여 각 request에서 이 페이지를 pre-render한다. getServerSideProps는 서버 측에서만 실행되며 브라우저에서는 실행되지 않는다.

[타입스크립트로 사용하기](https://nextjs.org/docs/api-reference/data-fetching/get-server-side-props#getserversideprops-with-typescript)

[예시](https://github.com/FIN443/next-simple-movie-app/blob/0a6601664389101a563ffd952578b9060290904a/pages/index.tsx)



## Routing

페이지 간 클라이언트 측 경로 전환을 활성화하고 single-page app 경험을 제공하려면 `Link` 컴포넌트를 사용해야 한다.

```html
// 변경 전
<a href="/about">About</a>

// 변경 후
import Link from 'next/link';

<Link href="/about">
    <a>About</a>
</Link>
```

### `useRouter()`

앱의 함수 컴포넌트에서 router 객체 내부에 접근하려면 useRouter() 훅을 사용할 수 있다.

`const router = useRouter()`

## Styles JSX

Next.js를 사용하면 JavaScript 파일에서 CSS 파일을 가져올 수 있다.

`CSS-in-JS`

```jsx
<style jsx>{`
	div {
		color: red
	}
`}</style>
```


# transition & animation

### transform과 변형 함수

> 요소를 이동하거나 회전, 왜곡시키는 등 비교적 단순한 변형

`transform: 함수`

* 2차원 변형 함수

| 종류              | 설명                                           |
| ----------------- | ---------------------------------------------- |
| translate(tx, ty) | 지정한 크기만큼 x축, y축으로 이동합니다.       |
| translateX(tx)    | 지정한 크기만큼 x축으로 이동합니다.            |
| translateY(ty)    | 지정한 크기만큼 y축으로 이동합니다.            |
| scale(sx, sy)     | 지정한 크기만큼 x축과 y축으로 확대∙축소합니다. |
| scaleX(sx)        | 지정한 크기만큼 x축으로 확대∙축소합니다.       |
| scaleY(sy)        | 지정한 크기만큼 y축으로 확대∙축소합니다.       |
| rotate(각도)      | 지정한 각도만큼 회전합니다.                    |
| skew(ax, ay)      | 지정한 각도만큼 x축과 y축으로 왜곡합니다.      |
| skew(ax)          | 지정한 각도만큼 x축으로 왜곡합니다.            |
| skew(ay)          | 지정한 각도만큼 y축으로 왜곡합니다.            |

* 3차원 변형 함수

| 종류                       | 설명                                               |
| -------------------------- | -------------------------------------------------- |
| translate3d(tx, ty, tz)    | 지정한 크기만큼 x축, y축, z축으로 이동합니다.      |
| translateZ(tz)             | 지정한 크기만큼 z축으로 이동합니다.                |
| scale3d(sx, sy, sz)        | 지정한 크기만큼 x축, y축, z축으로 확대∙축소합니다. |
| scaleZ(sz)                 | 지정한 크기만큼 z축으로 확대∙축소합니다.           |
| rotate(rx, ry, 각도)       | 지정한 각도만큼 회전합니다.                        |
| rotate3d(rx, ry, rz, 각도) | 지정한 각도만큼 회전합니다.                        |
| rotateX(각도)              | 지정한 각도만큼 x축으로 회전합니다.                |
| rotateY(각도)              | 지정한 각도만큼 y축으로 회전합니다.                |
| rotateZ(각도)              | 지정한 각도만큼 z축으로 회전합니다.                |
| perspective(길이)          | 입체적으로 보일 수 있도록 깊잇값을 지정합니다.     |

### transition

> 하나의 스타일을 완전히 다른 스타일로 바꿈

| 종류                       | 설명                                 |
| -------------------------- | ------------------------------------ |
| transition-property        | 트랜지션의 대상을 지정합니다.        |
| transition-duration        | 트랜지션을 실행할 시간을 지정합니다. |
| transition-timing-function | 트랜지션의 실행 형태를 지정합니다.   |
| transition-delay           | 트랜지션의 지연 시간을 지정합니다.   |
| transition                 | 위의 속성들을 한꺼번에 정합니다.     |

`transition-property: all | none | <속성 이름>`

`transition-duration: <시간>`

`transition-timing-function: linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(n, n, n, n)`

`transition-delay: <시간>`

`transition: <transition-property값> | <transition-duration값> | <transition-timing-function값> | <transition-delay값>`

### animation

| 종류                      | 설명                                                         |
| ------------------------- | ------------------------------------------------------------ |
| @keyframes                | 애니메이션이 바뀌는 지점을 지정합니다.                       |
| animation-delay           | 애니메이션의 시작 시간을 지정합니다.                         |
| animation-direction       | 애니메이션을 종료한 뒤 처음부터 시작할지, 역방향으로 진행할지 지정합니다. |
| animation-duration        | 애니메이션의 실행 시간을 지정합니다.                         |
| animation-iteration-count | 애니메이션의 반복 횟수를 지정합니다.                         |
| animation-name            | @keyframes로 설정해 놓은 중간 상태를 지정합니다.             |
| animation-timing-function | 키프레임의 전환 형태를 지정합니다.                           |
| animation                 | animation 속성을 한꺼번에 묶어서 지정합니다.                 |

```css
@keyframes <이름> {
    <선택자> { <스타일> }
}
```

`animation-name: <키프레임 이름> | none`

`animation-duration: <시간>`

`animation-direction: normal | reverse | alternate | alternate-reverse`

`animation-iteration-count: <숫자> | infinite`

`animation-timing-function: linear | ease | ease-in | ease-out | ease-in-out | cubic-bezier(n, n, n, n)`


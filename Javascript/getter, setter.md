# getter, setter

object 내의 함수들을 괄호없이 쓸 수 있게 만들어주는 키워드

**데이터의 무결성을 보존하기 위해 쓰는 키워드**

원본 데이터는 immutable 해야한다



#### 함수로 object 데이터를 꺼내는 방법

```js
var 사람 = {
    name : 'Yun',
    age : 27,
}
```

내년 나이를 출력해보고 싶으면? **내년 나이를 출력해주는 함수를 만들어 사용**

```js
var 사람 = {
    name : 'Yun',
    age : 27,
    nextAge(){
        return this.age + 1
    }
}
```

**사람.nextAge()** 을 사용하면 내년 나이가 출력된다

굳이 이렇게 하는 이유?

- object 안의 데이터가 복잡할 수록 함수 만들어놓는게 데이터 깨내기 쉽다
- 내부에 있는 name, age 변수를 건드리지 않아서 실수를 방지할 수 있어 안전하다

#### 함수로 object 데이터를 수정하는 방법

**데이터 수정을 위한 함수를 만들어 사용**

```js
var 사람 = {
    name : 'Yun',
    age : 27,
    setAge(나이){
        this.age = 나이
        // this.age = parseInt(나이) 안전장치
    }
}
사람.setAge(30);
```

사람.setAge(30) 이렇게 쓰면 자유롭게 나이 변경이 가능하다

굳이 이렇게 하는 이유?

- 내부에 있는 name, age 변수를 직접 건드리지 않아서 실수를 방지할 수 있다

#### 함수 쓰기 복잡하다면 get/set 키워드를 붙이자

함수를 만들어쓴다면 소괄호까지 써야하고 데이터 집어넣기 복잡해질수있다는 단점이있다

그렇다면 get/set 키워드를 함수 옆에 추가하면 된다

```js
var 사람 = {
    name : 'Yun',
    age : 27,
    set setAge(나이){
        this.age = parseInt(나이)
    }
}
사람.setAge = 30; //set 키워드를 추가하면 이렇게 함수 사용가능
```

set 붙은 함수들은 setter 라고 부른다

```js
var 사람 = {
    name : 'Yun',
    age : 27,
    get nextAge(){
        return this.age + 1
    }
}
console.log(사람.nextAge)
```

get 키워드를 사용하면 소괄호 없이 nextAge를 사용해서 데이터를 꺼낼 수 있다

get 붙은 함수들은 getter 라고 부른다

#### get/set 사용하는 기준은

데이터를 뽑아주는, 가져와주는, get 해주는 함수들은 get 쓰면 되고

데이터를 입력해주는, 수정해주는, set 해주는 함수들은 set 쓰면된다.

set 함수는 데이터를 입력해서 수정해주는 함수니까 파라미터가 한개 꼭 존재해야하고 get 함수는 파라미터가 있으면 안되고 함수 내에 return을 가져야한다
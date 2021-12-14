# 알고리즘 tip

## 입출력 빨리 받기

```python
from sys import stdin, stdout
input = stdin.readline
print = stdout.write
```

## 2차원 배열 입력

```
3
1 2 3
4 5 6
7 8 9
```

```python
arr = [list(map(int, input().split())) for _ in range(int(input()))]
```



```
4 10 20 30 40
3 7 5 12
3 125 15 25
```

```python
N, *arr = map(int, input().split())
```



```
3
AAAA 
ABCA 
AAAA
```

```python
arr = [list(input()) for _ in range(N)]
```

## 배열 출력

```python
arr = [1, 2, 3, 4]
print("".join(map(str, arr)))
=> 1234
```

```python
arr = [1, 2, 3, 4]
print(*arr)
=> 1 2 3 4
```



## 진법

* 10진수 -> 2, 8, 16진수 변환

```python
bin(42)
oct(42)
nex(42)
```

* 2, 8, 16진수 -> 10진수 변환

```python
int('0b111100', 2)
int('0o74', 8)
int('0x3c', 16)
```



## 문자열

* 문자열 거꾸로

```python
alph = "ABCD"
alph[::-1]
```

* 문자열 <--> 아스키코드

```python
ord() # 문자를 아스키코드로 변환하는 함수
chr() # 아스키코드를 문자로 변환하는 함수
```



## 배열

* 배열 초기화

```python
3, 5

N, M = map(int, input().split())
arr = [[0]*N for _ in range(M)]
```

* 배열의 원소를 거꾸로

```python
arr.reverse()
```

* 배열 원소 갯수

```python
list.count(찾는 값)
str.count(찾는 값)
```

* 원소 중복 제거

```python
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd']
alpha = list(set(alpha))
```

```python
lst = [[1,2], [1,2], [1]]
print(list(set(map(tuple, lst))))
```

* 배열 정렬

```python
arr.sort()
arr.sort(reverse=True)
arr.sort(key=lambda x:(x[0], x[1]))
=> 내림차순은?
-x[0]
```

* 삼항 연산자

```python
if a > b:
    res = a
else:
    res = b
```

```python
[True 조건] if 조건 else [False 조건]
res = a if a > b else b
```




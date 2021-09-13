# 재귀

* 재귀 단계
  * 함수가 자기 자신을 호출하는 부분
* 기본 단계
  * 함수가 자기 자신을 다시 호출하지 않는 경우, 즉 무한 반복으로 빠져들지 않게 하는 부분

```python
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
```


## 순열, 조합

순열과 조합의 가장 큰 차이점 => 순서가 있냐 없냐 !

* 순열은 순서가 있는 조합이다.
  * 순서를 고려한다는 것은 순서가 바뀌면 다른 것으로 취급함
* 조합은 순서를 생각하지 않고 선택만 한다.

순열 => 자물쇠 4자리 숫자 맞추기 1,2,3,4 와 4,3,2,1은 다르다.

조합 => 과일쥬스만들기 바나나 사과 딸기를 넣든 딸기 바나나 사과를 넣든 상관없다.

### itertools를 사용한 조합

```python
from itertools import combinations
print(list(combinations([1, 2, 3, 4], 3)))
```

`combinations`의 첫 번째 인자에 배열을 넣고, 두 번째 인자에는 `nCm`에서 m에 해당하는 값을 넣는다.

```python
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```



```python
for i in range(0, N-1):
    for j in range(i+1, N):
        print(i, j)
        
list(combinations([0, 1, 2, 3], 2))
```

### 순열

```python
from itertools import permutations
print(list(permutations(arr, M)))
```

### 빈도 계산

`Counter`

```python
from collections import Counter
```


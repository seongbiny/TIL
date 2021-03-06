# 배열 2 (Array 2)

### 배열 : 2차 배열

* 배열 순회
  * n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

**행 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[i])):
        Array[i][j]
```

**열 우선 순회**

```python
# i 행의 좌표
# j 열의 좌표
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j] 
```

지그재그 순회

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j) * (i % 2)]
```

**델타를 이용한 2차 배열 탐색**

> 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

```python
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < m:
                arr[nx][ny]
```

### 부분집합 생성

> 집합의 원소가  n개일 때, 공집합을 포함한 부분집합의 수는 2^n개이다.

{1, 2, 3, 4} => 2 x 2 x 2 x 2 = 16가지

1. 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

```python
# 간결 ver.
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)              # n : 원소의 개수
for i in range(1<<n):     # 1<<n : 부분 집합의 개수
    for j in range(n+1):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j):    # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=", ")
        print()
    print()
```

### 검색

> 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
>
> 목적하는 탐색 키를 가진 항목을 찾는 것
>
> 탐색 키 : 자료를 구별하여 인식할 수 있는 키

**순차 검색, 이진 검색, 해쉬**

#### 순차 검색

* 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  * 가장 간단하고 직관적인 검색 방법
  * 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  * 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임
* 2가지 경우 : 1. 정렬되어 있지 않은 경우 2. 정렬되어 있는 경우

**정렬되어 있지 않은 경우**

첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.

키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.

자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

* 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
* 시간 복잡도 : O(n)

**정렬되어 있는 경우**

> 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
>
> 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.

* 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
* 시간 복잡도 : O(n)

### 바이너리 서치

> 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
>
> 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
>
> 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

* 검색 과정
  * 자료의 중앙에 있는 원소를 고른다.
  * 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  * 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  * 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

### 선택 정렬

> 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

* 정렬 과정
  * 주어진 리스트 중에서 최소값을 찾는다.
  * 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  * 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
* 시간 복잡도 : O(n^2)

```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            min = j
        a[i], a[min] = a[min], a[i]
```

### 셀렉션 알고리즘

> 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
>
> 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

* 선택 과정
  * 정렬 알고리즘을 이용하여 자료 정렬하기
  * 원하는 순서에 있는 원소 가져오기
* k번째로 작은 원소를 찾는 알고리즘

```python
def select(list, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]
```




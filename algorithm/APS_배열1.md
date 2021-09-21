# 1. 배열 1(Array 1)

### 알고리즘

 #### 빅오 표기법(Big-O)

```
O(1) – 상수 시간 : 문제를 해결하는데 오직 한 단계만 처리함.
O(log n) – 로그 시간 : 문제를 해결하는데 필요한 단계들이 연산마다 특정 요인에 의해 줄어듬.
O(n) – 직선적 시간 : 문제를 해결하기 위한 단계의 수와 입력값 n이 1:1 관계를 가짐.
O(n log n) : 문제를 해결하기 위한 단계의 수가 N*(log2N) 번만큼의 수행시간을 가진다. (선형로그형)
O(n^2) – 2차 시간 : 문제를 해결하기 위한 단계의 수는 입력값 n의 제곱.
O(C^n) – 지수 시간 : 문제를 해결하기 위한 단계의 수는 주어진 상수값 C 의 n 제곱.
```

* O(1) : 상수

  ```PYTHON
  def hello_world():
      print("hello, world!")
  ```

* O(N) : 선형

  * 입력이 증가하면 처리 시간 또는 메모리 사용이 선형적으로 증가한다.

  ```python
  def print_each(li):
      for item in li:
          print(item)
  ```

* O(N^2) : Square

  * 반복문이 두 번 있는 경우

  ```python
  def print_each_n_times(li):
      for n in li:
          for m in li:
              print(n,m)
  ```

* O(log n) or O(n log n)

  * 주로 입력 크기에 따라 처리 시간이 증가하는 정렬 알고리즘에서 많이 사용된다.

  ```python
  def binary_search(li, item, first=0, last=None):
      if not last:
          last = len(li)
          
      midpoint = (last - first) / 2 + first
      
      if li[midpoint] == item:
          return midpoint
      
      elif li[midpoint] > item:
          return binary_search(li, item, first, midpoint)
      
      else:
          return binary_search(li, item, midpoint, last)
  ```

### 배열

**1차원 배열의 선언**

`Arr = list()` `Arr=[]`

**1차원 배열의 접근**

`Arr[0] = 10;` `Arr[idx] = 20;`

* 낙차문제 ??

### 정렬

**대표적인 정렬 방식의 종류**

버블 정렬 , 카운팅 정렬, 선택 정렬, 퀵 정렬, 삽입 정렬, 병합 정렬

#### 버블 정렬

> 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

* 정렬 과정

  * 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
  * 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
  * 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.

* 시간 복잡도

  * O(n^2)

* 배열을 활용한 버블 정렬

  ```python
  def Bubblesort(a): # 정렬할 List
      for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
          for j in range(0, i):
              if a[j] > a[j+1]:
                  a[j], a[j+1] = a[j+1], a[j]
  ```

#### 카운팅 정렬

> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

* 제한 사항
  * 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  * 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
* 시간 복잡도
  * O(n + k) : n은 리스트 길이, k는 정수의 최대값

```python
def counting_sort(data, count, result):
    for i in data:
        count[i] += 1   # data 요소의 출현 횟수
    print("count", count)

    for i in range(len(count)-1):
        count[i+1] += count[i]  # 누적 count
    print("누적 count", count)

    for i in range(len(data)-1, -1, -1):
        result[count[data[i]] - 1] = data[i]
        count[data[i]] -= 1
        print("result", result, "count", count)

data = [3, 2, 5, 4, 2, 1, 5, 2, 2, 1]
count = [0 for _ in range(max(data)+1)]   # 최댓값
result = [0 for _ in range(len(data))]  # data 길이만큼
counting_sort(data, count, result)
print(result)
```

* baby-gin game ?

### 완전 검색 (완전 탐색)

> 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법이다.
>
> Brute-force 라고도 부른다.

**완전 탐색 기법을 활용하는 방법**

1. 해결하고자 하는 문제의 가능한 경우의 수를 대략적으로 계산한다.
2. 가능한 모든 방법을 다 고려한다.
3. 실제 답을 구할 수 있는지 적용한다.

2-1 Brute Force 기법 - 반복 / 조건문을 활용해 모두 테스트하는 방법

2-2 순열 - n개의 원소 중 r 개의 원소를 중복 허용 없이 나열하는 방법

2-3 재귀 호출

2-4 비트마스크 - 2진수 표현 기법을 활용하는 방법

2-5 BFS, DFS를 활용하는 방법

### 그리디 ( 탐욕 알고리즘 )

> 탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법
>
> 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해나가는 방식으로 진행하여 최종적인 해답에 도달한다.

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해집합(Solution Set)에 추가한다.
2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는지를 검사한다.
3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1.의 해 선택부터 다시 시작한다.


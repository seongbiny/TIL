# combination & permutation & powerset

### combination1

```python
N = 4
R = 2

arr = [1, 2, 3, 4]
sel = [0] * R # 내가 뽑을 공간 미리 확보 

# idx : arr에서 시작하는 위치
# s_idx : 내가 뽑고 있는 위치
def comb(idx, s_idx):
    if s_idx == R:
        print(sel)
        return
    elif idx == N:
        return
    else:
        sel[s_idx] = arr[idx]
        comb(idx+1, s_idx+1) # 해당 idx번째 자리를 뽑거나
        comb(idx+1, s_idx) # 해당 idx번째 자리를 뽑지 않거나

comb(0, 0)
```

### combination2

```python
N = 4
R = 2

arr = [1, 2, 3, 4]
sel = [0] * R 

def comb(idx, s_idx):
    if s_idx == R:
        print(sel)
        return
    
    for i in range(idx, N):
        sel[s_idx] = arr[i]
        comb(i+1, s_idx+1)
        
comb(0, 0)
```

### combination3

```python
N = 4
R = 3

arr = [1, 2, 3, 4]

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])
```

### combination4

```python
# n개에서 r개를 고르는 조합, s 선택 구간의 시작, k 고른 개수

def nCr(n, r, s, k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1): # n-r+k 선택할 수 있는 구간의 끝
            comb[k] = i
            nCr(n, r, i+1, k+1)
            
N = 5
R = 3

comb = [0] * R

nCr(N, R, 0, 0)
```

---

### permutation_반복문

```python
arr = [1, 2, 3]

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```

### permutation_비트

```python
arr = [1, 2, 3, 4]
N = 4

sel = [0] * N

def perm(idx, check: int):
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j):
            continue

        sel[idx] = arr[j]
        perm(idx+1, check | (1 << j))

perm(0, 0)
```

###  permutation_스왑

```python
arr = [1, 2, 3]

N = 3

def perm(idx):
    if idx == N:
        print(arr)
        return
    
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]
        
perm(0)
```

### permutation_재귀

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N # 내가 직접 뽑은거 넣을 리스트
check = [0] * N # 내가 사용한거 체크할 리스트

def perm(idx):
    # idx : 내가 뽑고 있는 자리
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1 # 사용했다고 체크
                perm(idx+1)
                check[i] = 0 # 원상복귀
                
perm(0)                
```

---

### powerset_반복문

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

### powerset_비트

```python
hamberger = ['패티', '양상추', '치즈', '피클']

N = len(hamberger)
for i in range(1 << N):
    for j in range(N):
        if i & (1 << j): # 해당 j번째 비트가 1이라는 뜻 -> 값이 존재
            print(hamberger[j], end=' ')
    print()
```

### powerset_재귀

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N

def powerset(idx):
    if idx == N:
        print(sel)
    else:
        # 뽑고
        sel[idx] = 1
        powerset(idx + 1)
        # 안뽑고
        sel[idx] = 0
        powerset(idx + 1)
        
powerset(0)
```


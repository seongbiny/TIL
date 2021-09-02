# 이진 탐색

사전에서 단어를 찾을 때 한장한장 넘기는 것 보다 중간부터 찾아보는게 더 빠르다.

입력으로 정렬된 원소 리스트를 받고, 리스트에 원하는 원소가 있으면 그 원소의 위치를 반환한다. 아니면 null 값을 반환한다.

```python
def binary_search(list, item):
    # low와 high는 전체 리스트 중에서 어떤 부분을 탐색해야 하는지 알려준다.
    low = 0
    high = len(list)-1
    
    while low <= high: # 만약 탐색 범위를 하나로 줄이지 못했으면 계속 실행
        mid = (low + high) // 2 # 가운데 숫자를 확인
        guess = list[mid]
        
        if guess == item: # 아이템을 찾음
            return mid
       	if guess > item: # 추측한 숫자가 큼
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # 1
print(binary_search(my_list, -1)) # None
```

| 단순 탐색                  | 이진 탐색                |
| -------------------------- | ------------------------ |
| 100개의 item -> 100번 추측 | 100개의 item -> 7번 추측 |
| O(n)                       | O(log n)                 |


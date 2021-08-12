'''
데이터가 정렬되어있지 않은 경우
def sequetialSearch(key, lst):
    idx = 0
    N = len(lst)
    #idx를 증가하면서 key를 찾는다.
    #key를 찾을 때까지 idx를 증가한다.
    while idx<N and key != lst[idx]:
        idx += 1

    if idx == N: # 와일문 조건이 2개니까
        return -1
    else:
        return idx

lst = [4, 9, 11, 23, 2, 19, 7]
print(sequetialSearch(2, lst))
print(sequetialSearch(8, lst))
print(sequetialSearch(4, lst))  #첫번째 데이터와
print(sequetialSearch(7, lst))  #마지막 데이터를 꼭 확인해보자
'''

# 데이터가 정렬 되어있는 경우
def sequentialSearch2(key, lst):
    N = len(lst)
    idx = 0
    while idx < N and key > lst[idx]:
        idx += 1

    if idx<N and key == lst[idx]:
        return idx
    else:
        return -1
    #if idx == N:
    #    return -1


lst = [2, 4, 7, 9, 11, 19, 23]
print(sequentialSearch2(7, lst))
print(sequentialSearch2(2, lst))
print(sequentialSearch2(23, lst))
print(sequentialSearch2(5, lst))
print(sequentialSearch2(1, lst))
print(sequentialSearch2(24, lst))
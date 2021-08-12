lst = [64, 25, 10, 22, 11]
N = len(lst)

#i가 0 ~ N-2 포함 까지

def selectionS(lst):
    N = len(lst)
    for i in range(N-1):
        # i번째로 작은 값을 찾아서 i번째 위치에 있는 자료와 교환한다.
        # i에서 시작해서
        #minV = lst[i]
        minP = i
        for j in range(i+1, N):
            if lst[minP] > lst[j]: #minV > lst[j]:
                #minV = lst[j]
                minP = j

        lst[minP], lst[i] = lst[i], lst[minP]
selectionS(lst)
print(lst)
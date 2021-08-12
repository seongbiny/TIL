def binaryS(key, lst):
    start = 0
    end  = len(lst)-1
    while start <= end:
        m = (start + end)//2
        if key == lst[m]:
            return m
        if key <= lst[m]:
            end = m-1
        else:
            start = m+1

    return -1 # start 와 end 위치가 뒤집어질때까지 못찾아서 반복문 빠져나왔으므로

lst = [2, 4, 7, 9, 11, 19, 23]
print(binaryS(7, lst))
print(binaryS(2, lst))
print(binaryS(23, lst))
print(binaryS(5, lst))
print(binaryS(1, lst))
print(binaryS(24, lst))

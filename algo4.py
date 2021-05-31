def find_min(a):
    n = len(a)
    min_v = 0
    for i in range(1, n):
        if a[i] < a[min_v]:
            min_v = i
    return min_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))

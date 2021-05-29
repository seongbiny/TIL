def sum_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

def sum_x(x):
    return x*(x+1) // 2

print(sum_n(10))
print(sum_n(100))
print()
print(sum_x(10))
print(sum_x(100))

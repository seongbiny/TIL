import random

total = 1000000
ev = 0

for i in range(total):
    x = random.random()
    y = random.random()

    if x ** 2 + y ** 2 <= 1.0:
        ev += 1

print((ev / total) * 4 )

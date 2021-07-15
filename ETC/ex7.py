import random

total = 100000000000
ev = 0

for i in range(total):
    if random.randint(1, 6) == 2:
        ev = ev + 1

print(ev / total)

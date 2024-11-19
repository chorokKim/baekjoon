import math

N = input()

count = [0 for _ in range(10)]

for n in N:
    count[int(n)] += 1

set69 = math.ceil((count[6] + count[9]) / 2)
count[6], count[9] = 0, 0
max_count = max(count)
if max_count > set69:
    print(max_count)
else:
    print(set69)
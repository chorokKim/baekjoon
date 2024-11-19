A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)
arr = [0 for _ in range(10)]

for res in result:
    arr[int(res)] += 1
for a in arr:
    print(a)
N = int(input())
arr = [int(i) for i in input().split(" ")]
v = int(input())

count = [0 for _ in range(201)]
result = 0

for a in arr:
    if a == v:
        result += 1
print(result)
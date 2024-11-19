n = int(input())
arr = [int(i) for i in input().split(" ")]
x = int(input())

count = [0 for _ in range(2000000)]
result = 0

for a in arr:
    if count[x - a - 1] == 1:
        result += 1
    count[a - 1] += 1
print(result)
s = input()

arr = [0 for _ in range(26)]
for i in s:
    idx = ord(i) - ord("a")
    arr[idx] += 1

print(*arr)
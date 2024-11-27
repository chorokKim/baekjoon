from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
stack = []
result = [-1] * N
idx = N - 1

while idx >= 0:
    num = arr[idx]
    while stack and stack[-1] <= num:
        stack.pop()
        
    if stack:
        result[idx] = stack[-1]
    stack.append(num)
    idx -= 1
print(*result)
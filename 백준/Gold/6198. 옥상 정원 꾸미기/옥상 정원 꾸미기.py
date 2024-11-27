from sys import stdin

N = int(stdin.readline())
buildings = [int(stdin.readline()) for _ in range(N)]
stack = []
result = 0

for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    result += len(stack) - 1

print(result)
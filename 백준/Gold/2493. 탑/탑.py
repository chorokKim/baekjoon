from sys import stdin

N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
stack = []
result = [0] * len(towers)

for i in range(N):
    t = towers[i]
    while stack and towers[stack[-1]] < t:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, result))))
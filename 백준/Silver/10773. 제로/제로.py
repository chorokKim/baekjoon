from sys import stdin

stack = []

K = int(stdin.readline())
for _ in range(K):
    command = stdin.readline().strip()
    if command == "0":
        stack.pop()
    else:
        stack.append(int(command))
print(sum(stack))
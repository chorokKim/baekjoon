from sys import stdin

stack = []

N = int(input())
for _ in range(N):
    command = stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    else:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
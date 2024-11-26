from sys import stdin

n = int(stdin.readline())
stack = []
command = []
possibility = True
i = 1
for _ in range(n):
    num = int(stdin.readline().strip())
    while i <= num:
        stack.append(i)
        command.append("+")
        i += 1
    if stack[-1] == num:
        if len(stack) == 0:
            possibility = False
            break
        stack.pop()
        command.append("-")
    else:
        possibility = False
if possibility:
    for cmd in command:
        print(cmd)
else:
    print("NO")
from sys import stdin

stack = []
sticks = stdin.readline().strip()
answer = 0
for i, s in enumerate(sticks):
    if s == "(":
        stack.append(s)
    else:
        if stack and sticks[i - 1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)
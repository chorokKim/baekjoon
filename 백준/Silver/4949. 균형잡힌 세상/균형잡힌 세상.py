from sys import stdin

while True:
    line = stdin.readline()
    if line == ".\n":
        break
    stack = []
    result = "yes"
    for c in line:
        if c in "([":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = "no"
                break
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                result = "no"
                break
    
    if stack:
        result = "no"
    print(result)
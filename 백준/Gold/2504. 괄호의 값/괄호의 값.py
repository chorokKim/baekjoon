from sys import stdin

stack = []
string = stdin.readline().strip()
sum = 0
multi = 1
for i in range(len(string)):
    if string[i] == "(":
        multi *= 2
        stack.append(string[i])
    elif string[i] == "[":
        multi *= 3
        stack.append(string[i])
    elif string[i] == ")":
        if stack:
            if stack[-1] != "(":
                print(0)
                exit(0)
            if string[i - 1] == "(":
                sum += multi
            stack.pop()
            multi //= 2
        else:
            print(0)
            exit(0)
    else:
        if stack:
            if stack[-1] != "[":
                print(0)
                exit(0)
            if string[i - 1] == "[":
                sum += multi
            stack.pop()
            multi //= 3
        else:
            print(0)
            exit(0)

if stack:
    print(0)
else:
    print(sum)
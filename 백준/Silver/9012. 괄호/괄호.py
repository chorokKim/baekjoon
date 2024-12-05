from sys import stdin

N = int(stdin.readline())

for _ in range(N):
    string = stdin.readline().strip()
    stack = []
    answer = "YES"
    for s in string:
        if s == "(":
            stack.append(s)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = "NO"
                continue
    
    if stack:
        answer = "NO"
    print(answer)
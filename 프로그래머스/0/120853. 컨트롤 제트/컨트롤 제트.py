def solution(s):
    stack = []
    for i in s.split():
        if i == "Z":
            stack.pop()
            continue
        stack.append(int(i))
    return sum(stack)
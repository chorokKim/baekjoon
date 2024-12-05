from sys import stdin

N = int(stdin.readline())
answer = 0
for _ in range(N):
    word = stdin.readline().strip()
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    
    if not stack:
        answer += 1
print(answer)
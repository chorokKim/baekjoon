from sys import stdin

sel = []

def backtracking(s):
    if len(sel) == 6:
        print(*sel)
        return
    
    for i in range(s, len(case)):
        if case[i] not in sel:
            sel.append(case[i])
            backtracking(i + 1)
            sel.pop()
    
while True:
    inp = list(map(int, stdin.readline().split()))
    if inp[0] == 0:
        break
    case = inp[1:]
    case.sort()

    backtracking(0)
    print()
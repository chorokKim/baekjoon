from sys import stdin


L, C = map(int, stdin.readline().split())
letters = sorted(map(str, stdin.readline().split()))

sel = []
def backtracking(k):
    if len(sel) == L:
        v, c = 0, 0
        for s in sel:
            if s in "aeiou":
                v += 1
            else:
                c += 1
        if v > 0 and c > 1:
            print(''.join(sel))
            return
    
    for i in range(k, C):
        idx = ord(letters[i]) - ord('a')
        sel.append(letters[i])
        backtracking(i + 1)
        sel.pop()

backtracking(0)
from sys import stdin

N, M = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))
sel = []

def backtracking(k):
    if len(sel) == M:
        print(*sel)
        return
    for i in range(k, N):
        sel.append(arr[i])
        backtracking(i + 1)
        sel.pop()

backtracking(0)
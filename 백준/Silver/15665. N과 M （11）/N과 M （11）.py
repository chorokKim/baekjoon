from sys import stdin

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
sel = []
isused = [False] * N

def backtracking(k):
    if len(sel) == M:
        print(*sel)
        return
    tmp = 0
    for i in range(N):
        if tmp != arr[i]:
            sel.append(arr[i])
            tmp = arr[i]
            backtracking(k)
            sel.pop()

backtracking(0)
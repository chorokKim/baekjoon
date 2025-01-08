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
        if not isused[i] and tmp != arr[i]:
            sel.append(arr[i])
            isused[i] = True
            tmp = arr[i]
            backtracking(k + 1)
            sel.pop()
            isused[i] = False

backtracking(0)
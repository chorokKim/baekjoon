from sys import stdin

N, M = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))
sel = [0] * M
isused = [False] * N

def backtracking(k):
    if k == M:
        print(*sel)
        return
    for i in range(N):
        if not isused[i]:
            sel[k] = arr[i]
            isused[i] = True
            backtracking(k + 1)
            isused[i] = False

backtracking(0)
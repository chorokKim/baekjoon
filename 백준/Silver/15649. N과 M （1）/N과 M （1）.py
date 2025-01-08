from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [0] * M
isused = [False] * 10

def backtracking(k):
    if k == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            backtracking(k + 1)
            isused[i] = False
        else:
            pass

backtracking(0)
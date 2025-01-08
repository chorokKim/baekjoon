from sys import stdin

N, M = map(int, stdin.readline().split())
arr = []

def backtracking(k):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        arr.append(i)
        backtracking(k + 1)
        arr.pop()

backtracking(1)
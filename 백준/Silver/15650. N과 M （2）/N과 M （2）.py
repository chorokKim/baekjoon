from sys import stdin

N, M = map(int, stdin.readline().split())
arr = []

def backtracking(k):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(k, N + 1):
        arr.append(i)
        backtracking(i + 1)
        arr.pop()

backtracking(1)
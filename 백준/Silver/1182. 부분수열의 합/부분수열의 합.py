from sys import stdin

N, S = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
selected = []
count = 0

def backtracking(k):
    global count
    if sum(selected) == S and len(selected) > 0:
        count += 1
    
    for i in range(k, N):
        selected.append(arr[i])
        backtracking(i + 1)
        selected.pop()


backtracking(0)
print(count)
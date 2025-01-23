from sys import stdin


def backtracking(k):
    global broken
    global mx
    if k == N:
        mx = max(broken, mx)
        return
    if S[k] <= 0 or broken == N - 1:
        backtracking(k + 1)
        return
    for i in range(N):
        if i == k or S[i] <= 0:
            continue
        S[k] -= W[i]
        S[i] -= W[k]
        if S[k] <= 0:
            broken += 1
        if S[i] <= 0:
            broken += 1
        backtracking(k + 1)
        if S[k] <= 0:
            broken -= 1
        if S[i] <= 0:
            broken -= 1
        S[k] += W[i]
        S[i] += W[k]

N = int(stdin.readline())
S, W = [], []
for _ in range(N):
    s, w = map(int, stdin.readline().split())
    S.append(s)
    W.append(w)
broken = 0
mx = 0
backtracking(0)
print(mx)
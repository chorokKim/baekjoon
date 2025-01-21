from sys import stdin

N = int(stdin.readline())
d = [0 for _ in range(N + 1)]
proc = [0 for _ in range(N + 1)]

d[1] = 0
proc[1] = 0
for i in range(2, N + 1):
    d[i] = d[i - 1] + 1
    proc[i] = i - 1
    if i % 2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
        proc[i] = i // 2
    if i % 3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
        proc[i] = i // 3

print(d[N])
p = N
while True:
    print(p, end=' ')
    if p == 1:
        break
    p = proc[p]
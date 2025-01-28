from sys import stdin

N = int(stdin.readline())
ropes = []
for _ in range(N):
    ropes.append(int(stdin.readline()))

ropes.sort(reverse=True)

mw = 0
for i in range(1, len(ropes) + 1):
    w = ropes[i - 1] * i
    mw = max(mw, w)
print(mw)
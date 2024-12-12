from sys import stdin
from collections import deque

F, S, G, U, D = map(int, stdin.readline().split())
building = [-1 for _ in range(F + 1)]

building[S] = 0
queue = deque([S])
move = [U, -D]

while queue:
    c = queue.popleft()
    for m in move:
        n = c + m
        if n <= 0 or n > F or building[n] > -1:
            continue
        building[n] = building[c] + 1
        queue.append(n)

if S == G:
    print(0)
elif building[G] == -1:
    print("use the stairs")
else:
    print(building[G])
from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
vis = [-1 for _ in range(200000)]
vis[N] = 0
queue = deque([N])
while vis[K] == -1:
    cur = queue.popleft()
    move = [1, -1, cur]
    for m in move:
        dest = cur + m
        if dest >= 200000 or dest < 0:
            continue
        if vis[dest] >= 0:
            continue
        vis[dest] = vis[cur] + 1
        queue.append(dest)
print(vis[K])
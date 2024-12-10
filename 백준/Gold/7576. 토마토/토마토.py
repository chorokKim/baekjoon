from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
board = []
vis = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    board.append(row)
    vis.append([0] * M)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
for x in range(N):
    for y in range(M):
        if board[x][y] != 1 or vis[x][y] > 0:
            continue
        vis[x][y] = 1
        queue.append([x, y])
while queue:
    cx, cy = queue.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == -1 or vis[nx][ny] > 0:
            continue
        vis[nx][ny] = vis[cx][cy] + 1
        queue.append([nx, ny])
days = -1
for x in range(N):
    for y in range(M):
        if board[x][y] != -1 and vis[x][y] == 0:
            print(-1)
            exit(0)
        days = max(days, vis[x][y] - 1)
print(days)
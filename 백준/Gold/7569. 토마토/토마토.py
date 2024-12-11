from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())
board = []
vis = []
for _ in range(H):
    tmp_board = []
    tmp_vis = []
    for _ in range(N):
        row = list(map(int, stdin.readline().split()))
        tmp_board.append(row)
        tmp_vis.append([-1] * M)
    board.append(tmp_board)
    vis.append(tmp_vis)

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()
days = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if board[z][x][y] != 1 or vis[z][x][y] != -1:
                continue

            vis[z][x][y] = 0
            queue.append([z, x, y])

while queue:
    cz, cx, cy = queue.popleft()
    for i in range(6):
        nz = cz + dz[i]
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nz < 0 or nz >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nz][nx][ny] != 0 or vis[nz][nx][ny] != -1:
            continue

        vis[nz][nx][ny] = vis[cz][cx][cy] + 1
        days = max(days, vis[cz][cx][cy] + 1)
        queue.append([nz, nx, ny])

for z in range(H):
    for x in range(N):
        for y in range(M):
            if vis[z][x][y] == -1 and board[z][x][y] != -1:
                print(-1)
                exit(0)
print(days)
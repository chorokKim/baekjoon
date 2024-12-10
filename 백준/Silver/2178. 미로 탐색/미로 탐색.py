from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = []
vis = []
for _ in range(N):
    row = stdin.readline().strip()
    board.append(row)
    vis.append([-1] * M)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
for x in range(N):
    for y in range(M):
        if board[x][y] != "1" or vis[x][y] >= 0:
            continue
        queue.append([x, y])
        vis[x][y] = 1
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if board[nx][ny] != "1" or vis[nx][ny] >= 0:
                    continue
                vis[nx][ny] = vis[cx][cy] + 1
                queue.append([nx, ny])
                
print(vis[N - 1][M - 1])
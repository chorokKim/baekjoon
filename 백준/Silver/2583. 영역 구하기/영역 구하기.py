from sys import stdin
from collections import deque

M, N, K = map(int, stdin.readline().split())
board = [[0] * N for _ in range(M)]
vis = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
count = 0
area = []
for x in range(M ):
    for y in range(N):
        if board[x][y] == 1 or vis[x][y] == 1:
            continue
        count += 1
        vis[x][y] = 1
        queue.append([x, y])
        a = 1
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                if board[nx][ny] == 1 or vis[nx][ny] == 1:
                    continue
                vis[nx][ny] = 1
                queue.append([nx, ny])
                a += 1
        area.append(a)
print(count)
print(*sorted(area))
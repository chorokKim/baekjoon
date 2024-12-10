from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
vis = []
for i in range(n):
    row = list(map(int, stdin.readline().split()))
    board.append(row)
    vis.append([0] * m)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
max_area = 0
count = 0
for x in range(n):
    for y in range(m):
        if board[x][y] == 0 or vis[x][y] == 1:
            continue
        count += 1
        queue.append([x, y])
        vis[x][y] = 1
        area = 0
        while queue:
            area += 1
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny] != 1 or vis[nx][ny] == 1:
                    continue
                vis[nx][ny] = 1
                queue.append([nx, ny])
        max_area = max(max_area, area)

print(count)
print(max_area)
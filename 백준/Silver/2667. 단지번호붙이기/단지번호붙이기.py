from sys import stdin
from collections import deque

N = int(stdin.readline())
board = []
vis = []
for _ in range(N):
    row = stdin.readline().strip()
    board.append(row)
    vis.append([0] * N)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque()
count = 0
area = []
for x in range(N):
    for y in range(N):
        if board[x][y] == "0" or vis[x][y] == 1:
            continue
        vis[x][y] = 1
        queue.append([x, y])
        count += 1
        a = 1
        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if board[nx][ny] == "0" or vis[nx][ny] == 1:
                    continue
                vis[nx][ny] = 1
                queue.append([nx, ny])
                a += 1
        area.append(a)
print(count)
for a in sorted(area):
    print(a)
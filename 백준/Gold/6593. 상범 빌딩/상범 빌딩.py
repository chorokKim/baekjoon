from sys import stdin
from collections import deque

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, stdin.readline().split())
    if [L, R, C] == [0, 0, 0]:
        break
    board = []
    vis = []
    for _ in range(L):
        temp_board = []
        temp_vis = []
        for _ in range(R + 1):
            row = stdin.readline().strip()
            temp_board.append(row)
            temp_vis.append([-1] * C)
        board.append(temp_board)
        vis.append(temp_vis)
    
    queue = deque()
    ez, ex, ey = 0, 0, 0
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if board[z][x][y] == "S":
                    vis[z][x][y] = 0
                    queue.append([z, x, y])
                if board[z][x][y] == "E":
                    ez, ex, ey = z, x, y

    while queue:
        cz, cx, cy = queue.popleft()
        for i in range(6):
            nz = cz + dz[i]
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nz < 0 or nz >= L or nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nz][nx][ny] == "#" or vis[nz][nx][ny] > -1:
                continue
            vis[nz][nx][ny] = vis[cz][cx][cy] + 1
            queue.append([nz, nx, ny])

    if vis[ez][ex][ey] != -1:
        print("Escaped in " + str(vis[ez][ex][ey]) + " minute(s).")
    else:
        print("Trapped!")
from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    board = []
    vis = []
    for _ in range(M):
        board.append([0] * N)
        vis.append([0] * N)

    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        board[x][y] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    cnt = 0
    for x in range(M):
        for y in range(N):
            if board[x][y] != 1 or vis[x][y] == 1:
                continue
            vis[x][y] = 1
            queue.append([x, y])
            cnt += 1
            while queue:
                cx, cy = queue.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if nx < 0 or nx >= M or ny < 0 or ny >=N:
                        continue
                    if board[nx][ny] != 1 or vis[nx][ny] == 1:
                        continue
                    vis[nx][ny] = 1
                    queue.append([nx, ny])
    print(cnt)
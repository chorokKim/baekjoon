from sys import stdin
from collections import deque

N = int(stdin.readline())
board = []
max_level = 0
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    board.append(row)
    max_level = max(max_level, max(row))

def bfs(level):
    vis = [[0] * N for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    cnt = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] <= level or vis[x][y] == 1:
                continue
            vis[x][y] = 1
            queue.append([x, y])
            cnt += 1
            while queue:
                cx, cy = queue.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if board[nx][ny] <= level or vis[nx][ny] == 1:
                        continue
                    vis[nx][ny] = 1
                    queue.append([nx, ny])
    return cnt

max_cnt = 0
for level in range(max_level):
    cnt = bfs(level)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)